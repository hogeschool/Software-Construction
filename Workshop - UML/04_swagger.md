# API documentation
In the introduction we were discussing how to describe the communication between NASA's Mission Control and the Voyager probes. We made a start with a Sequence diagram and a Class diagram to describe their communication, but it was not ideal. If we were to use UML for the Mission Control - Voyager interface then it would result in a lot of diagrams without a clear overview. That's why tools like Swagger were invented.

## What is Swagger?
Swagger is a way to document your REST API in a **standardized** way. The best way to explore what Swagger really is, is to view Swagger's Petstore example:

[Swagger Petstore API](https://petstore.swagger.io)

## Things to explore

### The general description
On top we find a title and a description. You have some freedom here and it is up to you to give a clear description of your API.

### Endpoints
Swagger allows you to organize CRUD actions per endpoint. Here we see GET, POST, PUT and DELETE actions for the endpoints **pet**, **store** and **user**.

### Requests
The request part describes the request and its response in details. Expanding the pet's PUT we find:

- The body and that this field is required
- The model that we must send and an example
- When you run `execute` we see the response

### Models
The model descriptions are extracted from the endpoint models.

Anything that is relevant for developers is present in the documentation. Now it's time to build your own Swagger doc.

### Activity
Suppose your company needs to build a basic calculator. It should handle:

- Additions
- Subtractions
- Multiplications
- Divisions

One of the requirements is that the calculator must be available for mobile, desktop and web. Your company decides not to build the mobile, desktop and web client itself; they leave that to other vendors. But they do provide the calculator API. The code base is provided to you, see `app.py`.

It's your task to let the other developers know how to use the API:

- Describe the API with Swagger
- You can use the json or yaml variant for this
- Use the [Swagger specification](https://swagger.io/specification) in combination with [Swagger Petstore](https://petstore.swagger.io) example

Present your documentation by loading your json/yaml file into [Swagger's online Editor](https://editor.swagger.io).

Like the Petstore example, Swagger documentation can be made interactive but that is beyond the scope of this workshop. See the resources for a tutorial.