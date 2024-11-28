# A need for diagrams
In this workshop we give a brief overview of the Unified Modeling Language (UML), why it is useful and with a focus on its applications. But let's start with a story.

## The Voyager probe
In the 1970s, NASA embarked on an ambitious mission to explore the outer planets of our solar system with the Voyager program. The twin spacecraft, Voyager 1 and Voyager 2, were designed to send back invaluable data about Jupiter, Saturn, Uranus, Neptune, and beyond. One of the critical aspects of the mission was ensuring reliable communication between the spacecraft and Earth across billions of miles. The engineers faced the challenge of designing a robust communication system that could handle the vast distances and extreme conditions of space.

Meanwhile the probes have left our solar system. Due to this distance the communication bandwidth with the probes has dropped to only **120 bits per second** and it takes **22 hours** to reach the them.

![NASA’s Voyager 1 soars through interstellar space 40 years after it was launched](https://cdn.mos.cms.futurecdn.net/iNJkfLq8evP5EcbGxvsqhi-1920-80.jpg)

The Voyager probes send out regular 'pings' but one day the NASA engineers started to receive scrambled rubbish... After restarting the Computer Command System (CSS) it became clear that one of the memory banks was damaged by the high energy particles. Now image that you are tasked to reprogram the CSS.

### Activity
What would be the first this you would do?

#### Answer
You would look for documentation describing the system.

So you reach for the documentation and find the following diagram:

![Block diagram for Voyager CCS](https://www.allaboutcircuits.com/uploads/articles/ccs_viking_voyager_blockdiagram_nasa.jpg)

Would this diagram be enough to apply your changes?

#### Learning 1
> Without knowing anything about the diagramming language used in the Block diagram, we were able to judge that it is not helpful for our purpose. So good diagram models are intuitive.

### Discussion time
What documentation would we need?

#### Possible answer
Since we need to communicate with the Voyager probe, we need a communication protocol. 

It should describe:

- What messages we can send
- What the system does with our messages
- Which response we get back

#### Example
When we lookup this protocol, we find the following description.

**Communication Protocol**

The communication takes place between two participants:

1. **Center Center** (referred to as "Center"): The communication control center.
2. **Voyager Probe** (referred to as "Voyager"): The Voyager space probe.

The communication between **Center** and **Voyager** takes the following sequence:

1. The **Center** initiates a connection to the **Voyager** by sending a "Connect" message.
2. The **Voyager** receives the connection request and acknowledges it by sending an "Acknowledge Connection" message back to the **Center**.
3. The **Center** sends data to the **Voyager** with a "Send Data" message.
4. The **Voyager** processes the received data internally (represented by "Process Data").
5. The **Voyager** acknowledges that the data has been received by sending an "Acknowledge Data Received" message to the **Center**.
6. The **Center** sends a "Disconnect" message to the **Voyager** to terminate the communication session.
7. The **Voyager** acknowledges the disconnection by sending an "Acknowledge Disconnection" message back to the **Center**.

#### Activity
What would this look like in a diagram?

#### Compare results
There are no wrong results here. Pick out some good ones and some unclear ones and discuss their clarity and expressiveness. The diagrams need to be useful.

#### Possible solution
The protocol could like something like:

![Protocol](./plant_uml/voyager_protocol/Voyager%20Communication%20Protocol.svg)

This protocol is based on the TCP protocol, but would this be handy for the Voyager communication? Why? For those interested, see the [TCP protocol](https://developer.mozilla.org/en-US/docs/Glossary/TCP) for more context.

#### Learning 2
> Diagrams are much easier to interpret than text. Expressing our documentation in diagrams therefore results in less interpretation errors (bugs) and faster implementation (development speed).

### Discussion time
We now know how both participants communicate, but we don't yet know what they are saying. Or, in other words: what messages they pass around.

- Do they have a header?
- Do they have a built-in integrity check?

#### Example
The message might be structured like:

![Message](./plant_uml/voyager_message/Voyager%20Message%20Description.svg)

#### Activity
What does this diagram say?

#### Possible solution
The `opcode` describes the instruction for the CSS to execute and the `checksum` is added to check that the message has not corrupted during its 22 hour flight. The diagram says that the message consists of a header and a body.

But this raises the question what the possible `opcode`s are. Hopefully this is documented as well... We will come back to this at the end of this workshop when we introduce Swagger documentation. This is documentation specifically designed for describing APIs.

## Conclusion
Diagrams make our developer life easier than textual descriptions.