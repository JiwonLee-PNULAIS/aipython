Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> A, B = map(int, input("두 정수 A와B를 입력하시오: ").split())
두 정수 A와B를 입력하시오: 1, 3
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    A, B = map(int, input("두 정수 A와B를 입력하시오: ").split())
ValueError: invalid literal for int() with base 10: '1,'
>>> 1 3
SyntaxError: invalid syntax
>>> A, B = map(int, input("두 정수 A와 B를 입력하시오: ").split())
두 정수 A와 B를 입력하시오: 1 3
>>> result = A+B
>>> print("두 정수의 합은:",result)
두 정수의 합은: 4
>>> 