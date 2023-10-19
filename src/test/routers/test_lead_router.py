from test.conftest import BaseTestClass


class TestLeadRouter(BaseTestClass):
    def test_create_lead(self, client, lead_create):
        self._generate_support_objects()

        response = client.post('/api/v1/leads', json=lead_create.model_dump())
        assert response.status_code == 201
        assert response.json() == 1

        response = client.post('/api/v1/leads', json=lead_create.model_dump())
        assert response.status_code == 409
        assert response.json() == {'detail': 'lead_already_exists'}

    def test_get_lead(self, client, lead_create):
        self._generate_support_objects()

        client.post('/api/v1/leads', json=lead_create.model_dump())

        response = client.get('/api/v1/leads/1')
        assert response.status_code == 200

    def test_get_leads(self, client):
        self._generate_support_objects()

        for i in range(50):
            year_of_inscription = 2019 if i % 2 == 0 else 2020
            self._generate_lead(
                id=i,
                year_of_inscription=year_of_inscription
            )

        response = client.get('/api/v1/leads', params={'per_page': 10})
        response_json = response.json()
        assert response.status_code == 200
        assert response_json['count'] == 50
        assert len(response_json['results']) == 10
        assert response_json['next_page'] == 2
        assert response_json['previous_page'] is None

        response_1 = client.get(
            '/api/v1/leads',
            params={
                'page': response_json['next_page'],
                'per_page': 10
            }
        )
        response_json_1 = response_1.json()
        assert response_json_1['count'] == 50
        assert len(response_json_1['results']) == 10
        assert response_json_1['next_page'] == 3
        assert response_json_1['previous_page'] == 1

        response_2 = client.get(
            '/api/v1/leads',
            params={
                'page': response_json_1['next_page'],
                'per_page': 10
            }
        )
        response_2_json = response_2.json()
        assert response_2_json['count'] == 50
        assert len(response_2_json['results']) == 10
        assert response_2_json['next_page'] == 4
        assert response_2_json['previous_page'] == 2

        response_3 = client.get(
            '/api/v1/leads',
            params={
                'page': response_2_json['next_page'],
                'per_page': 10
            }
        )
        response_3_json = response_3.json()
        assert response_3_json['count'] == 50
        assert len(response_3_json['results']) == 10
        assert response_3_json['next_page'] == 5
        assert response_3_json['previous_page'] == 3

        response4 = client.get(
            '/api/v1/leads',
            params={
                'page': response_3_json['next_page'],
                'per_page': 10
            }
        )
        response_4_json = response4.json()
        assert response_4_json['count'] == 50
        assert len(response_4_json['results']) == 10
        assert response_4_json['next_page'] is None
        assert response_4_json['previous_page'] == 4

