# Best Practices and Pitfalls

### :zap: Commit, commit and commit some more
It’s much easier to fix small problems than big problems, as a general rule. One of the biggest advantages of continuous integration is that code is integrated into a shared repository against other changes happening at the same time. If a development team commits code changes early and often, bugs are easier to identify because there is less code to sort through.

By testing in small batches, code quality is improved and teams can iterate more effectively.

### :eyeglasses: Read the documentation (and then read it again)
Continuous integration systems make documentation widely available, and this documentation can be very helpful long after you’ve implemented CI into your workflow. 

> It can be helpful to reference the documentation in READMEs or in other accessible formats. Encourage team members to read the documentation first, bookmark links, create FAQs, and incorporate these resources into onboarding for new team members.

### :gem: Optimize pipeline stages
CI pipelines contain jobs and stages: Jobs are the activities that happen within a particular stage, and once all jobs pass, code moves to the next stage. To get the most out of your CI pipelines, optimize stages so that failures are easy to identify and fix.

Stages are an easy way to organize similar jobs, but there may be a few jobs in your pipeline that could safely run in an earlier stage without negatively impacting your project if they fail. Consider running these jobs in an earlier stage to speed up CI pipelines.

### :rocket: Make builds fast and simple
Nothing slows down a pipeline like complexity. Focus on keeping builds fast, and the best way to do that is by keeping things as simple as possible.

Every minute taken off build times is a minute saved for each developer every time they commit. Since CI demands frequent commits, this time can add up. Martin Fowler discusses a guideline of the ten-minute build that most modern projects can achieve. Since continuous integration demands frequent commits, saving time on commit builds can give developers a lot of time back.

### :factory: Use failures to improve processes
Improvement is a process. When teams change their response to failures, it creates a cultural shift for continuous improvement. Instead of asking who caused the failure, ask what caused the failure. This means shifting from a blaming culture to a learning culture.

If teams are doing frequent commits, it becomes much easier to identify problems and solve them. If there are patterns in failed builds, look at the underlying causes. Are there non-code errors that are causing builds unnecessarily? Maybe incorporate an allow_failure parameter. Look for ways to continually improve, make failures blameless, and look for causes (not culprits).

### :computer: Test environment should mirror production
In continuous integration, every commit triggers a build. These builds then run tests to identify if something will be broken by the code changes you introduce. The test pyramid is a way for developers to think of how to balance testing. End-to end testing is mostly used as a safeguard, with unit testing being used most often to identify errors. One important thing to keep in mind with testing is the environment. When the testing and production environments match, it means that developers can rely on the results and deploy with confidence.

> Continuous integration helps developers deploy faster and get feedback sooner. Ultimately, the best continuous integration system is the one you actually use. Find the right CI for your needs and then incorporate these best practices to make the most of your new CI workflow.