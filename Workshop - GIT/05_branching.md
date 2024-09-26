Branching and Merging:

Discuss the concept of branches and their use cases.

Teach students how to create, switch, and merge branches.

Explain the difference between fast-forward and non-fast-forward merges.



## Branching

Most large code bases have at least two branches - a ‘live’ branch and a
‘development’ branch. The live branch is code which is OK to be deployed
on to a website, or downloaded by customers. The development branch
allows developers to work on features which might not be bug free. Only
once everyone is happy with the development branch would it be merged
with the live branch.

Creating a branch in Git is easy. The `git branch` command, when used by
itself, will list the branches you currently have

    $ git branch

The `*` should indicate the current branch you are on, which is
`main`.

If you wish to start another branch, use
`git checkout -b (new-branch-name)` :

    $ git checkout -b test-branch-1

Try git branch again to check which branch you are currently on:

    $ git branch
      test-branch-1
    * main

The new branch is now created. Now let’s work in that branch. To switch
to the new branch:

    $ git checkout test-branch-1

`git checkout (branch-name)` is used to switch branches.

Let’s perform some commits now,

    $ echo 'some content' > test.txt
    $ git add test.txt
    $ git commit -m "Added experimental txt"

Now, let’s compare them to the main branch. Use `git diff`

    $ git diff main

Basically what the above output says is that `test.txt` is present on
the `test-branch-1` branch, but is absent on the `main` branch.

:confused: Stuck? <br>
Ask for help from your teacher

## Now you see me, now you don’t

Git is good enough to handle your files when you switch between
branches. Switch back to the `main` branch

Try switching back to the main branch (Hint: It’s the same command we
used to switch to the test-branch-1 branch above)

Now, where’s our `test.txt` file ?

    $ ls
    README.md  processing.txt  tools.txt  git-changed-me.txt

As you can see the new file you created in the other branch has
disappeared. Not to worry, it is safely tucked away, and will re-appear
when you switch back to that branch.

Now, switch back to the test-branch-1 branch, and check that the `test.txt` is
now present.

:confused: Stuck? <br>
Ask for help from the teacher

## Merging

We now try out merging. Eventually you will want to merge two branches
together after the conclusion of work.\
`git merge` allows you to do that.

Git merging works by first switching the branch you want to *into*, and
then running the command to merge the other branch in.

We now want to merge our `test-branch-1` branch into `main`. First, switch to
the `main` branch.

    git checkout main

Next, we merge the `test-branch-1` branch into `main` :

    $ git merge test-branch-1

Do you see the following output ?

    Merge made by recursive.
     test.txt |    1 +
     1 files changed, 1 insertions(+), 0 deletions(-)
     create mode 100644 test.txt

You have to be in the branch you want merge *into* and then you always
specify the branch you want to merge.

At this point, you can also try out `gitk` to visualize the changes and
how the two branches have merged

## Merge Conflicts

Git is pretty good at merging automagically, even when the same file is
edited. There are however, some situations where the same line of code
is edited there is no way a computer can figure out how to merge.\
This will trigger a conflict which you will have to fix.

We now practise fixing merge conflicts. Recall that conflicts are caused
by merges which affect the same block of code.

Here’s a branch we prepared earlier. The branch is called `gitlab`. Run
the code below to set it up (don’t worry if you can’t understand it)

    $ git checkout gitlab

You should now have a new branch called `gitlab`. Try merging that
branch into `main` now and fix the ensuing conflict.

:confused: Stuck? <br>
Ask for help from the teacher

## Fixing a conflict

You should see a `conflict` with the `git-changed-me.txt` file. This means that
the same line of text was edited and committed on both the main branch
and the gitlab branch. The output below basically tells you the current
situation :

    Auto-merging git-changed-me.txt
    CONFLICT (content): Merge conflict in git-changed-me.txt
    Automatic merge failed; fix conflicts and then commit the result.

If you open the `git-changed-me.txt` file, you will see something similar as
below:

    $ cat git-changed-me.txt
    <<<<<<< HEAD
    Git: A Lifesaver for Collaboration
    When you’re new to the world of software engineering, there are fundamental skills you need to acquire to excel in your job. Git is undoubtedly one of those skills. As a junior developer, I was familiar with basic Git commands like git add, git commit, and git push. However, when I joined a team at Checkr, I realized there was much more to learn.

    ...

    Conclusion
    In summary, Git isn’t just a tool; it’s a mindset. It empowers software engineers to work efficiently, collaborate effectively, and embrace continuous improvement. As I reflect on my journey, I realize that Git has indeed changed my life as a developer. So, embrace Git, explore its features, and let it transform your coding experience!
    =======
    Git and Gitlab CI/CD: Transforming the Lives of Software Engineers
    As software engineers, we constantly face the challenge of optimizing our workflows. Git, the ubiquitous version control system, has been a game-changer for collaboration, code management, and professional growth. However, when we combine Git with Gitlab CI/CD, we unlock a whole new level of efficiency and automation. Let’s explore how these two tools have transformed my life as a developer.

    ...

    Conclusion
    Git and Gitlab CI/CD together empower software engineers to work efficiently, collaborate effectively, and embrace continuous improvement. As we reflect on our journey, we realize that these tools have indeed changed our lives as developers. So, embrace Git, explore Gitlab CI/CD, and let them transform your coding experience!
    >>>>>>> gitlab

Git uses pretty much standard conflict resolution markers. The top part
of the block, which is everything between `<<<<<< HEAD` and `======` is
what was in your current branch.\
The bottom half is the version that is present from the `gitlab` branch.
To resolve the conflict, you either choose one side or merge them as you
see fit.

For example, we might decide to choose the version from the `gitlab`
branch.

Now, try to **fix the merge conflict**. Pick the text that you think is
better

:confused: Stuck or stumped? <br>
Ask for help from the teacher


Once we have done that, we can then mark the conflict as fixed by using
`git add` and `git commit`.

    $ git add git-changed-me.txt
    $ git commit -m "Fixed conflict"

Congratulations. You have fixed the conflict. All is good in the world.

## :tada: Congratulations!

You have learnt :

1.  Branching and merging
2.  Fixing conflicts