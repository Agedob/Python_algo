# First 
    Write a program that compares two lists and prints a message depending on if the inputs are identical or not.

    Your program should be able to accept and compare two lists: list_one and list_two. If both lists are 
    identical print "The lists are the same". If they are not identical print "The lists are not the same." 
    Try the following test cases for lists one and two:


    list_one = [1,2,5,6,2]
    list_two = [1,2,5,6,2]

    list_one = [1,2,5,6,5]
    list_two = [1,2,5,6,5,3]

    list_one = [1,2,5,6,5,16]
    list_two = [1,2,5,6,5]

    list_one = ['celery','carrots','bread','milk']
    list_two = ['celery','carrots','bread','cream']

# Second 

    Write a program that takes a list of strings and a string containing a single character, 
    and prints a new list of all the strings containing that character.

    Here's an example:


    # input
    word_list = ['hello','world','my','name','is','Anna']
    char = 'o'
    # output
    new_list = ['hello','world']

# Third

    Write a program that prints all the prime numbers and all the perfect squares for all numbers between 100 and 100000.

    For all numbers between 100 and 100000 test that number for whether it is prime or a perfect square. If it is a prime number, print "Foo". If it is a perfect square, print "Bar". If it is neither, print "FooBar". Do not use the python math library for this exercise. For example, if the number you are evaluating is 25, you will have to figure out if it is a perfect square. It is, so print "Bar".

        PRIME: Any integer other than 0 or ± 1 that is not divisible without remainder by any other integers except ± 1 and ± the integer itself.
            101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199.

        SQUARE: When a number or integer (not a fraction) is multiplied by itself, the resultant is called a 'Square Number'. For example, 3 multiplied by 3 is equal to 3-squared or 3 x 3 = 32. So, basically, the exponential form of multiplication of a number or integer by itself is called a square number.
            121, 144, 169 and 196

    This assignment is extra challenging! Try pair programming and pulling up a whiteboard.

# Fourth 

    1)Odd/Even:
    Create a function called odd_even that counts from 1 to 2000.   
    As your loop executes have your program print the number of that 
    iteration and specify whether it's an odd or even number.

    2)Create a function called 'multiply' that iterates through each 
    value in a list (e.g. a = [2, 4, 10, 16]) 
    and returns a list where each value has been multiplied by 5.

    3)Write a function that takes the multiply function call as an 
    argument. Your new function should return the multiplied list as
    a two-dimensional list. Each internal list should contain the 1's 
    times the number in the original list. 

# Fifth

    Write a function that generates ten scores between 60 and 100. 
    Each time a score is generated, your function should display what
    the grade is for a particular score. Here is the grade table:

    Score: 60 - 69; Grade - D
    Score: 70 - 79; Grade - C
    Score: 80 - 89; Grade - B
    Score: 90 - 100; Grade - A

# Sixth

    Write a function that simulates tossing a coin 5,000 times. 
    Your function should print how many times the head/tail appears.

# Seventh

    Create a function called draw_stars() that takes a list of numbers and prints out *.

# Eighth

    Create a dictionary containing some information about yourself.
    The keys should include name, age, country of birth, favorite language.
    Write a function that will print something like the following as it executes
            My name is Anna
            My age is 101
            My country of birth is The United States
            My favorite language is Python
    There are two steps to this process, building a dictionary and then gathering all
    the data from it. Write a function that can take in and print out any dictionary keys and values.

    Note: The majority of data we will manipulate as web developers will be hashed in
    a dictionary using key-value pairs. Repeat this assignment a few times to really get
    the hang of unpacking dictionaries, as it's a very common requirement of any web application.

# Ninth 

    Given the following list:
    students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    Create a program that outputs:
    Michael Jordan
    John Rosales
    Mark Guillen
    KB Tonel

    Now, given the following dictionary:
    users = {
    'Students': [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
    'Instructors': [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
    }
    Create a program that prints the following format (including number of characters in each combined name):
    Students
    1 - MICHAEL JORDAN - 13
    2 - JOHN ROSALES - 11
    3 - MARK GUILLEN - 11
    4 - KB TONEL - 7
    Instructors
    1 - MICHAEL CHOI - 11
    2 - MARTIN PURYEAR - 13

# Tenth 

    Write a function that takes in a dictionary and 
    returns a list of tuples where the first tuple
    item is the key and the second is the value.
    #function output
    [("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]

