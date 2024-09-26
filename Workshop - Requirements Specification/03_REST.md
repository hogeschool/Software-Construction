# Understanding REST
In the previous chapter we did already mention prefetching income details from the Belastingdienst API. There are multiple ways to implement such an Application Programming Interface (API in short) and one of them is REST (REpresentational State Transfer). To better understand REST, we first introduce the concept of an API and look at an alternative implementation.

## Application Programming Interfaces (APIs)
Suppose we need to build a forum discussion platform. The forum can be accessed via the browser, and we want to make it available via a native mobile app. It is further required that the discussions and responses are synchronized between the browser and mobile app.

Because of the synchronisation requirement, it is better to store the account and all its data in one central place and let the app and browser interface with it. The standard way to solve this is to store the account and corresponding data on a remote server and expose access to it via an HTTP API.

## HTTP communication
The Hypertext Transfer Protocol (HTTP) is the magic behind the whole internet and is used in nearly all client-server situations. The details of the Hypertext Transfer Protocol will be covered in the WebDev course, but to better understand this lesson we should know that HTTP messages -the messages sent back and forth between the clients and the server- consist of two parts: a header and a body.

### Example: image upload
If we want to update our profile picture we can send the following message:

### Message Header
The header describes how the server must interpret the sent message, for example:

```
PUT /profile/picture HTTP/1.1
HOST: forum.com
Connection: keep-alive
Content-Type: text/plain
Content-Length: 852
```

It says: you can expect 852 bytes of text data and the logic behind /profile/picture should to do something with the picture. Look at the CargoHub code base to see how this logic is technically implemented.

### Message Body
The body contains the data we want to send to the server, here a base64-encoded image:

```
iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBIWXMAAAsTAAALEwEAmpwYAAACL0lEQVR4nO2WTUtUURjHf+CkRIONe9tlI0T05svGPkMa2Hdob7qPyFpFg5AbX76Dm3KaoIXkBxDLpaDuUswog2aUB/4XHgY8c87lSgj+4cCdO8/zP+c+b/8Dl7hgqAIzwCfgG/BLy57rwDRw6zw2HgIawEnksgM+LGLjK8Ac0BLxD2ABeKxoXNOy53FgEdiXrfnUgFLezfuAzyL7DbwEeiP8rgOv5JNFo5Lnyxsi2AWGc3zAPWBbHF+A7hTnOTnuAP3kR784jOtdSsG1FMIiCsmi9wdoAg9iHBo6seW8KLwWp7VqEFVX7VZMRaHiumMgZDgjI2u1rBifAWvAgdaa3tl/JNgtift56AB1GVmfGyYDw8b+I8FuQr9XQwfYkpEfpy+Ap5oLfXq2d+3oZJel93voAEcyKlM8yuK2Pc7Ez3M8QK+4D1NTUBQGxW3K2bEIxykeT8T9MWQ0LSNTNY9HwFfgbuTkW5ePx7K4p0LOVRnttw2imhOmkYC/je492ZqPH0QHMYMIyeeJJDVDD/BB74+BeWAUuKo1BrwH/rpeN58Mb2LC77+iJQExYcrQpZneDAydf1I9L70jToxMoqNQC8jxHcn1phTT1oY2vt1me0NpM663JKDkUtEp72fhvruQ1PNczSruEBbC2cirVUU5P3b1kHwly1BSaJuuO5YkLIOamGU9T6jVsmpvKuy5L6UeltuVhGt5Pfb2k4oB6fmqRuqR1qZazIbMzWTWS/AfcQoFNst85lXcugAAAABJRU5ErkJggg==
```

If you are curious about this picture: try to base64 decode it!

But before we can upload stuff we first need to get access the our profile.

### Activity
To get access to our profile we need to authenticate ourselves. Let's have a look at how our hogeschool Rotteram does this. Assuming we use the Chrome browser:

1. Go to login.hr.nl
2. Open the developers tool (use the `F12` key)
3. Open the Network tab
4. Insert your credentials
5. Press the Login button
6. View the Header and Payload tab for /login

### Observations
On the Header tab we see that:

- The login page calls the url `https://login.hr.nl/v1/login`
- The request method is `POST` and the status code is `200 OK`

On the Payload tab we see that:

- The credentials are encoded via Form Data (key-value pairs)

