# Version Control Integration

We've talked about branching in an earlier workshop (GIT), let's see how these branches can help us by integrating them in a CI/CD pipeline. There are multiple branching strategies available each with the goal to solve that problem and to enable teams to work together on the same source code. A well-defined branching strategy ensures consistent processes for making changes to source control within a team. The right approach fosters collaboration, efficiency, and accuracy in the software delivery process, while an inadequate strategy (or lack thereof) can result in wasted time.

## Types of branches
To understand what branch strategy we should use, we first have to understand what types of branches there are.

### Trunk Branches
In every Git repository, there exists a trunk (also known as main, mainline, or the master branch). When a Git repository is initially created, the trunk is automatically established as the implicit first branch. The role of the trunk and the timing of changes merged into it depend on the specific branching strategy employed. 

##### Advantages
- truly Continuous Integrations
- small changes
- feature flags
- branch by abstraction

##### Disadvantages
- contention collision
- more complex
- desired High team maturity
- strong automation
- test a lot before push

<br>

### Development branch
The development branch serves as a persistent feature branch where developers make changes before they’re ready for production. Unlike the trunk, it remains intact and is never deleted. In certain cases, the development branch aligns with a non-production environment, and commits to it trigger deployments to the test environment. 

![Development branch](assets/images/01%20How%20it%20works.svg)
*Source: https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow*

##### Advantages
- usually ensures a clean state of branches at any given moment in the life cycle of the project
- branch development is totally separated from the production ( main branch )
- the main branch is always or almost ready for release
- the branches naming follows a systematic pattern making it easier to comprehend
- gitflow offers a dedicated channel for hotfixes to production.

##### Disadvantages
- Many branches can become difficult to manage
- features can take days to merge because a lot of changes are committed to the development branch without being integrated, tested previously.
- long-lived branches is a large maintenance headache for a team
- complex work process complexity
- slow feedback
- heavy branch overhead

<br>

### Feature Branches
Depending on the branching strategy, a feature branch can have either a short or long lifespan. Typically, it serves as a workspace for individual developers to make changes specific to their work, but it can also be shared among multiple developers. 
Developers create separate branches for specific features or bug fixes, this isolates changes related to a particular task.
These changes are then merged back into the main branch (e.g., main or master) when the feature is complete.

![Feature branches](assets/images/02%20Feature%20branches.svg)
*Source: https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow*

##### Advantages
- lightweight workflow
- work well with CI/CD
- small teams can build, test and deploy features fast
- developers lead on small sets of changes instead of the entire release
- simple work process complexity
- each team or sub-team could maintain their own branch for development
- light branch overhead
- fast feedback
- clean History

##### Disadvantages
- the merge to the main branch needs to be done carefully because of - the risk of being unstable.
- as your teams grow, this model can cause costly merge conflicts
- as have many branches the complexity is growing

<br>

### Release Branches
Created for preparing a new release.
Stabilizes the code, fixes critical bugs.
Merged into both the main branch and other active feature branches.

![Release branches](assets/images/03%20Release%20branches.svg)
*Source: https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow*

##### Advantages
- Required for teams that support multiple version
- Every release is perfectly traceable
- The team can work independently on every release
- The development of a release is very neat and respectful of all good practices of software development

##### Disadvantages
- usually no automation
- no continuous anything
- usually associated with low-frequency deployment
- communication between the team is complex
- merge is complicated

<br>

### Hotfix Branches
Created to fix critical issues in production.
Based on the main branch.
Merged back into the main branch and release branches.

![Hotfix branches](assets/images/04%20Hotfix%20branches.svg)
*Source: https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow*

<br>

## Git Integration with CI/CD Pipelines
Developers commit code changes to the VCS (e.g., Git).
CI server (e.g., GitHub Actions, Jenkins, GitLab CI/CD) detects changes and triggers a build.
Automated tests (unit, integration) run.
If tests pass, artifacts are generated.
CD pipeline picks up the artifacts for deployment.

### Integration Points:
- Hooks: Git hooks (pre-commit, post-receive) trigger actions (e.g., running tests) during commits or pushes.
- Webhooks: Notify CI/CD systems about new commits or PRs.
- Pipeline Configuration: CI/CD tools are configured to listen to specific branches or events.
- Artifact Management: Store build artifacts in repositories (e.g., Nexus, Artifactory).