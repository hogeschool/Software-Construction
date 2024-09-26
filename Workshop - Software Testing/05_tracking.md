# Tracking with GitHub

When it comes to bug tracking, GitHub provides an easy-to-implement yet powerful way to manage issues related to a code project.

<br>

## GitHub Issue Tracker
GitHub has a built-in issue tracking system that allows you to log and manage issues directly within your repository. [More info about issue tracking](https://docs.github.com/en/issues/tracking-your-work-with-issues/planning-and-tracking-work-for-your-team-or-project) 

1. **Creating Issues**: You can create new issues by navigating to the `Issues` tab in your repository. Click on the `New Issue` button, and provide details about the issue, including a title, description, and labels (such as “bug,” “enhancement,” etc.).
2. **Issue Details**: Each issue has a dedicated page where you can discuss the problem, provide additional context, and collaborate with other team members. You can also assign the issue to specific individuals.
3. **Labels and Milestones**: GitHub allows you to categorize issues using labels. For example, you can label an issue as “bug,” “feature request,” or “documentation.” Additionally, you can set milestones to track progress toward specific goals.
4. **Comments and Discussions**: Team members can comment on issues, discuss potential solutions, and provide updates. GitHub’s notification system ensures that relevant parties stay informed.
5. **Closing Issues**: Once an issue is resolved, you can close it. GitHub provides options to reference related pull requests, link to commits, and mark the issue as resolved.

<br>

## Branching

Branches allow you to develop features, fix bugs, or safely experiment with new ideas in a contained area of your repository. When you create a branch, you’re essentially creating a separate copy of your codebase where you can work independently without affecting the main codebase. Each branch represents a specific task or feature. 
[More info about creating a branch in GitHub](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-a-branch-for-an-issue)

### Why branch?
1. **Isolation**: By creating a branch, you isolate your changes from the main codebase. This prevents accidental interference with other ongoing work.
2. **Collaboration**: Branches facilitate collaboration. Multiple team members can work on different branches simultaneously, and then merge their changes back into the main branch.
3. **Feature Development**: You can create feature branches to work on specific features or enhancements. Once the feature is complete, you merge it back into the main branch.
4. **Bug Fixes**: Branches are useful for fixing bugs. You create a branch, make the necessary fixes, and then merge it back.
5. **Experimentation**: If you want to try out a new idea without affecting the main code, create an experimental branch.

### Best practices
Here are some best practies you could follow when creating branches. <br>

**Create from the Default Branch**<br>
Typically, you create a new branch from the default branch (often named “main” or “master”). This ensures your branch starts with the latest code.

**Descriptive Names**<br>
Give your branches descriptive names (e.g., “feature/user-authentication” or “bugfix/404-page”). Clear names make it easier to understand the purpose of each branch.

**Regularly Merge**<br>
Regularly merge changes from the default branch into your feature branch to keep it up-to-date.

**Pull Requests**<br>
Use pull requests to propose merging your branch into the default branch. This allows for code review and discussion before merging.

**Delete Stale Branches**<br>
After merging, delete branches that are no longer needed to keep your repository tidy

> :bulb: **Remember** that every project is different, but it is always necessary to make good agreements about how you formulate things like Issues and Branches and how to deal with Bugs or new Features. [More info about flows](https://docs.github.com/en/get-started/using-github/github-flow)

<br>

## Classification

Now, let’s discuss the defect life cycle and severity/priority classification:

### Defect Life Cycle: 
The defect life cycle encompasses various stages, including identification, logging, assignment, fixing, retesting, and closure. Each stage plays a crucial role in managing defects effectively.

- **Identification**: Detecting defects during testing.
- **Logging**: Creating detailed bug reports.
- **Assignment**: Assigning the issue to the relevant team member.
- **Fixing**: Developers address the issue.
- **Retesting**: Verifying that the fix works.
- **Closure**: Marking the defect as resolved.

### Severity and Priority Classification:
#### Severity 
Refers to the impact of a defect on the system. It can be categorized as critical, major, minor, or trivial.
- **Critical**: The defect causes system failure or data loss.
- **Major**: Significant functionality is affected.
- **Minor**: Minor functionality issues.
- **Trivial**: Cosmetic issues with minimal impact.

#### Priority
Indicates the order in which defects should be addressed. Prioritization depends on business needs, user impact, and project timelines.
- **High Priority**: Requires immediate attention.
- **Medium Priority**: Important but not urgent.
- **Low Priority**: Can be addressed later.