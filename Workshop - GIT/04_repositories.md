

## GitHub
But, wait. There’s more. What about this distributed sharing thing with
Git ?

To be able to share, we’ll need a server to host our git repositiories.
GitHub (<a href="https://github.com/">github.com</a>) is probably the
easiest place to begin with.

## Login or sign up with GitHub

If you've already got an account you can skip on to creating the repo on
github, or forking this repository and cloning it down to your local machine.

Otherwise...

Go <a href="https://github.com/signup">sign up for an account</a> at
GitHub; Or login into your GitHub account if you had previously signed
up.

Hint: You may need to setup git cache your GitHub password - see
<a href="https://help.github.com/articles/set-up-git">https://help.github.com/articles/set-up-git</a>

Then come back here, we’ll wait.

## Create your first GitHub repository

A repository (repo) is a place where you would store your code. You were
practising on your very own repo just now!

The following <a href="https://help.github.com/articles/create-a-repo">
tutorial</a> will show you how to create a GitHub repo - which you can
then share with others

Then come back here, we’ll wait.

## Pushing your local changes

We have been working on our local branch for now, but what if we want to work further on another location and we forgot our machine? This is where remote repo's like GitHub come in handy.

Within our local branch we can use `git push` to push commits made on our local branch to a remote repository.

To push changes from our `main` branch to the remote `origin` we use

    $ git push origin main

this will push our latest commit to the remote repository so the local changes are reflected on the remote.

:no_mouth: Stuck? <br>
Ask for help from the teacher


## Pulling the latest remote version

When we working with a remote repository we used `clone` in a previous part to get the complete remote branch as a fresh new repository to our local machine. This works fine for the first time, but we don't always want a fresh version... we want to get the latest changes.

#### Fetching changes from a remote repository
Use `git fetch` to retrieve new work done by other people. Fetching from a repository grabs all the new remote-tracking branches and tags without merging those changes into your own branches.

If you already have a local repository with a remote URL set up for the desired project, you can grab all the new information by using `git fetch *remotename*` in the terminal:

    $ git fetch origin

##### :bulb: Setting up remote url

If we haven't cloned the repository via `git clone` we need to setup a remote url first.
You can check if this the case via

    $ git remote -v

    # Verify new remote
    > origin  https://github.com/OWNER/REPOSITORY.git (fetch)
    > origin  https://github.com/OWNER/REPOSITORY.git (push)

If there is no remote on your current local branch, you can add it via

    $ git remote add origin <repository-url>

:expressionless: Stuck? <br>
Ask for help from the teacher

### Merging changes into your local branch

Merging combines your local changes with changes made by others.

Typically, you'd merge a remote-tracking branch (i.e., a branch fetched from a remote repository) with your local branch:

    $ git merge origin/main
    # will merge the remote origin into local main

:neutral_face: Stuck? <br>
Ask for help from the teacher

### Pulling changes from a remote repository

`git pull`` is a convenient shortcut for completing both `git fetch` and `git merge` in the same command:

    $ git pull origin main
    # Grabs online updates and merges them with your local work

Because pull performs a merge on the retrieved changes, you should ensure that your local work is committed before running the pull command. If you run into a merge conflict you cannot resolve, or if you decide to quit the merge, you can use `git merge --abort` to take the branch back to where it was in before you pulled.

:anguished: Stuck? <br>
Ask for help from the teacher

## :tada: Great job!

You have learnt:

1.  Forking a repo at GitHub
2.  Git push
3.  Git fetch
4.  Git pull