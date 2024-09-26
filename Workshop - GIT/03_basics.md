## Starting your journey

First, clone this repository:

    $ git clone https://github.com/commd-hr/workshop-git

You may want to fork (create your own copy of) the project on github and
clone from your own repo. You can find the fork button at the top right of
the screen on a github repository, or more help about doing that [here](https://help.github.com/articles/fork-a-repo/).

Once you have cloned your repository, you should now see a directory called `workshop-git`. This is your `working directory`

    $ cd workshop-git
    $ ls

:bulb: Everywhere that `ls` is used, you can use `dir` on Windows.

:no_mouth: Stuck? <br>
Ask for help from the teacher

For the curious, you should also see the `.git` subdirectory. This is
where all your repository’s data and history is kept.

    $ ls -a .git

You will see :

    branches  config  description  HEAD  hooks  info  objects  refs

## The staging area

Now, let’s try adding some files into the project. Create a couple of
files.

Let’s create two files named `processing.txt` and `tools.txt`.

    $ touch processing.txt tools.txt

:bulb: For Windows we need to use some other command:

    > echo "" > processing.txt & echo "" > tools.txt

Let’s use a mail analogy.

In Git, you first add content to the `staging area` by using `git add`.
This is like putting the stuff you want to send into a cardboard box.
You finalize the process and record it into the git index by using
`git commit`. This is like sealing the box - it’s now ready to send.

Let’s add the files to the staging area

    $ git add processing.txt tools.txt

## Committing

You are now ready to commit. The `-m` flag allows you to enter a message
to go with the commit at the same time.

    $ git commit -m "I am adding two new files"

:anguished: Stuck? <br>
Ask for help from the teacher

## Let’s see what just happened

We should now have a new commit. To see all the commits so far, use
`git log`

    $ git log

The log should show all commits listed from most recent first to least
recent. You would see various information like the name of the author,
the date it was commited, a commit SHA number, and the message for the
commit.

You should also see your most recent commit, where you added the two new
files in the previous section. However git log does not show the files
involved in each commit. To view more information about a commit, use
`git show`.

    $ git show

You should see something similar to:

    commit f72e20f112dfa87f4cbff9e1130cd06b0b625996
    Author: Ditmar Commandeur <commd@hr.nl> 
    Date:   Tue Apr 23 08:48:54 2024 +0200

        I am adding two new files

:confused: Stuck? <br>
Ask for help from the teacher

## A necessary digression

In this section, we are going to add more changes, and try to recover
from mistakes.

Be forewarned, this next step is going to be hard. We will need to add
some content to processing.txt.

Open `processing.txt` and type in your favourite line from a song, or:

e.g. Lorem ipsum Sed ut perspiciatis, unde omnis iste natus error sit
voluptatem accusantium doloremque laudantium

Then **save** the file

What did we change? A very useful command is `git diff`. This is very
useful to see exactly what changes you have done.

    $ git diff

You should see something like the following:

    diff --git a/processing.txt b/processing.txt
    index 1899a1c..b0ed26b 100644
    --- a/processing.txt
    +++ b/processing.txt
    @@ -1 +1 @@
    -""
    +This is some new text
    \ No newline at end of file

:grey_question:
Stuck? Ask for help from the teacher

## Staging area again

Now let’s add our modified file, `processing.txt` to the staging area. Do you
remember how ?

Next, check the `status` of `processing.txt`. Is it in the staging area now?

:expressionless: Stuck? <br>
Ask for help from the teacher

## Undoing - full

Let’s say we did not like putting Lorem ipsum into `processing.txt`. One
advantage of a staging area is to enable us to back out before we
commit - which is a bit harder to back out of. Remembering the mail
analogy - it’s easier to take mail out of the cardboard box before you
seal it than after.

Here’s how to back out of the staging area :

    $ git reset HEAD processing.txt

    Unstaged changes after reset:
    M   processing.txt

Compare the `git status` now to the git status from the previous
section. How does it differ?

:weary: Stuck? <br>
Ask for help from the teacher

Your staging area should now be empty. What’s happened to the Lorem
Ipsum changes? It’s still there. We are now back to the state just
before we added this file to staging area. Going back to the mail
analogy, we just took our letter out of the box.

## Undoing - specific files

Sometimes we did not like what we have done and we wish to go back to
the last *recorded* state. In this case, we wish to go back to the state
just before we added the Lorrem ipsum text to `processing.txt`.

To accomplish this, we use `git checkout`, like so:

    $ git checkout processing.txt

You have now un-done your changes. Your file is now empty.

:neutral_face: Stuck? <br>
Ask for help from the teacher


## :tada: Congratulations!

You have learnt :

1.  Clone a repository
2.  Commit files
3.  Check status
4.  Check diff
5.  Undoing changes
