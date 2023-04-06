# Javascript - warm_up :script: 
[JavaScript](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics) is a high-level programming language that is commonly used for scripting and building web front-ends. It is an essential component of web development, allowing developers to create interactive, dynamic, and responsive web pages that can be customized and personalized based on user interactions.

In web front-end development, JavaScript is primarily used for adding interactivity and functionality to HTML and CSS code. JavaScript can be used to manipulate HTML elements, such as changing their content or appearance, responding to user input, and handling events like clicks and scrolls. It can also be used to dynamically generate HTML content, allowing developers to build web pages on the fly.

JavaScript is also used extensively for building web applications, such as online games, social media platforms, and e-commerce websites. With the advent of front-end frameworks like React and Angular, JavaScript has become even more popular, as these frameworks provide powerful tools for building complex and responsive user interfaces.

One of the main advantages of JavaScript is its ubiquity - it is supported by all major web browsers and can be used on both client-side and server-side programming. Moreover, the language is constantly evolving, with new features and updates being added regularly. This means that JavaScript is a versatile and flexible language that can adapt to changing web development trends and technologies.

However, JavaScript can also pose some security risks when used improperly, such as cross-site scripting (XSS) attacks or injection attacks. To mitigate these risks, developers must take care to write secure and well-structured code, and follow best practices and guidelines for web development.

**To run a JavaScript script**, you can use a command-line interface (CLI) such as the Terminal on a Mac or the Command Prompt on Windows. To run a JavaScript script, you must have a JavaScript interpreter installed on your system, such as Node.js or a web browser.
Here's an example of how to run a JavaScript script using Node.js:
```
node filename.js
```

Open a terminal window.
Navigate to the directory where the script is located using the `cd` command.
Type `node scriptname.js` and press Enter, where `scriptname.js` is the name of your script.

To create variables and constants in JavaScript, you can use the `var`, `let`, and `const` keywords. Variables and constants are used to store values that can be used later in your program.
Here's an example of how to create variables and constants in JavaScript:
```
// Create a variable
var myVar = 42;

// Create a constant
const PI = 3.14159;

// Create a variable using let
let myLetVar = "Hello";
```
`var`, `const`, and `let` are keywords used to declare variables and constants in JavaScript. The main differences between them are:
`var` is function-scoped, which means that it can be accessed anywhere within the function in which it is defined.
`let` and `const` are block-scoped, which means that they can only be accessed within the block in which they are defined.
`var` and `let` can be reassigned to a new value, while `const` cannot be reassigned once it has been initialized.
`const` requires an initial value when it is declared, while `var` and let do not.

JavaScript supports several data types:
Primitive data types: `number`, `string`, `boolean`, `null`, and `undefined`
Object data type: `object`
Special data types: `NaN` and `Infinity`

The `if` and `if...else` statements are used to execute code based on a condition. Here's an example:
```
let x = 10;

if (x > 5) {
  console.log("x is greater than 5");
} else {
  console.log("x is less than or equal to 5");
}
```
Comments can be used in JavaScript to add notes or explanations to your code. Single-line comments start with `//` and multiline comments start with `/*` and end with `*/`. Here's an example:
```
// This is a single-line comment
```
Values can be assigned to variables in JavaScript using the assignment operator `(=)`. For example:
```
let x = 4;
```
This code creates a variable called x and assigns it the value of 4.

**While loops and for loops** are used to repeat a block of code until a condition is met. Here's an example of a while loop:
```
let x = 1;
while (x <= 10) {
  console.log(x);
  x++;
}
```
This code will output the numbers from 1 to 10. Here's an example of a for loop:
```
for (let i = 1; i <= 10; i++) {
  console.log(i);
}
```
This code will also output the numbers from 1 to 10.

The `break` statement is used to exit a loop prematurely, while the `continue` statement is used to skip over a single iteration of a loop. Here's an example of using `break`:
```
for (let i = 1; i <= 10; i++) {
  if (i === 5) {
    break;
  }
  console.log(i);
}
```
This code will output the numbers from 1 to 4.
Here's an example of using `continue`:
```
for (let i = 1; i <= 10; i++) {
  if (i === 5) {
    continue;
  }
  console.log(i);
}
```
This code will output the numbers from 1 to 4, and then 6 to 10.

**A function** is a block of code that performs a specific task. You can define a function in JavaScript using the `function` keyword, followed by the function name, and a set of parentheses. Here's an example of a function that takes two parameters and returns their sum:
```
function addNumbers(x, y) {
  return x + y;
}
```
This function is called by passing in two arguments, like this:
```
let result = addNumbers(3, 5);
console.log(result);
```
If a `function` does not use any return statement, it will return `undefined` by default. For example:
```
function sayHello() {
  console.log("Hello, world!");
}
let result = sayHello();
console.log(result);
```
This code will output `Hello, world!` and then `undefined`.

In JavaScript, variables have function-level scope by default, meaning that they are only accessible within the function in which they are declared. However, variables declared with the `let` and `const` keywords have block-level scope, meaning that they are only accessible within the block in which they are declared (e.g. a loop or an if statement). Global variables, declared outside of any function or block, are accessible from anywhere in the code.

JavaScript has several arithmetic operators for performing mathematical operations:
      Addition: `+`
      Subtraction: `-`
      Multiplication: `*`
      Division: `/`
      Modulus (remainder): `%`
      Exponentiation: `**`
```
let x = 10;
let y = 5;
let z = x + y; // z equals 15
let w = x * y; // w equals 50
let r = x % y; // r equals 0
```
In JavaScript, a dictionary is typically called an object. An object can be created by enclosing key-value pairs in curly braces, like this:
```
let person = {
  name: "John",
  age: 30,
  city: "New York"
};
```
The values of an object's properties can be accessed using dot notation or bracket notation, like this:
```
console.log(person.name); // Output: John
console.log(person["age"]); // Output: 30
```
The properties of an object can be added or modified like this:
```
person.email = "john@example.com";
person.city = "Los Angeles";
```
A property from an object can be deleted using the `delete` keyword, like this:
```
delete person.email;
```
In JavaScript, you can import code from another file using the `import` statement. This is typically used in conjunction with modules, which are separate JavaScript files that contain specific functionality.
To import a module in a JavaScript file, use the following syntax:
```
import { function1, function2 } from "./module.js";
```
Replace `function1` and `function2` with the names of the functions or variables desired to import from the module, and replace `./module.js` with the path to the module file.

Note that the `import` statement is only supported in modern browsers and in Node.js version 13 and later. In older versions of Node.js, the CommonJS `require()` function is used to import modules.




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