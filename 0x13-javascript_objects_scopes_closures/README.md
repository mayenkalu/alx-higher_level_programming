# Javascript - Objects, Scopes and Closures :note:
[JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Basics) is a versatile programming language that has become an essential tool for web developers. Here are some reasons why JavaScript programming is amazing:
  *   JavaScript is a client-side language, which means that it runs on the user's browser rather than the server, allowing for dynamic and interactive web applications.
  *   JavaScript has a wide range of frameworks and libraries that make development faster and more efficient, such as React, Angular, and Vue.
  *   JavaScript is a flexible language that can be used for both front-end and back-end development, making it a popular choice for full-stack developers.
  *   JavaScript has a large and active community of developers who contribute to open-source projects and share knowledge and resources.

Creating an object in JavaScript is straightforward. You can use the object literal syntax, which involves enclosing a list of key-value pairs in curly braces:
```
let myObject = {
  name: 'John',
  age: 30,
  city: 'New York'
};
```
The this keyword in JavaScript refers to the object that the function is a method of. For example, in the following code, this refers to the person object:
```
let person = {
  name: 'John',
  age: 30,
  greet: function() {
    console.log('Hello, my name is ' + this.name);
  }
};
person.greet(); // Output: Hello, my name is John
```
In JavaScript, `undefined` is a value that represents the absence of a value. It is a primitive data type that is automatically assigned to variables that are declared but not initialized.

Variable type and scope are important in JavaScript because they determine how variables can be accessed and modified in different parts of the code. Variables in JavaScript can be declared using `var`, `let`, or `const`, each with different scoping rules.

A closure is a feature of JavaScript that allows a function to access variables in its outer scope, even after the function has returned. This can be useful for creating private variables and methods.
A prototype is a mechanism in JavaScript that allows objects to inherit properties and methods from other objects. All JavaScript objects have a prototype property, which refers to the object from which they inherit.

To inherit an object from another object in JavaScript, you can use the `Object.create()` method:
```
let parentObject = {
  name: 'John',
  age: 30
};

let childObject = Object.create(parentObject);
childObject.name = 'Jane';
console.log(childObject.name); // Output: Jane
console.log(childObject.age); // Output: 30
```

## Task Description:
1. [0-rectangle.js](./0-rectangle.js)
  - Script defines a class `Rectangle`.

2. [1-rectangle.js](./1-rectangle.js)
  - Builds on [0-rectangle.js](./0-rectangle.js).
  - The constructor must take 2 arguments `w` and `h`, initializing two instance attributes, `w`(`width`) and `h`(`height`).

3. [2-rectangle.js](./2-rectangle.js)
  - Builds on [1-rectangle.js](./1-rectangle.js).
  - creates an empty object, if `w` and `h` is equal to zero or not a positive integer.

4. [3-rectangle.js](./3-rectangle.js):
  - Builds on [3-rectangle.js](./3-rectangle.js).
  - Create an instance method called print() that prints the rectangle using the character `X`.

5. [4-rectangle.js](./4-rectangle.js)
  - Builds on [4-rectangle.js](./4-rectangle.js).
  - Creates instance methods- `rotate()` (that exchanges the `width` and `height` of the `Rectangle`) and `double()` (that multiplies the `width` and `height` of the `Rectangle` by `2`).

6. [5-square.js](./5-square.js)
  - Script defines a class `Square` that inherits from `Rectangle`.
  - Constructor takes one argument `size`.
  - The constructor of `Rectangle` must be called (by using `super()`).

7. [6-square.js](./6-square.js): 
  - Builds on [5-square.js](./5-square.js).
  - Creates an instance method `charPrint(c)` that prints the `Square` using the character `c`.
  - If `c` is `undefined`, use the character `X`.

8. [7-occurrences.js](./7-occurrences.js)
  - Function returns the number of occurrences in a list.
  - Prototype: `exports.nbOccurences = function (list, searchElement)`.

9. [8-esrever.js](./8-esrever.js)
  - Function reverses a list.
  - Prototype: `exports.esrever = function (list)`.
  - Not allowed to use the built-in method `reverse`.

10. [9-logme.js](./9-logme.js)
  - Function prints the number of  arguments already printed and the new argument value.
  - Output: `<number arguments already printed>: <current argument value>`

11. [10-converter.js](./10-converter.js)
  - Function converts a number from base 10 to another base passed as argument.
  - Prototype: `exports.converter = function (base)`.
  - Not allowed to import any file and declare any new variable (`var`, `let`, etc..).

12. [100-map.js](./100-map.js)
  - Script imports an array and must import `list`.
  - Must use a `map` and creates a new list with each value equal to the value of initial list times the index of the new list.
  - Prints both the initial and new list.

13. [101-sorted.js](./101-sorted.js)
  - Script imports a dictionary of occurrences by user ID and computes a new dictionary of user ID's by occurrence.
  - Script must import `dict`. In the new dictionary: A key is a number of occurrences and A value is the list of user ids.
  - Prints the new dictionary at the end.

14. [102-concat.js](./102-concat.js)
  - Script concatenates two files.
  - The first argument is the file path of the first source file.
  - The second argument is the file path of the second source file.
  - The third argument is the file path of the destination.


