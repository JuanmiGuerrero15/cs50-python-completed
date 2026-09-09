# CS50 – Introduction to Programming with Python

This repository contains my solutions to Harvard University's **CS50's Introduction to Programming with Python** course.

I am using this course to strengthen my programming foundations, with a particular interest in **computational linguistics, natural language processing (NLP), and language technologies**.

---

## 📈 Progress

- Problem Set 0: Completed ✔️
- Problem Set 1: Completed ✔️
- Problem Set 2: Completed ✔️
- Problem Set 3: Completed ✔️
- Problem Set 4: Completed ✔️
- Problem Set 5: Completed ✔️
- Problem Set 6: Completed ✔️
- Problem Set 7: Completed ✔️
- Problem Set 8: Completed ✔️
- Final Project: Completed ✔️

---

## 🧠 Topics Covered

### 0 – Functions & Variables

- Input and output handling
- Variables and assignment
- Functions and return values
- Function parameters and arguments
- Basic arithmetic and mathematical operations
- Type conversion (`int`, `float`, `str`, `bool`)
- String formatting and f-strings
- Working with user input
- Designing simple programs through functions

---

### 1 – Conditionals

- Conditional logic (`if`, `elif`, `else`)
- Boolean expressions
- Comparison and logical operators
- Truth values
- Nested conditionals
- String methods (`lower`, `strip`, `replace`, `split`, `endswith`)
- Text normalization and parsing
- Input validation
- Problem decomposition

---

### 2 – Loops

- `for` and `while` loops
- Nested loops
- Iteration over strings, lists, and ranges
- `break` and `continue`
- Input validation using loops
- Counters and accumulators
- State tracking
- Iterating over collections
- Pattern generation
- Avoiding infinite loops

---

### 3 – Exceptions

- `try` / `except` for error handling
- `ValueError`
- Handling invalid user input
- Preventing program crashes
- Robust input validation
- Distinguishing runtime errors from logical errors
- Raising exceptions with `raise`
- Understanding and debugging tracebacks

---

### 4 – Libraries & APIs

- Importing and using Python libraries
- Standard libraries such as:
  - `random`
  - `sys`
  - `requests`
  - `inflect`
  - `json`
- Command-line arguments with `sys.argv`
- Exiting programs with `sys.exit`
- Random number generation
- Working with external APIs
- HTTP requests
- JSON data
- API authentication and API keys
- Nested dictionaries and data structures
- Handling network errors with `requests.RequestException`
- Parsing API responses
- Formatting numerical and financial data
- Currency conversion
- Working with third-party packages

---

### 5 – Unit Tests

- Automated testing with `pytest`
- Writing unit tests
- Testing individual functions
- Assertions
- Testing expected outputs
- Testing invalid inputs
- Testing edge cases
- Organizing test files
- Using `assert`
- Understanding the importance of automated testing
- Identifying bugs through systematic testing

---

### 6 – File I/O

- Reading and writing files
- Opening files with `open()`
- Using `with` for safe file handling
- Reading files line by line
- Writing data to files
- File paths
- Handling `FileNotFoundError`
- Working with text files
- Processing structured data
- CSV files
- The `csv` module
- `csv.reader`
- `csv.DictReader`
- Writing CSV files
- Dictionaries and lists as structured data
- Sorting collections with `sorted()`
- Using `key` functions and `lambda`
- Working with JSON files
- Serialization and deserialization
- Data transformation and processing

---

### 7 – Regular Expressions

- Pattern matching with regular expressions
- The `re` module
- `re.search()`
- `re.match()`
- `re.fullmatch()`
- `re.sub()`
- Capturing groups
- Character classes
- Quantifiers
- Anchors
- Alternation
- Escaping special characters
- Extracting information from text
- Validating structured input
- Parsing dates, times, URLs, emails, and other patterns
- Using regular expressions for text processing

---

### 8 – Object-Oriented Programming

- Classes and objects
- Creating custom data types
- Constructors with `__init__`
- Instance attributes
- Instance methods
- `self`
- Class attributes
- Encapsulation
- Object state
- Representing real-world entities through objects
- Inheritance
- Method overriding
- Polymorphism
- Reusing and organizing code through classes
- Understanding object-oriented program structure

---

### 9 – Et Cetera

- Sets with `set`
- Removing duplicate values
- Global variables
- Constants
- Type hints
- Static type checking with `mypy`
- Writing docstrings
- Command-line argument parsing with `argparse`
- Unpacking sequences and dictionaries
- `*args` and `**kwargs`
- `map()`
- `filter()`
- List comprehensions
- Dictionary comprehensions
- `enumerate()`
- Generators
- `yield`
- Iterators
- Writing more concise and expressive Python code
- Improving code readability and maintainability

---

## 🧩 Python Concepts Developed

Throughout the course, I have worked with:

- Variables and data types
- Strings and string manipulation
- Lists
- Tuples
- Sets
- Dictionaries
- Functions
- Lambda functions
- Loops
- Conditionals
- Exceptions
- Modules and libraries
- Command-line arguments
- File handling
- CSV and JSON
- APIs
- Regular expressions
- Classes and objects
- Unit testing
- Data structures
- Algorithms
- Sorting and searching
- Input validation
- Error handling
- Type hints
- Comprehensions
- Iterators and generators
- Command-line interfaces

