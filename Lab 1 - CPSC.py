Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("Hello, world")
Hello, world
print("Welcome to CPSC 207")
Welcome to CPSC 207
print(Hello \nWorld")
      
SyntaxError: unexpected character after line continuation character
print("Hello\nWorld")
      
Hello
World
print("How\nare\nyou?")
      
How
are
you?
print("Today", "is", "Wednesday")
      
Today is Wednesday
print("Today" + "is" + "Wednesday")
      
TodayisWednesday
print("a\nb\nc")
      
a
b
c
print("Hello" + "World")
      
HelloWorld
print("Hello\n" + "\nWorld!")
      
Hello

World!
print("123\n45\n6")
      
123
45
6
1+2*3
      
7
(1+2)*3
      
9
7/3
      
2.3333333333333335
7//3
      
2
7%3
...       
1
>>> 22/4
...       
5.5
>>> 22//4
...       
5
>>> 22%4
...       
2
>>> 3**2
...       
9
>>> 2**3
...       
8
>>> (4+3)//2
...       
3
>>> 6%2
...       
0
>>> 1+2*(3**4)
...       
163
>>> print("2+2", "=" , 2+2)
...       
2+2 = 4
>>> print("2+2" + "=" 2+2)
...       
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("2+2=", 2+2)
...       
2+2= 4

>>> print("50 pounds is", 50*0.453592, "Kilograms")
...       
50 pounds is 22.6796 Kilograms