So the login is implemented by calling the `/v1/login` endpoint of the HR-server, where the credentials are send along in the body. The server will respond by setting a authentication cookie and saying '200 OK'. You will learn more about this process during the WebDev course.

Because we call an endpoint with a verb in it ('login'), we know that this is not a REST-based request; we're calling a function so it's a Remote Procedure call (RPC), where calling the login-function results in setting a authentication cookie.

In the CargoHub code you'll find how you would implement the authentication process in REST. But what ís REST?

## What is REST?
Where RPC is designed around the idea of *calling functions*, REST is designed around the idea of *querying resources*. These resources are usually derived from the entities in our data model. So you can use the endpoints to reverse engineer the data model.

### Resources and URIs
A server often exposes multiple resources. For a online store we may want to view orders and fetch items, for example. Each of these resources is mapped onto a URL:

- **Orders**: `https://api.store.com/v1/orders`
- **Items**: `https://api.store.com/v1/items`

You can also query single items from a resource:

- **Order**: `https://api.store.com/v1/orders/{order_id}`
- **Item**: `https://api.store.com/v1/items/{item_id}`

REST uses Uniform Resource Identifiers (URIs) to expose the internal resources via a web server. Here the URI is the whole URL: the domain and subdomain part (`https://api.store.com`) plus the resource (`orders` or `items`).

> With this knowledge you should already be able to read off the endpoints of the CargoHub API.

#### Question
What URL would you expect for fetching accounts? And for prices?

#### Answer
The resource would be 'accounts' so `https://api.store.com/v1/accounts`. Mind the plural form. Similarly for prices. Note that 'prices' is probably not an entity within the data model, but it can be queried as a resource.

If you wonder what the difference is between URIs and URLs: URIs are more general than URLs and can used in file system and network paths, whereas URLs are the path description of the HTTP protocol. See the links in the resources for more details.

> Sometimes you see `https://store.com/api/v1` instead of the subdomain `https://api.store.com/v1`. That's a matter of taste or depends on the technical implementation. It is further common to add a version number to our api to help us with its maintainability. This may become clear during this course.

### Naming resources
We have already seen than REST does not use verbs to access a resource. So to fetch the items of a store, we cannot use the URL `https://api.store.com/fetch-items`. Instead, we use the GET method of the HTTP protocol to encode the fetch action.

### Question
Suppose we want to fetch the items of the store. How would we do that?

### Answer
To fetch the items, we combine the HTTP GET method with our URL:

`GET https://api.store.com/v1/items`

The resource here is `items` (note the plural form) and the fetch operation is represented by the `GET` method.

### Question
How do we tell the server about the URL and the `GET` method?

### Answer
These instructions are set in the header of the HTTP message.

Since we query a resource, the server responds by sending the queried resource over the line. The server responds with a HTTP message header telling the browser how to interpret the response. It could send

```
HTTP/1.1 200 OK
Server: Apache
Content-Type: application/xml
Content-Length: 223
```

with a body containing the XML response:

```
<items>
    <item>
        <id>1</id>
        <name>Rubber Duck</name>
        <price>12.99</price>
    </item>
    <item>
        <id>2</id>
        <name>Stress Ball</name>
        <price>8.99</price>
    </item>
</items>
```

### Activity
Can you translate the XML response into JSON?

### Answer
A possible, compact solution would be:

```
[
    {
        "id": 1,
        "name": "Rubber Duck",
        "price": 12.99
    },
    {
        "id": 2,
        "name": "Stress Ball",
        "price": 8.99
    }
]
```

There is no standard for the response representation in REST, but it common to send a response via JSON. We are then referring to 'JSON over REST'.

## RESTful operations
We have already seen that we can map a fetch operation on the HTTP GET method. We can extend this by mapping the standard Create, Read, Update and Delete (CRUD) data operations onto the following HTTP methods:

### GET: Retrieve information from the server
GET is *idempotent*. This means that you can make this call infinite times, and it will not make changes.

### POST: Create a piece of new information
POST is not idempotent because it creates a new resource. Calling it more often will create more resources.

### PUT: Update a piece of existing information
PUT is idempotent; it updates the same record with the same data.

### DELETE: Remove a piece of information
DELETE is not idempotent because it removes a record.

### Question
Given the HTTP methods, how would we update an item of the store with REST?

