# scam-call-checker
A Python command-line tool to check and report scam phone numbers, helping users identify fraudulent calls and protect themselves from scams.

## Description

This project addresses a major problem in the ever-growing technological industry that is scamming. Today, many people, primarily senior citizens
are victim to such problems, and the scammers are making a living out of it, a report from global anti scam alliance states that over $1.03 trillion
has been stolen by scammers in 2024 alone , scamming has been a major issue globally in countries like india there are thousands of separate companies operating illegally just for the sake of scamming and the one's who are doing these are living luxury out of stolen money that a person saved or worked for years

This program allows the user to check and report a scam number additionally it gives out general information about a scam number like why is it dangerous and recommend actions for the user, it uses a MOCKAPI key to store and retrieve data. this program at it's most this is just a prototype soon there will be a GUI to make the process easier and many other feature like email checking , improved suggestions etc will be added soon and everything will be updated in the project's github repository

Currently the program offers only a four common category option for reporting a new number, a new system will be implemented shortly that has a better way to categorize the scams

## Features

- Checking scam numbers
- Report new scam numbers
- Explanation about the scam
- Recommendation based on the scam

## How to run

1. Step 1 - Download the file and its requirement from the github page
2. Step 2 - Find the downloaded file location
3. Step 3 - Open terminal
4. Step 4 - Navigate to the folder of the downloaded location
5. Step 5 - Run python project.py

## Project Files

**project.py**: The main core python file it contains all the functions of the project including the scam number checker
**test_project.py**: This is a test python file for the main program it checks whether the mains program works as intended
**requirements.txt**: This file contains the list of module required for the main program to work check if you have the required modules installed if not install it with : pip install {module_name}

## Functions

### `main()`
the main function integrates all other functions this is very useful when only under a certain condition a function should take place and in general it is common practice to use the main() function for integration

### `validate_phone(phone)`
the validate phone function as the name suggests validates a phone number so if a user enters a wrong one it catches it currently it does not use regex instead it checks for the length of the phone number , does it start with + and does the number any other character other than numbers

### `validate_category(category)`
the validate category validates a category among the four predefinded one's so if a user enters a unknown category or a false one the function catches it from the given category

### `check(phone)`
the check function checks if a number is a scam it returns the category of the scam and the number of reports on the specific number if found it is reported else if the number hasn't been reported it returns the number is safe and if the number is not in the database it return not found.

### `explain_risk(category , reports ,risk)`
the explain risk expects three inputs using those it explains the dangerosness of the scam, using the category it gets a predefined explantion of the ways that scammers may use to scam in that specific category, using the risk level it determines the riskness of the number to the user and in the end it combines all of these into a sentence and prints it in the end it also contains a part of give advise function[modified like that to safely test the function] that is for the recommended actions to the user

### `give_advise(risk)`
the give advise function expects risk level as a input and gives a recommended action by it for the sake of easier testing the give advise function instead of housing all of recommended actions in itself has been split and mostly contained in the explain risk function

### `add_entry(phone)`
the add entry function adds a new scam number to the database , first it checks if the phone number already exists in the database if yes it updates the number of reports by 1 if not it creates a entry contains all the information about the scam like the category , reports etc

## Design choice

I chose to use MOCKAPI key as it offered a free alternative that allowed the database to be shared among users and also simulated real world  scenario , The validate functions (validate_phone and validate_category) could have been combined into one funcyion , but i chose to split them for easier testing and readability. The check function was designed to accept international phone numbers rather than specific countries or group of countries as scamming is a global issue.
