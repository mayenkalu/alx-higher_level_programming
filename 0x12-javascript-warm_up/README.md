# Javascript - warm_up :script: 
[JavaScript](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics) is a high-level programming language that is commonly used for scripting and building web front-ends. It is an essential component of web development, allowing developers to create interactive, dynamic, and responsive web pages that can be customized and personalized based on user interactions.

In web front-end development, JavaScript is primarily used for adding interactivity and functionality to HTML and CSS code. JavaScript can be used to manipulate HTML elements, such as changing their content or appearance, responding to user input, and handling events like clicks and scrolls. It can also be used to dynamically generate HTML content, allowing developers to build web pages on the fly.

JavaScript is also used extensively for building web applications, such as online games, social media platforms, and e-commerce websites. With the advent of front-end frameworks like React and Angular, JavaScript has become even more popular, as these frameworks provide powerful tools for building complex and responsive user interfaces.

One of the main advantages of JavaScript is its ubiquity - it is supported by all major web browsers and can be used on both client-side and server-side programming. Moreover, the language is constantly evolving, with new features and updates being added regularly. This means that JavaScript is a versatile and flexible language that can adapt to changing web development trends and technologies.

However, JavaScript can also pose some security risks when used improperly, such as cross-site scripting (XSS) attacks or injection attacks. To mitigate these risks, developers must take care to write secure and well-structured code, and follow best practices and guidelines for web development.


## Objectives :bulb:
In this project, I understood and practiced:
  - Why JavaScript programming is amazing
  - How to run a JavaScript script
  - How to create variables and constants
  - What are differences between var, const and let
  - What are all the data types available in JavaScript
  - How to use the if, if ... else statements
  - How to use comments
  - How to affect values to variables
  - How to use while and for loops
  - How to use break and continue statements
  - What is a function and how do you use functions
  - What does a function that does not use any return statement return
  - Scope of variables
  - What are the arithmetic operators and how to use them
  - How to manipulate dictionary
  - How to import a file

## Task description:
  1. [0-javascript_is_amazing.js](./0-javascript_is_amazing.js)
      -  JavaScript script that creates a constant variable `myVar` with the value `'Javascript is amazing'`.
      -  Usage: `./0-javascript_is_amazing.js`

  2. [1-multi_languages.js](./1-multi_languages.js)
      -  JavaScript script that prints three lines.
      -  Usage: `./1-multi_languages.js`
      -  Line 1: `'C is fun'`.
      -  Line 2: `'Python is cool'`.
      -  Line 3: `'Javascript is amazing'`.

  3. [2-arguments.js](./2-arguments.js)
      -  JavaScript script that prints a message depending on the number of arguments passed.
      -  Usage: `./2-arguments.js <arg 1> <arg 2> ...`
      -  If no arguments are passed, prints `'No argument'`.
      -  If one argument is passed, prints `'Argument found'`.
      -  Otherwise, prints `'Arguments found'`.

  4. [3-value_argument.js](./3-value_argument.js)
      -  JavaScript script that prints the first argument passed to it.
      -  Usage: `./3-value_argument.js <arg>`
      -  If no argument is passed, prints `'No argument'`.

  5. [4-concat.js](./4-concat.js)
      -  JavaScript script that prints two arguments passed in the format `<arg 1>  is <arg 2>`.
      -  Usage: `./4-concat.js <arg1> <arg2>`

  6. [5-to_integer.js](./5-to_integer.js)
      -  JavaScript script that prints `My number: <first argument converted in integer>` if the first pased argument can be converted to an integer.
      -  Usage: `./5-to_integer.js`
      -  If the argument cannot be converted to an integer, prints `'Not a number'`.

  7. [6-multi_languages_loop.js](./6-multi_languages_loop.js)
      -  JavaScript script that prints three lines using an array and a loop.
      -  Usage: `./6-multi_languages_loop.js`
      -  First line: `'C is fun'`.
      -  Second line: `'Python is cool'`.
      -  Third line: `'Javascript is awesome'`.

  8. [7-multi_c.js](./7-multi_c.js): JavaScript script that prints `x` times `'C is fun'`.
  * Usage: `./7-multi_c.js <x>`
  * If the first argument cannot be converted to a number, prints
  `'Missing number of occurrences'`.

  9. [8-square.js](./8-square.js): JavaScript script that prints a square.
  * Usage: `./8-square.js <size>`
  * If the first argument cannot be converted to a number, prints `'Missing size`'.
  * Uses the `X` character to print the square.

  10. [9-add.js](./9-add.js): JavaScript script that prints the addition of two
  numbers passed as arguments.
  * Usage: `./9-add.js <number 1> <number 2>`
  * Prototype: `function add(a, b)`

  11. [10-factorial.js](./10-factorial.js): JavaScript script that computes and
  prints a factorial.
  * Usage: `./10-factorial.js <number to compute factorial of>`

  12. [11-second_biggest.js](./11-second_biggest.js): JavaScript script that
  locates the second largest number in the list of provided arguments.
  * Usage: `./11-second_biggest.js <arg 1> <arg 2> ...`
  * If no arguments are passed or the number of arguments is `1`, prints `0`.

  13. [12-object.js](./12-object.js): Update of the following script that replaces
  the value `12` with `89`.
```
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);
```

  14. [13-add.js](./13-add.js): JavaScript function `add` that returns the addition
  of two numbers.

  15. [100-let_me_const.js](./100-let_me_const.js): JavaScript script that modifies
  the value of `myVar` in the following file to `333`.
```
#!/usr/bin/node
myVar = 89;
require('./100-let_me_const')
console.log(myVar);
```

  * [101-call_me_moby.js](./101-call_me_moby.js): JavaScript function that executes
  `x` times a given function.

  * [102-add_me_maybe.js](./102-add_me_maybe.js): JavaScript function that
  increments a given number and calls a given function.

  * [103-object_fct.js](./103-object_fct.js): Update of the following JavaScript
  script adding a new function `incr` that increments the number `value`.
```
#!/usr/bin/node
let myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
```