### Answer
First note that the update operation is mapped onto the HTTP PUT method. The tricky part is how to encode which item we need to update and with what data. Here is how we encode the update in REST terms:

`PUT https://api.store.com/v1/items/1`

and send along the updated item in the body of the request:

```
{
    "id": 1,
    "name": "Rubber Duck",
    "price": 21.99
}
```

Note that we pass the identifier of the item we want to update in the URI. So the general URI for updates is `https://api.store.com/v1/items/{item_id}`.

### Payload heavy-ness
Through the design of the URI for updates you can see why REST is payload heavy: before you can update an item, you first need to know its identifier. And to know this identifier, you need to fetch *all* items. This is not a problem for 10 items, but you might have 10,000 items... which translates in a huge payload.

> With REST APIs you often need multiple roundtrips to perform a single action. More on this later.

## Status codes
To indicate if an operation was succesful, the HTTP protocol adds a status code to the response. Responses are grouped into five classes:

- **Informational responses**: 100 – 199
- **Successful responses**: 200 – 299
- **Redirection messages**: 300 – 399
- **Client error responses**: 400 – 499
- **Server error responses**: 500 – 599

### Activity
Using the [Mozilla documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status), which status code is send when:

- A resource cannot be found
- You are not allowed to access a resource
- Something goes wrong on the server
- A resource is created

### Answers
We expect the status codes:

- 404 Not Found
- 403 Forbidden
- 500 Internal Server Error
- 201 Created

Take a look at the CargoHub API and see if you recognize these code. They also give you a hint of what the code does.

## Stateless-ness
Last, but not least: REST is designed around the idea of being stateless. This means that a RESTful web server:

- Does not remember any previous action
- Does not store any session data, e.g. for authentication

So each request acts as a fresh request, and all necessary information must be send along with each request by the client. This is a second reason why REST may be payload heavy.

The upside is that RESTful APIs are far more flexible and less complex than statefull APIs: with a single Access Key you can query multiple servers with multiple resources all over the world. For this reason big companies like Facebook and Google use REST for most of their services.

But enough theory, time for some interaction with a real RESTful API.

### Activity
There are multiple ways to interact with an API: we could use the terminal with cURL, but for simplicity we are going to use Hoppscotch, an Open Source version of the well-known Postman tool.

To start go to [hoppscotch.io](https://hoppscotch.io). The user interface elements should remind you of the browser dev view at the beginning of this chapter:

- The default url is the endpoint of the API
- Below the endpoint we find the body and header of the request
- Below that we see the response, the status code and the time it took

We are going to query the RESTful API described on [this site](jsonplaceholder.typicode.com).

1. Open the site and look for the resources and the routes (the URIs for these resources)
2. In the Hoppscotch UI, change the default `https://echo.hoppscotch.io` to the endpoint `https://jsonplaceholder.typicode.com`

Now answer the following questions:

3. What's the name of the user that wrote the post with id = 12?
4. What's the title of the second comment on post with id = 2?
5. How many albums does user with id = 8 have?

### Answers
(3) To know the name of the user that wrote post 12:

- You first have to fetch all posts via the `/posts` endpoint
- We then search for the post with id: 12 and look for the userId
- Finally we fetch all users with the `/users` endpoint
- We lookup user with id: 2 and find the name Ervin Howell

Here you see that a RESTful API requires multiple requests (with potentially lots of data) to extract only a name.

(4) To know the title of the 2nd comment on post 2:

- Fetch all comments via the `/comments` endpoint
- Search for the comments with postId: 2
- Filter the comments, chose the 2nd comment and find the title "repellat consequatur praesentium vel minus molestias voluptatum"

Here you see that the client (you in this case) needs to do all the searching and filtering. RESTful API therefore add query parameters to do this for you:

If you did not yet do this, try using the endpoint: `/comments?postId=2`. Now you only have to lookup the second entry. This makes the payload burden less heavy.

(5) To know the number of albums for user 8:

- Directly fetch the filtered list from the endpoint `/albums?userId=8`
- Now count the number of results to find 10 albums for user 8

## Conclusion
You now know what RESTful APIs are, that they are used in many places and that they have their pros and cons. With this knowlegde you should be able to reverse engineer the CargoHub API. Next we discuss how you can extract its underlying requirements, such that you can document those.