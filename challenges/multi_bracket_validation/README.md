# Challenge - Multiple Bracket Validation

**Author**: Stephen Koch
**Version**: 1.0.0

## Overview
In this module, we are writing a function that, when given a string, can determine wither or not brackets are being opened and closed at the proper places. The function returns True or False based on correct bracket usage.

Example:
```
Input string: (){}[]
Output: True
```
```
Input string: ({[hello_world]}){}
Output: True
```
```
Input string: ({)}[]
Output: False
```

## Getting Started
Running tests is straight forward and involves using pytest.

First, make sure that you have python3 installed:
```
$ python3 --version
Python 3.7.5
```
If you do not:
```
$ brew install python
```
You need to have the files locally. Click on the green clone or download button and Download ZIP:

![Click_to_download](../../assets/Click_to_download.png)

Navigate to your command line:
```
MacOS: Press command + space to open up the search feature
Search for "terminal" - This is your default command line on MacOS.
```
In your command line, navigate to this directory:
```
$ cd ~  ##this is your root directory
$ cd Downloads  ##by default: Downloads is a directory inside of your root; and where your file will be downloaded
$ cd python_data_structures_and_algorithims ##and now you are in this directory
```
This module is running tests on given data imputs. Install [pytest](https://docs.pytest.org/en/latest/getting-started.html) to get started:
Installing pytest:
```
$ pip install -U pytest
```
Running tests:
```
$ pytest
```

## Approach & Efficiency
For this module, the goal was to traverse the string that came into the function as input - for loop was used. Then conditionals were set up to check...<br>IF the character is an open bracket THEN add the character to a string of all the open brackets (open_brac variable).<br>IF the character is a closing bracket THEN check the end of the string (open_brac) and if the end of open_brac was the corresponding open bracket, continue the loop and remove the open bracket character from the open_brac string. 

The for loop continues for the length of the string. At the end, if all the conditions are met along the way, one last conditional is checked. If the open_brac string that was storing all the open bracket characters is now empty... that means that all of the brackets were opened and were closed. Only then can the function return True.

The BigO for this function is O(n) for both time and space. The entire input string is traversed each time the function is invoked. The bigger the input, the bigger the space and time.
 
## Solution:
![Multiple_Bracket_Validation](../../assets/multi_bracket_validation.jpeg)

## Change Log
Fri Dec 27 2019 14:06:20<br>Created multi_bracket_validation function. Tested edge cases; functioning as expected.


