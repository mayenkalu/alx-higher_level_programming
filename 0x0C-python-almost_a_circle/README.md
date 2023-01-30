# Python - Almost a circle
This project prepares for the AirBnB project, which is a big part of the Higher level curriculum. 

This project, reviews everything about Python:- Import, Exceptions, Class, Private attribute, Getter/Setter, Class method, Static method, Inheritance, Unittest, Read/Write file.

It also explores: `args` and `kwargs`, Serialization/Deserialization, JSON.

## Learning Objectives

At the end of this project, the following should be explained:

- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- What is \*args and how to use it
- What is \*\*kwargs and how to use it
- How to handle named arguments in a function

## Tasks
### Descriptions
- [models] - folder containing all the classes and corresponding subclass
- [base.py] - Contains the base class Base for all other classe:
- Class Base:
- private class attribute \_\_nb\_objects = 0
- class constructor: def __init__(self, id=None)::
	- if id is not None, assign the public instance attribute id with this argument value - you can assume id is an integer and you don’t need to test the type of it
	- otherwise, increment \__nb\_objects and assign the new value to the public instance attribute id
