# Java to Javascript; A Workflow Analysis

During my developer training and first project I learnt how to develop Java applications. However recently I have begun working on some front end projects, requiring a whole new set of skills. Writing Javascript is something I am currently upskilling in and while I'm able to create webpages and unit test simple code using Jest I am less aware of all the other available tooling within a front end ecosystem. So what tools are there around Javascript that I may have seen Java equivalent versions of before?

## How to write code the TDD way

With Java, adding to a code base is a case of expanding or adding functions or classes to implement new functionality. Lots of aspects (interface object security, type safety, etc.) of Java don't need testing, but to guarantee a codebase's health JUnit and Mockito have been my tools of choice for adding unit tests. Using Spring <mockmvc> I've been able to mock endpoint request calls and responses for (sort of) integration tests and end to end tests.

In Javascript, unit testing is most commonly done through Jest. It's declarative structure is a little confusing at first sight, but the concepts are the same. Instead of calling declared functions more often I find myself rendering React components and asserting on what they return. Cypress, a full fledged front end testing framework  <!-- <check this>  --> is something that may tailor front end visual testing better - I'll add this to my "To learns".

<!-- <should I add something here about lighthouse?> -->

## Assuring code formatting and order

For styling code, the first tool I learnt to use was Checkstyle. This utility will flag styling inconsistencies within your code according to a set of rules. Most often pre defined rule sets are used, but rules can be added, reworded or removed entirely if desired. 

The front end equivalent I have found (and seems to be standard everywhere for JS and TS) is Prettier. Prettier works almost identically to Checkstyle - checking for formatting issues. VSCode includes a widely downloaded extension to enforce Prettier rules on save, a very helpful utility for applying this tool. I imagine checkstyle has the same sort of extension for IntelliJ, something I should look into.

## Automated code assessment

My first encounter with a linter was PMD. It scans all changes like Checkstyle but checks for more nuanced issues within the logic of the code; more specifically areas of improvement. One time use declared variables or types that can be more specifically defined are flagged to the user. Spotting minor mistakes a human can make with machine consistency can be (and is) quite useful.

For a front end linter I have learnt to use ESLint. A tool I had the luck of setting up myself for a client project, It flags code logic issues just like PMD does. It's `.eslintrc` file contains ruleset configuration and files to ignore can be included in an `.eslintignore`. VSCode also supports some fantastic ESLint extensions that will check your code as you write (no need to run any commands at all!)

## How to remove stuck bugs

Like the Mark II machine that [required a moth removed](https://www.computerhistory.org/tdih/september/9/), I too need to be able to debug my work. IntelliJ includes a "debug" mode that, once you understand how it works, revolutionises understanding issues in code. I'd compare fixing Java code problems before I used this debug tool to solving a crime with no evidence. Adjusting code blindly, perhaps throwing a `console.log` here and there, hoping one of the attempts will unearth the issue. Seeing all your variables state at any given time, being able to step over & through line by line allows a developer to find the exact point everything goes awry and it's brilliantly useful.

I've learnt a lot about the Google Chrome devtools for fixing CSS issues, but not so much for the Javascript logic in my front-end work. And as much as I rave about the usefulness of a debugger in Java, I am still yet to use one in Javascript. I've definitely felt the need for one many times, but I'm yet to have the opportunity, remote desktop permission, time, energy (or whatever excuse I feel like using at time time) to explore how to use one. This will definitely be at the top of my list of things to explore in the near future, my writing of this paragraph is making that very clear!

<!-- IntelliJ debugger, step through code 1 line at a time (very helpful!), Git commit history -->

## How to manage external dependencies

I have experienced the benefits and difficulties of using Maven and Gradle. Although I must state I have never set any of these build-automation tools up, I do feel they simplify the area I've worked the most with - package management. Adding Checkstyle and PMD (something a team member did on a recent project) also seems very painless.

For front end package management I've used Node, more specificaly it's package manager npm. Creating config through terminal import commands makes quickly setting up projects easy, plus it seems almost every sort of dependency you could want is posted to nodes package registry. I have no desire to look for an alternative tool, this one seems perfect.

## So... What's missing?

Exploring the equivalent tooling for front end and back end tooling has highlighted some things I should look into learning

1. **A front end debugger.** I definitely clarified in my head the benefit of a debugger in this article. Now realising I'm yet to learn how to debug Javascript has'
2. **More extensive testing tooling.**. With only expeience in Jest I should check out what else I can use to test my code. Maybe Cypress or Lighthouse is a good place to start...
3. **Checkstyle & PMD Extensions.** Perhaps all my envy for the convenience of the Prettier and ESLint extensions can be resolved?