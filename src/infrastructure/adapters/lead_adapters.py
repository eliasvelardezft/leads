from domain.interfaces import IAdapter


class LeadPersistanceAdapter(IAdapter):
    @staticmethod
    def domain_to_persistance():
        pass

    @staticmethod
    def persistance_to_domain():
        pass


class LeadClientAdapter(IAdapter):
    @staticmethod
    def client_to_domain():
        pass

    @staticmethod
    def domain_to_client():
        pass
