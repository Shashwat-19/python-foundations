# Python Foundations – Curated Learning Path

![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat-square)
![Status](https://img.shields.io/badge/status-active-success?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-lightgrey?style=flat-square)

## Overview

This repository hosts a structured and curated learning path for mastering the Python programming language. It aggregates and synthesizes curriculum materials from industry-standard sources including CS50 (Harvard), Apna College, CodeWithHarry, and freeCodeCamp.

The content is designed for engineers and developers seeking a rigorous understanding of Python fundamentals, best practices in software design, and readiness for advanced domains such as backend development and data engineering. This is not strictly a tutorial repository, but a record of disciplined engineering practice.

## Goals

- **Foundational Mastery**: Establish a deep understanding of Python's memory model, data structures, and execution flow.
- **Code Quality**: Enforce clean, readable, and PEP 8 compliant code standards.
- **Engineering Discipline**: cultivate habits of testing, documentation, and version control from the outset.
- **System Readiness**:Prepare for complex systems programming, including concurrency and backend architecture.

## Learning Philosophy

The approach adopted in this repository prioritizes "first principles" thinking over syntax memorization.

1. **Concept Acquisition**: Theoretical study from curated high-quality lectures.
2. **Implementation**: Writing code from scratch to solve specific algorithmic problems.
3. **Analysis**: documenting edge cases, performance implications, and language behavior options.
4. **Refinement**: Refactoring code for readability and efficiency, followed by rigorous unit testing.
5. **Application**: Integrating concepts into small-scale, modular projects.

## Repository Structure

The repository is organized into progressive modules, each adhering to a specific domain of the language.

```text
python-foundations/
├── 00-introduction-setup/      # Environment configuration and CLI basics
├── 01-variables-datatypes/     # Memory management and type systems
├── 02-strings-conditionals/    # Text processing and control flow logic
├── 03-lists-tuples/            # Sequence types and mutability
├── 04-dictionaries-sets/       # Hash maps and set theory
├── 05-loops/                   # Iteration protocols and efficiency
├── 06-functions-recursion/     # Stack frames, scope, and functional patterns
├── 07-file-io/                 # Persistence and context management
├── 08-oops/                    # Inheritance, polymorphism, and encapsulation
├── 09-exceptions/              # Error handling strategies
├── 10-unit-testing/            # Test-driven development with pytest
├── 11-regex/                   # Pattern matching and text extraction
├── 12-advanced-python/         # Decorators, generators, and introspection
├── 13-concurrency/             # Threading and multiprocessing
├── projects/                   # Capstone applications
│   ├── cli-todo/
│   └── expense-tracker/
├── requirements.txt            # Dependency definitions
└── README.md
```

## Topics Covered

- **Core Syntax & Semantics**: Complete coverage of built-in types and operators.
- **Data Structures**: In-depth analysis of list implementations, hashing mechanisms in dictionaries, and algorithmic complexity.
- **Control Flow**: Advanced iteration, list comprehensions, and structural pattern matching.
- **Object-Oriented Programming**: Design patterns, dunder methods, and interface design.
- **Software Testing**: Unit testing methodologies using `pytest`.
- **System Operations**: File I/O, serialization (`json`, `pickle`), and environment management.
- **Advanced Concepts**:
  - Decorators and closures
  - Iterators and Generators
  - Context Managers
  - Regular Expressions
  - Concurrency models

## Tools & Technologies

- **Language**: Python 3.x
- **Testing**: pytest
- **Version Control**: Git & GitHub
- **Environment**: Virtual Environments (`venv`)
- **Editor**: VS Code

## Projects

### CLI To-Do Application

A command-line interface application demonstrating distinct separation of concerns, persistent storage, and user input validation.

### File-based Expense Tracker

An analytical tool focusing on data serialization, file handling reliability, and basic data aggregation algorithms.

## Progress Status

This repository is currently **Active**. Content is being added and refined continuously as the learning path progresses.

## License

This project is released under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

Curriculum structure and concepts are derived from the following educational resources:

- **CS50 (Harvard University)**: Introduction to Computer Science
- **Apna College**: Comprehensive Python Tutorials
- **CodeWithHarry**: Practical Python implementation
- **freeCodeCamp**: Specialized modules and project ideas