---

## 🛠️ Tools & Technologies

- **Python**
- **Git & GitHub**
- **pytest**
- **mypy**
- **CSV / JSON**
- **REST APIs**
- **Regular Expressions**
- **Command-line interfaces**
- **VS Code**
- **Python Package Manager (pip)**

---

## 🧠 Skills Developed

- Translating real-world problems into code
- Breaking complex problems into smaller functions
- Writing modular and reusable programs
- Designing clear control flow
- Debugging runtime and logical errors
- Reading and interpreting error messages
- Handling invalid input and edge cases
- Working with files and structured data
- Consuming and processing external APIs
- Manipulating and transforming text
- Validating structured information
- Writing automated tests
- Applying object-oriented programming principles
- Working with regular expressions
- Processing textual data
- Thinking algorithmically
- Improving code readability and organization
- Designing command-line applications
- Developing and documenting an independent Python project

---

## 🔤 Relevance to Computational Linguistics

Several concepts from this course are particularly relevant to my academic and professional interests in **computational linguistics and natural language processing**.

The course has provided a foundation for:

- Text processing and normalization
- String manipulation
- Pattern matching with regular expressions
- Structured text extraction
- Data cleaning and transformation
- Working with collections of textual data
- Processing CSV and JSON datasets
- Consuming language-related APIs
- Automating repetitive linguistic tasks
- Designing modular text-processing programs
- Comparing and analysing textual data

These skills provide a foundation for progressing toward more advanced topics such as:

- Natural Language Processing (NLP)
- Corpus linguistics
- Computational morphology
- Computational syntax
- Information extraction
- Text classification
- Stylometry
- Machine learning for language
- Large Language Models (LLMs)

---

# 📝 Final Project

## Computational Text Analysis

For my CS50P final project, I developed a **Python-based computational text analysis program**.


### 🔍 Language Identification

The program can create and use language profiles based on reference texts. These profiles represent the distribution of characters and other textual features found in a language corpus.

When a new text is provided, the program processes it and compares its characteristics with the stored language profiles. It then calculates similarity scores and uses them to estimate the most likely language.

This approach demonstrates how relatively simple statistical properties of language can be used to perform a basic NLP task.

### 📁 Project Structure

The complete implementation can be found in the [`final project`](./final%20project) folder.

The project includes the Python source code, reference language profiles, textual data, and tests used to validate the main functionality.

The project was designed as a standalone command-line application and brings together many of the concepts developed throughout CS50P, including functions, loops, dictionaries, sets, file I/O, JSON, regular expressions, exception handling, unit testing, and modular program design.

### 🎯 Why I Chose This Project

I chose this project because I wanted the final assignment to go beyond demonstrating Python syntax and instead connect programming with my background in **Hispanic Philology and linguistics**.

The project represents an initial step toward **computational linguistics and NLP**, where linguistic phenomena can be represented as data and analysed through computational methods.

It also allowed me to explore a question that is particularly interesting to me: **how much information about language and writing style can be extracted from the text itself?**

---

## 📚 Problem Sets

### Problem Set 0 – Functions, Variables

- Indoor Voice
- Playback Speed
- Making Faces
- Einstein
- Tip Calculator

### Problem Set 1 – Conditionals

- Deep Thought
- Home Federal Savings Bank
- File Extensions
- Math Interpreter
- Meal Time

### Problem Set 2 – Loops

- camelCase
- Coke Machine
- Just Setting Up My Twttr
- Vanity Plates
- Nutrition Facts

### Problem Set 3 – Exceptions

- Fuel Gauge
- Felipe's Taqueria
- Grocery List
- Outdated

### Problem Set 4 – Libraries

- Emojize
- Frank, Ian and Glen's Letters
- Adieu, Adieu
- Guessing Game
- Little Professor
- Bitcoin Price Index

### Problem Set 5 – Unit Tests

- Testing My Twit
- Back to the Bank
- Re-requesting a Vanity Plate
- Refueling

### Problem Set 6 – File I/O

- Lines of Code
- Pizza Py
- Scourgify
- CS50 P-Shirt

### Problem Set 7 – Regular Expressions

- NUMB3RS
- Watch on YouTube
- Working 9 to 5
- Regular, um, Expressions
- Response Validation

### Problem Set 8 – Object-Oriented Programming

- Seasons of Love
- Cookie Jar
- CS50 Shirtificate

---

## 🎯 Goal

My goal is to build a strong foundation in **Python programming and computational thinking** and progressively apply these skills to **computational linguistics, natural language processing, and language technologies**.

CS50 provides the programming foundation; my next step is to combine it with my background in **Hispanic Philology and linguistics** to work on computational approaches to language.

The final project represents the first step in that direction by applying Python programming to the analysis of real textual data.

---

## 📌 Note

This repository documents my learning journey through **CS50's Introduction to Programming with Python**.

Each problem set represents a step in developing my programming skills, from basic procedural programming and control flow to file processing, APIs, regular expressions, testing, object-oriented programming, and more advanced Python features.

The final project brings these skills together in an independent application focused on **computational text analysis**, providing a bridge between my background in **linguistics** and my growing interest in **programming, NLP, and computational linguistics**.

The solutions in this repository reflect my progression in **Python, problem-solving, debugging, algorithmic thinking, text processing, and computational approaches to language**.
