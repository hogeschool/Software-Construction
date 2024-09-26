# Combining REST and Requirements
Now we have a basic understanding of RESTful APIs and requirements, let's combine the two.

### Question
Looking back at the different types of requirements, which types apply to APIs? 

Choose from:

- Business requirements
- User requirements
- Functional requirements
- Non-functional requirements

### Answer
In short: they all apply.

You might think that user requirements don't apply to APIs. Even though we do not directly interact with the end users, the actual users of our API are our collegue developers.

### Question
What should they need to be able to work with our API?

### Answer
Indeed: good documentation. It is your teams goal to provide good documentation of the CargoHub API during this project.

## Mapping Requirements to RESTful API Design
During the project you get an existing API code base and it is your task to reverse engineer the functional requirements it implements.

### Question
Given the endpoints below, what kind of app does this RESTful API represent?

- `https://api.app.com/lists`
- `https://api.app.com/members`
- `https://api.app.com/lists/tasks`
- `https://api.app.com/lists/tasks/members`

### Answer
It could be the API of a collaborative to-do app.

### Question
The direct users of our API are the developers that need to implement the app. They require that:

- The API should be easy to understand
- The API should be easy to work with

Does the endpoint description satisfy this demand?

### Answer
Not really. It does describe which resources there are and how they relate, but this is not enough to work with this API. For example: it is not clear what properties a member has and how to update those.

### Question
What functional requirements can you deduce from the endpoints and the fact that the API exposes the logic of a collaborative to-do app?

### Possible Answer
It's a to-do app so the API should support:

- Creating a to-do list
- Changing the name of a to-do list
- Remove a to-do list
- Listing the to-do lists
- Adding tasks to a to-do list
- Checking tasks from a to-do list
- Removing tasks from the to-do lists

Since it is a collaborative to-do list, the API should also support:

- Inviting new members
- Coupling one or more members to a certain task
- Showing the members attached to a task
- Removing members from a certain task

### Question
Can you deduce any non-functional requirement from the information above?

### Answer
Not really. It is clear that it is a collaborative to-do app, but it is not clear how many concurrent members the app should support. It is further clear that the API should be well described for our collegue developers, but nothing is mentioned about the code base itself. Are we expected to document our code? Etcetera.

## Conclusion
In this lesson we have deduced some basic requirements from endpoint only. It is your task to reverse engineer all requirements from the CargoHub code base. To help you document your reseach we end with some structure, tips and tricks.