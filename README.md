Test

24/12/2019
I added the .gitignore precompiled file from Github. It is now correctly ignoring the \__pycache__ folders

Virtualization in python: venv seems like overkill. It's better to use just pipenv, it's lighter and makes less mess in the files.



Questions for the programmer:
while I write code, how should I strucure it?
Part of the answer comes from the language itself and what is needed. Another part
comes from the design pattern chosen for the project. Some other parts defy both of these necessities and are up to the programmer. It is mostly important to have a space organized by categories (i.e., what that file is for). Put file of the same category in folders.

How do I solve problems?
Just follow what the interpreter says to you. Read compiler errors carefully and try to understand what is happening. It is ok and normal if you don't understand anything. Just Google the feedback and try to make most of what comes up. Try to tame errors and learn from them. StackOverflow is your best friend. Documentation (of a language, framework, protocol, anything) is your guardian protector.

How should I work?
When approaching something complex, just sketch the outlines (what kind of files could be possibly needed, what some lines of code should do...). I've found for myself that writing pseudocode is very useful and provides a skeleton for real code to come, so that you don't forget what comes next while programming.
Also, remember to test from time to time, and to read variables (dumping them or using a debugger).
This way you'll know what is happening inside your code and know how to handle some unforeseen instantiated variable.