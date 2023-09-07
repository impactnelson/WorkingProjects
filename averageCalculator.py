# Average Calculator

''' Overview

This Python script defines a function called `avg` that calculates the average of a variable number of numerical values.

## Usage

To use the `avg` function, follow these steps:

1. Import the function in your Python script or interactive session.
   
   ```python
   from average_calculator import avg

Here's an example of how to use the avg function:

from average_calculator import avg

values = [15, 25, 35, 45]
result = averageCalculator(*values)
print(result)  # Output: 30.0
In this example, we calculate the average of a list of values by unpacking the list using the * operator and passing it to the avg function.

AUTHOR:
NCHOPEREU NELSON
EMAIL: nghonelson14@gmail.com


This README file provides a brief overview of the project, instructions for usage, an example,
and sections for authorship and licensing information. You can customize it further to suit your project's specific needs.


'''

#Source Code
def averageCalculator(*scores):
    scores = int(input('Enter Your scores:\n\n'))
    #scores = int(scores)
    totalScores = 0
    for score in scores:
        totalScores += score
    return totalScores / len(scores)
#averageCalculator()
print(averageCalculator(2,4,5,6))
























