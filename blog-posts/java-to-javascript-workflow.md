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

For a front end linter I have learnt to use ESLint. A tool I had the luck of setting up myself for a client project, It flags code logic issues just like PMD does. It's `.eslintrc` file contains ruleset configuration and files to ignore can be included in an '.eslintignore'. VSCode also supports some fantastic ESLint extensions that will check your code as you write (no need to run any commands at all!)

## How to remove stuck bugs

Like the Mark II machine that [required a moth removed](https://www.computerhistory.org/tdih/september/9/), I too need to be able to debug my work.

<!-- IntelliJ debugger, step through code 1 line at a time (very helpful!), Git commit history -->

## How to manage packages and dependencies

<!-- the project/tooling Maven for plugins & dependency, IntelliJ for all sorts of checks -->