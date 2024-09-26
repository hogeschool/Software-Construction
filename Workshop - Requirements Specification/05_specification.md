# Requirements Specification
You are expected to document a lot during this project. We therefore end this series with the do's and don't of writing down requirements, and with some tips for writing good documentation in general.

## Specifying requirements
It is your task to write down good requirements.

### Activity
What do you think of the following requirements?

1. Users must be able to share to-do lists
2. The app should be fast and secure
3. Implement notifications

### Possible Answer
1. Users must be able to share to-do lists:

This requirement is too vague. It doesn't specify how users will share the lists, with whom they can share them, or any permissions and access control details.

2. The app should be fast and secure

This is a non-specific requirement. "Fast" and "secure" are subjective terms and need clear definitions and measurable criteria.

3. Implement notification

This lacks detail about the types of notifications (e.g., email, push notifications), what triggers them, and the customization options available to users.

## Good requirements
Writing bad requirements is easy: just jot down the first thing that comes to mind. Good writing requires **attention** and **structure**. To help you write down good requirements here are some guiding principles:

### Properties

#### Clear and Unambiguous
Each requirement should be stated in a way that it can only be interpreted in one way. Avoid vague language and ensure that the requirement is easily understandable.

#### Specific
The requirement should be detailed enough to provide a clear understanding of what is needed. It should describe the functionality, constraints, and expected outcomes precisely.

#### Measurable
Requirements should be quantifiable so that they can be tested and verified. This includes specifying metrics for performance, accuracy, and other relevant criteria.

#### Achievable
The requirement should be realistic and feasible within the given constraints, such as time, budget, and technology.

#### Relevant
Each requirement should be directly related to the project’s goals and objectives. It should contribute to the overall purpose of the system.

#### Complete
The requirement should include all necessary information, covering all aspects needed to implement the feature or functionality.

#### Consistent
Requirements should not conflict with other requirements. Consistency ensures that all requirements can coexist without contradiction.

#### Verifiable
It should be possible to verify each requirement through testing, inspection, or other verification methods to ensure that it has been implemented correctly.

#### Traceable
Each requirement should be traceable back to its origin, whether it’s a stakeholder need, a business objective, or a higher-level system requirement. This helps in managing changes and understanding the impact of modifications.

## Activity
- Read the scenario below and the sample poorly formulated requirement
- Rewrite the requirement to meet the properties of good requirements
- Explain how your rewritten requirement satisfies each property of a good requirement

### Scenario
You are part of a team developing a collaborative to-do app. One feature needed is the ability for users to share to-do lists with others. A poorly formulated requirement for this feature might be: "Users must be able to share to-do lists."

### Task
Rewrite the above requirement considering the properties of good requirements. After rewriting the requirement, provide a brief explanation for how your requirement satisfies each property.

### Possible Answer
Rewritten Requirement:

"Users must be able to share to-do lists with other registered users by entering their email addresses. Shared users should have the ability to view, edit, and complete tasks on the shared list. Notifications must be sent to shared users when a list is shared with them, and the owner of the list should be able to revoke access at any time. The sharing functionality must be accessible within the to-do list interface and must respond within 2 seconds after the share button is clicked."

**Clear and Unambiguous:** The requirement specifies that sharing is done by entering email addresses and that only registered users can be shared with. It also clarifies the permissions shared users will have.

**Specific:** It details what actions shared users can perform (view, edit, complete tasks) and how notifications and revoking access should work.

**Measurable:** The response time of 2 seconds for the sharing functionality is a quantifiable metric.

**Achievable:** Assuming current technology and resources, this requirement is realistic and feasible.

**Relevant:** Sharing to-do lists is directly related to the collaborative nature of the app.

**Complete:** It covers all necessary aspects of the sharing functionality, including permissions, notifications, and access control.

**Consistent:** There are no conflicting elements within the requirement or with other potential requirements.

**Verifiable:** The requirement can be tested through functional testing (e.g., sharing a list, editing tasks) and performance testing (response time).

**Traceable:** This requirement can be traced back to the need for collaborative features in the app.

## Tip
Look for good examples and guiding principles to help you with writing. Approach it like programming: "code" with words and sentences to bring your message across. Like with programming: you need to design you message so do some sketching, refining and even testing; test if your message can be decoded by others.

# Summary
Good writing is a work of art; it takes time and effort. If you don't like writing: really do practice and remember that you don't write for yourself. You write because you provide clarity to your team and to all the other stakeholders in your project.