Students (leads) fastapi service

## Domain Modeling

![image](https://github.com/eliasvelardezft/leads/assets/40184787/dc878ebe-4ab7-453e-b6ea-4982140b2dfb)

In the domain, we model the following main entities:

- Lead: These are the students that we are going to register and enroll in courses. The student has a career.
- Enrollment: This is the relationship between a lead and a course (enrollment). Although the lead has a career, they can enroll in courses for subjects that belong to other careers (this can happen according to the university's model, and it is not beneficial to restrict it).
- Course: Models the specific teaching of a subject at a given time by a professor in a specific classroom.

In addition, we have the following supporting classes:

- Address:
- Career: Has a list of subjects. I did this instead of having a subject related to a career because it is common in real-life situations for the same subject to be present in multiple careers (e.g. research methodology).
- Subject
- Status: For handling state, two patterns are implemented:
    1. State changes with history: For a machine learning system that aims to predict dropout, it is valuable to have information about when state changes occur in an enrollment. For example, if all course enrollments for a specific subject have a very short time between transitioning from **progress** to **dropped**, it means that people are prematurely dropping that subject.
    2. State pattern: This is implemented using the IEnrollmentStatus interface, which is implemented by all concrete classes that represent the states in our domain. In the interface, all transition methods (progress(), complete(), drop(), fail()) are defined, and they are only implemented in those states that are allowed to make that specific transition. The great benefit of this is that we avoid conditionals within the transition methods to check if the state is valid for making a specific transition.

## Application Architecture

The application is composed of the following main components:

- **Api**: Connects the app with the outside world. It is structured in a way that allows adding versions in the future. In each version, we find, in addition to the **routers**, the **client adapters** (explained in the *application flow* section), the **dependencies** (to obtain the services with their repositories), **DTOs**, and **api exceptions**.
- **Domain**:
Here we can find the business logic of our application. Specifically, we can find:
    - Models: Class representations of real-world concepts that our application needs to handle.
    - Interfaces: Classes that define the structure for the behavior of the classes we implement in the **infrastructure** layer.
    - Services: These classes are responsible for handling the application logic. Although the services are currently simple in the project's current state, having them provides a perfect place to carry out processes that involve interacting with multiple objects from different classes and have a specific business logic.
    
    If we want to move our application to a completely different project with a different framework, database, configuration, etc., we can move this folder to that project and use it as a base to implement the rest.
    
- **Infrastructure**:
This is where the code is placed to make our business/domain logic work in the context of an application that uses specific libraries.
We can find:
    - The **persistance adapters** (explained in the *application flow* section)
    - The necessary code to create migrations with *alembic*
    - The SQLAlchemy models (Python classes that are converted into database tables by SQLAlchemy)
    - The repositories that implement the interface defined in the domain.
    - The implementation of the IPaginator interface from the domain.

The application is structured as follows:

![image](https://github.com/eliasvelardezft/leads/assets/40184787/043f9f08-6e78-452a-a59f-829d655fcd5e)

**Note**:

The API layer's call to the Infrastructure layer is only in the part of the dependencies to define which implementations of the domain interfaces we are going to use in our app. Outside of that dependency injection part, the API layer and the infrastructure layer independently consume the domain layer.

## Application Flow

![image](https://github.com/eliasvelardezft/leads/assets/40184787/2438a6b4-9c88-44e9-b13b-ebbad47ca131)

Our application has a designated flow for transferring information from the beginning (when the information arrives from the client to our API layer) to the end (when that information is either saved or retrieved from the database).

The conversion between information formats is called from the layers that interact with the outside world. In the case of the **client adapters**, they are called from the **routers** since they convert the incoming (and outgoing) information from the **frontend**. On the other hand, the **persistance adapters** are called from the repositories, as they are the bridge between our **domain** and the **database**.

Having these conversions allows us to model the domain in ways that are very useful for managing business logic in the application but are not as useful for sending to the frontend or saving in the database (such as the use of **value objects**, for example).

### Pagination

For pagination, I decided to use the page/per-page pattern as I find it more convenient for the user than offset/limit. In the **domain**, I have an **IPaginator** interface, which defines the initialization parameters and a **get_response** method. In the service (also part of the domain), we receive the class that implements that interface through dependency injection. The service instantiates the Paginator since it has all the information and objects it needs, and finally returns the paginated information to the router.

Regarding the Paginator implemented in the infrastructure layer, it has private methods to calculate the offset/limit based on page and per_page. Additionally, it receives the repository as a parameter, which it uses to obtain the paginated information from the database (also functioning with filtering). Then, it returns the paginated information (total count, list of elements, next and previous page).
