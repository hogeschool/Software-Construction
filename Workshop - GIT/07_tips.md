## :rocket: Best Practices and Tips

Using Git best practices, teams can coordinate all changes in a software project and utilize fast branching to help teams quickly collaborate and share feedback, leading to immediate, actionable changes.

### Make incremental, small changes

Write the smallest amount of code possible to solve a problem. After identifying a problem or enhancement, the best way to try something new and untested is to divide the update into small batches of value that can easily and rapidly be tested with the end user to prove the validity of the proposed solution and to roll back in case it doesn't work without deprecating the whole new functionality.

Committing code in small batches decreases the likelihood of integration conflicts, because the longer a branch lives separated from the main branch or codeline, the longer other developers are merging changes to the main branch, so integration conflicts will likely arise when merging. Frequent, small commits solves this problem. Incremental changes also help team members easily revert if merge conflicts happen, especially when those changes have been properly documented in the form of descriptive commit messages.

### Keep commits atomic

Related to making small changes, atomic commits are a single unit of work, involving only one task or one fix (e.g. upgrade, bug fix, refactor). Atomic commits make code reviews faster and reverts easier, since they can be applied or reverted without any unintended side effects.

The goal of atomic commits isn't to create hundreds of commits but to group commits by context. For example, if a developer needs to refactor code and add a new feature, she would create two separate commits rather than create a monolithic commit which includes changes with different purposes.

### Develop using branches

Using branches, software development teams can make changes without affecting the main codeline. The running history of changes are tracked in a branch, and when the code is ready, it's merged into the main branch.

Branching organizes development and separates work in progress from stable, tested code in the main branch. Developing in branches ensures that bugs and vulnerabilities don't work their way into the source code and impact users, since testing and finding those in a branch is easier.

### Write descriptive commit messages

Descriptive commit messages are as important as a change itself. Write descriptive commit messages starting with a verb in present tense in imperative mood to indicate the purpose of each commit in a clear and concise manner. Each commit should only have a single purpose explained in detail in the commit message. The Git documentation provides guidance on how to write descriptive commit messages:

    Describe your changes in imperative mood, e.g. “make xyzzy do frotz” instead of “[This patch] makes xyzzy do frotz” or “[I] changed xyzzy to do frotz,” as if you are giving orders to the codebase to change its behavior. Try to make sure your explanation can be understood without external resources. Instead of giving a URL to a mailing list archive, summarize the relevant points of the discussion.

Writing commit messages in this way forces software teams to understand the value an add or fix makes to the existing code line. If teams find it impossible to find the value and describe it, then it might be worth reassessing the motivations behind the commit. There's always time to commit later, as long changes are stashed and there's consistency in commits.

### Obtain feedback through code reviews

Requesting feedback from others is an excellent way to ensure code quality. Code reviews are an effective method to identify whether a proposal solves a problem in the most effective way possible. Asking individuals from other teams to review code is important, because some areas of the code base might include specific domain knowledge or even security implications beyond the individual contributor's attributions.

### Identify a branching strategy

Determining a single branching strategy is the solution to a chaotic development experience.

While there are several approaches to development, the most common are:
- Centralized workflow: Teams use only a single repository and commit directly to the main branch.
- Feature branching: Teams use a new branch for each feature and don't commit directly to the main branch.
- GitFlow: An extreme version of feature branching in which development occurs on the develop branch, moves to a release branch, and merges into the main branch.
- Personal branching: Similar to feature branching, but rather than develop on a branch per feature, it's per developer. Every user merges to the main branch when they complete their work.