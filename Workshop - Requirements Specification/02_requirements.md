# Different types of requirements
Requirements don't spring out of thin air; they are actively developed by multiple stakeholders, starting with "the business".

## Business requirements
Every project should start with a sound business case. This could be to solve a dire practical problem and make money for shareholders. Or, in the context of a government, it could be to simplify the tax declaration process and release the pressure on the support team.

Once the goal is defined, we must identify the contraints. We may have (1) a limited budget of 100.000 euro, (2) only one dedicated dev team at our disposal and (3) the law may demand that the tax declaration tool must be finished at the end of the year.

### Activity
Translate the three constraints above into requirements.

Hint: start with 'The solution...'

### Possible answer
- *We have a limited budget* translates into

**The solution needs to be implemented within a budget of 100.000 euro**

- *We have only one dedecated dev team* translates into

**The solution should be implementable by a single dev team**

- *The law demands that tool must be finished at the end of the year* becomes

**The solution must be delivered before 31 december 2024**

> Notice the *specificity* of these requirements: they are *clear* and *measurable*. It is therefore easy to verify whether we have satisfied them. Also notice the verbs *needs*, *should* and *must*. These signal the strictness or importance of the requirements.

## User requirements
It is in our interest to make the tax declaration tool as simple as possible. Else users would contact the support team, which goes against our business objective. So we require the user experience to be intuitive and self-explanatory.

### Question
Can you think of other user requirments for governmental software?

### Possible Answer
Since we are a governmental institution we are further required to make the software accessible to the visually impaired and (color) blind.

> Notice that we only specify what is required. We do not yet say how we are going to implement it. Remember that requirements are about what to build.

The user requirements describe the project from the user's perspective and they should be in line with the business goals. Users are an important stakeholder during the process.

## Functional software requirements
Given the context above, we can refine the requirements further to the software level.

### Question
Provided that the goal is to make tax declarations easier, how would you refine that 'the user experience must be intuitive and self-explanatory'? Or: what functionality would make the experience intuitive and self-explanarory?

### Possible answer
To make tax declarations easier, the system should fetch all known details up front. This could translate into the following functional requirements:

- The system should automatically lookup the user's employer
- Given the employer, the system should prefetch the income details from the Belastingdienst API
- The system should prefetch all savings details from the user's bank accounts
- The user interface should prefill the bank balances, gross income, ...
- The user interface should highlight the missing values that need to be filed
- The user interface should explain the meaning of the fields with an info marker

> Functional requirements translate the business and user requirements into more refined steps. They specify what the system needs to do in order to fullfill the requirements.

## Non-functional requirements
Knowing what the system needs to do is not enough, though. For example, the functional requirements don't tell us how many concurrent users the system must be able to handle. Or if code should be reusable. Or...

### Activity
Try to answer the following question:

- How many concurrent requests may we expect on the first tax declaration day? Estimate this based on these [CBS statistics](https://www.cbs.nl/nl-nl/visualisaties/dashboard-bevolking/bevolkingspiramide)

### Possible answer
It's about the estimation process here, not about the precise answer:

From the 17,951,000 Dutch citizens about 2 x 60 x 110,000 is 13,200,000 have to pay taxes: a factor 2 for male and female, 60 for the range between 20 and 80 years old and 125,000 as an average for each age. If all these users would declarate their taxes within an 8 hours time window then the system would need to handle 460 request per second. If we expect a one-hour peak in the morning and one in the evening then we receive 1,800 requests per seconds. Etcetera. Each scenario may require a different solution.

> Notice that we don't talk about specific solutions; we only discuss possible system load scenarios. Requirements do not include solutions / implementation details. These are described in design and technical documuments. Be aware of this while you write your requirement specification document.

### Functional or non-functional?
Think about the following requirements and mark them as 'functional' or 'non-functional':

- The system must allow users to log in using a username and password
- The system must be able to handle 10,000 concurrent users
- The system must be available 99.9% of the time, excluding scheduled maintenance periods
- User passwords shall be stored using strong hashing algorithms such as bcrypt
- The system must be maintainable by a single developer

### Answers
- Functional: access via login
- Non-functional: has to do with scalability and concurrency
- Non-functional: has to do with availability
- Non-functional: has to do with security
- Non-functional: has to do with maintainability

## Mind The Difference
Functional requirements describe *what the system must do*, non-functional requirements define the "ilities"

- Usability
- Maintainability
- Scalability
- Availability
- Deployablity
- Traceability
- Testability
- Stability
- Security
- ...

and

- Privacy
- Compliancy
- Concurrency
- ...

Indeed, there are a lot of non-functional demands but not all do apply to each project. Each stakeholder will bring in his or her non-functional demands. Try to relate each requirement to a stakeholder...

> You could say that the non-functional requirements define how the functional requirements need to be implemented & documented and which tools we need to choose. Without the non-functional requirements we are just "scripting away like an amateur", not engineering a solution. Engineering requires non-functional "ilities".

## Conclusion
Requirements start with a clear goal and are refined to be specific enough to design a proper solution.