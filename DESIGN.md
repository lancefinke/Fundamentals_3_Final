# Design Document

Documentation explaning the design features of the Car Catalogue

## Introduction

The Car Catalog records data on a collection of cars. It keeps tracks of each cars' make, model, year, color, mileage, price, transmission type, and also allows user to give each car a unique ID number to make searching easier. A verification system will also be implemented. This will verify that whether a car model exist or not. If a car is verified, that means that the make, model and year exist with 100% certanity. If it is not verified, the car might still exist, but it is not confirmed with 100% certaninty it does. to do this, the cataolog will utilize an API and see if the make, mode, and year of the car can be found within the API database. 

## Data Structures

2 data structures will be implemented in this catalog: an array and a dictionary. The array will store all of the cars and the dictionary will story the different quantities of makes, models, and years. If a user wants to find out how many cars were made in 2020, or how many Fords there are saved in the catalog, the dictionary will store these values. Most of the algorithms in this catalog will perform operations on the array of cars

## Search Algorithms

There will be two types of search algorithms: one that finds a specific car based on an ID number and another that returns a list of cars that are of a certain make, model, or year. The first search method mentioned will use binary search to make the run time as efficent as possible. It is named `findID` and takes 4 parameters. The second search method will use linear search becuase it has to check every car in the array and see if it matches a certain specification. It's current name is `findSpec` and  it takes in an `int` parameter. The int paramter is used in a `match`/`case` block that makes the function compatible for all 3 uses.

## Sorting Algorithm

The sorting algorithm for the catalog will be quick search. It will sort the cars based on ID number and will automatically be called before the binary search function. The quick search algorithm is relatively simple to implement and is much more efficient than selection search with an average run time of O(n log n). The function is named `sortByID` and takes in a list parameter.

## User Inferface

The Console based user interface will contain a numbered list of commands the user can execute by typing in numbers. All of the instrucitons will be clearly listed out in the console. an information or help tab will be avaliable to users and upon execution, it will print out a menu containing information about the catalog.

## Persistant Storage

To store the collection data I will use a JSON file. The JSON file will consist of an array of different objects, each one containing the data for s specific car. Upon loading the python file, all of the data from the JSON file will be loades in the data structures. I chose a JSON file becuase it is very easy to parse JSON files in python and the Object notation makes data easy to store and filter through.

## Exception Handling

To handle exceptions, I will use try and except blocks. When an error is detected, the user will be notified and they will be told to re-eneter the value. To allow for re-enetering values, most methods will implement while loops that break when a correct value is submitted. Users will also be given the option to quit and return to the main menu if they wish to do so. The user will also be notifed if the car did not pass the verification test.

