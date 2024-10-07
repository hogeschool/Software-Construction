# Hands-On Code Refactoring

## Code gets "dirty"
It's the programmer's task to ship features. Once finished with the current feature we move on to the next and the next. But as a project progresses entropy kicks in. This means that code becomes harder to read and to maintain. As a result bugs creep in, the performance goes down and our feature velocity grinds to a halt.

Code gets "dirty" because of

- Inexperience
- Hard deadlines
- Shortcuts
- Unknowns

Another word for "dirty code" is "technical debt" and it's our task to fight it proactively during the development process by refactoring our code.

## What is code refactoring?
Refactoring means (re)organizing your code **without modifying its original functionality**. Refactoring is the process of making **small** changes or adjustments to your code without affecting or changing how the code functions while in use.

## Benefits of refactoring

### It helps improve structure and coherence
Refactoring helps you **improve the design** of your software. Developing applications is a difficult task. As you add additional functions, the relevance of your design may be affected. Then, abstractions are no longer as pure as they once were.

#### Example

> We started with a `Bird` class which contains a `fly()` method. From it we derived the `Swan`, `Eagle` and the `Dove` type. All works fine, but then a `Pinguin` enters the scence, followed by a `Kiwi` and an `Ostrich`. So the `fly()` method needs to moved to adjust for the latter type of birds. It's a general rule that we will encounter stuff we did not account for.

You can improve the structure and coherence of your programs by refactoring your code **regularly**.

### It gives a better understanding of the code
If you refactor properly, your code will be more easily understandable afterwards. Your code will also be easier to understand by improving the design.

#### Example

> If you find pieces of code where you need to do a lot of "pointer chasing" it is generally a good idea to refactor the code. Same is true for a lot of functions calling each other to model simple functionality. Chasing functions and pointers makes your code hard to understand.

It is common knowledge that developers read code far more frequently than they write it. As a result, it's in your best interest to keep things as simple as possible, which considerably improves maintainability. Also, people who read it in the future will be grateful.

### Refactoring broadens your knowledge
Finally, refactoring is a method of **active learning**. Even if you didn't write the code, refactoring it gives you a better grasp of what it does. And by reading the code of your collegues you will learn other possible ways to write code and absorb good practices.

**Warning**
> It may be tempting to show-off your skills and impress your collegues by introducing "superstar code". Don't do that or you'll enter into an arms race and the readability of your code spirals out of control. Again: keep things as simple as possible.

## Quick discussion
Briefly share your experiences with refactoring during Project B.