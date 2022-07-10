# SWP

### Programming Language:
Python

### Purpose:
This program calculates the distribution of the degrees of seperation in subset of Facebook data. <br>

### Requirements:
* cmath <br>
* numpy <br>

### How it works:
This program reads in a .txt file with Facebook data.<br>
The data represents connections between user as follows: <br>
10 32 <br>
47 29 <br>

Meaning user 10 is friends with user 32, and user 47 is friends with user 29. <br>

The program creates an "adjacency list" out of the data. <br>
Then performs a Breadth First Search (BFS) on the resulting directed graph. <br>

The output of the given data is:<br>
{0: 0.0, 1: 1.1, 2: 16.6, 3: 24.4, 4: 35.9, 5: 15.7, 6: 4.1, 7: 1.9, 8: 0.1, 9: 0, 10: 0}
