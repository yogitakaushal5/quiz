#15/04/2026
#assignment=5

1. What are the key features of Python?

Python is easy to learn, has simple readable syntax, is interpreted, dynamically typed,
 platform independent, and has a large standard library.

2. Why is Python called an interpreted language?

Because Python executes code line by line instead of converting the whole program into machine
 code at once.

3. Difference between compiled and interpreted languages

Compiled languages (like C) convert the whole code before execution. Interpreted languages 
(like Python) execute code line by line.

4. What makes Python dynamically typed?

You don’t need to declare the data type of a variable. The type is decided at runtime.

5. Why is Python platform independent?

Python code can run on different operating systems without changing the code.

6. Advantage of Python being a high-level language

It is easy to write, read, and understand, so development is faster.

7. Limitations of Python

Python is slower than low-level languages and uses more memory.

8. How does Python execute a program internally?

Python first converts source code into bytecode, then executes it using the Python Virtual
 Machine (PVM).

9. What is bytecode in Python?

Bytecode is an intermediate code generated from source code, which is not machine code but
 closer to it.

10. What is PVM (Python Virtual Machine)?

PVM is the engine that executes bytecode line by line.

11. Difference between source code, bytecode, and machine code

Source code is written by humans, bytecode is intermediate code, and machine code is binary
 code executed by the computer.

12. Does Python compile code before execution?

Yes, Python compiles code into bytecode before executing it.

13. Where is bytecode stored?

In the __pycache__ folder as .pyc files.

14. Is Python fully interpreted?

No, Python is both compiled (to bytecode) and interpreted (executed by PVM).

15. What is compilation in Python?

It is the process of converting source code into bytecode.

16. What is parsing in Python?

Parsing checks the structure of the code according to grammar rules.

17. What is a parse tree?

It is a tree representation showing the full structure of the code.

18. What is Abstract Syntax Tree (AST)?

It is a simplified version of the parse tree used for execution.

19. Difference between parse tree and AST

Parse tree is detailed; AST is simplified and optimized.

20. What role does AST play in Python execution?

AST helps in optimizing and converting code into bytecode.

21. What is the compilation pipeline in Python?

Source code → Tokens → Parse tree → AST → Bytecode → Execution.

22. What are the steps from source code to execution?

Write code → Compile to bytecode → Execute using PVM.

23. What is lexical analysis in Python?

It breaks code into tokens like keywords, variables, and operators.

24. What is syntax analysis in Python?

It checks whether the code follows correct grammar rules.

25. What happens if there is a syntax error?

The program stops and shows an error message.

26. What is a code object in Python?

It is a compiled version of Python code ready for execution.

27. What is a .pyc file?

It is a file that stores compiled bytecode.

28. When are .pyc files created?

They are created when the program runs for the first time.

29. What is the purpose of pycache folder?

It stores bytecode files to speed up execution.

30. Does Python recompile code every time?

No, it reuses bytecode if the source code is not changed.

🔹 Data Types
31. Built-in data types in Python

int, float, string, list, tuple, set, dictionary.

32. Difference between mutable and immutable

Mutable objects can be changed (list), immutable cannot (string, tuple).

33. Why are strings immutable?

To improve performance and ensure data safety.

34. What is None type?

It represents no value or null.

35. Can Python store multiple data types in one variable?

Yes, variables can change type during execution.

36. What is type casting?

Converting one data type to another.

37. Difference between implicit and explicit conversion

Implicit happens automatically, explicit is done manually.

38. Example of implicit conversion

int + float = float.

39. What happens when you convert float to int?

Decimal part is removed.

40. Can we always convert string to int?

No, only if the string contains a valid number.

41. What error occurs if conversion fails?

ValueError.

🔹 Input & Output
42. Difference between input() and print()

input() takes user input, print() displays output.

43. Why input() returns string?

Because all user input is treated as text by default.

44. How to take integer input?

Use int(input()).

45. sep and end in print()

sep separates values, end defines how the line ends.

46. Multiple inputs in one line

Use input().split().

47. Output formatting

Use f-strings or format().

🔹 Operators
48. Difference between / and //

/ gives float result, // gives integer (floor).

49. Use of % operator

Gives remainder.

50. Use of ** operator

Used for power.

51. Why ^ is not power operator?

Because it is a bitwise XOR operator.

52. Assignment operators

=, +=, -=, *=, etc.

53. Difference between = and ==

= assigns value, == compares values.

54. += operator internally

It adds and assigns: x = x + value.

55. Output of 5 > 3 > 1

True.

56. Can relational operators be chained?

Yes, Python allows chaining.

🔹 Variables
57. What is a variable?

A name used to store data.

58. Why no need to declare type?

Because Python is dynamically typed.

59. Can we change variable type?

Yes, anytime.

60. Multiple assignment

Assign multiple values at once.

61. Swap without third variable

a, b = b, a

🔹 Identifiers
62. What are identifiers?

Names of variables, functions, etc.

63. Rules for identifiers

Start with letter/underscore, no spaces, no keywords.

64. Can identifier start with number?

No.

65. Identifier vs keyword

Keywords are reserved words.

66. Is Python case-sensitive?

Yes.

🔹 History
67. Who developed Python?

Guido van Rossum

68. When was Python released?

1991

69. Why was Python created?

To make programming easy and readable.

70. Why name “Python”?

Inspired by a comedy show.

71. Major versions

Python 2 and Python 3.

72. Why Python 2 discontinued?

It became outdated and less secure.

🔹 Output Questions
73. print(True + True) → 2

(True = 1)

74. print(10 and 0 or 5) → 5
75. print(5 > 3 > 2) → True
76. print(bool("")) → False
77. print(10 / 3) → 3.333...
78. print(10 // 3) → 3