# DSA-Project 1) Typing Master 2) Rat In Maze
# 1) Typing Master
The project Contains Typing Master:
Objective:
To develop a terminal-based typing test application. The application tests the
user's typing speed by presenting a list of random words from a selected
category and measures metrics like words per minute (WPM).
Prerequisites:
1. Python 3.x installed
2. Basic understanding of file I/O, data structures (list, dictionaries), and JSON
format.
Specifications:
Input:
1. Username for the leaderboard.
2. Option to start the typing test, show the leaderboard, or exit.
Output:
1. A set of random words for the user to type.
2. Typing Metrics: Words Typed, Time Taken, Words Per Minute.
DSA Project Documentation 2
Rules:
1. Users must type the words exactly as shown.
2. Users can quit the game by pressing 'Ctrl + Q' at any time.
Guidelines:
1. On starting, the user is prompted to enter a username.
2. The user then chooses an option to either start the typing test, show the
leaderboard, or exit.
3. Once the test starts, metrics like words typed and WPM are measured.
Code Structure:
update_leaderboard Function: Updates and sorts the leaderboard stored
in a JSON file.
show_leaderboard Function: Displays the leaderboard from the JSON file.
load_words_from_json Function: Loads words from a JSON file into a
Python dictionary.
get_user_input Function: Captures user input from the terminal.
main Function: Contains the main game logic.
Future Perspective:
1. Add more typing categories.
2. Implement a time-based challenge mode

# 2) Rat In Maze

Objective:
To develop a terminal-based application that generates a random maze, finds a path
from the start to the end, and visualizes the maze and path in the terminal.
Prerequisites:
1. Basic understanding of arrays and loops.
2. Familiarity with terminal-based input/output.
Specifications:
Input:
1. Size of the maze ( ).
2. Users choose to either print the path, generate another puzzle, or exit the game.
Output:
1. A visual representation of the generated maze in the terminal.
2D
n ∗ n
DSA Project Documentation 2
2. A visual representation of the path from start to end, if it exists.
Rules:
1. The maze is represented as a array where each cell can be either a wall or
an open space.
2. The top-left corner is the start ( ) and the bottom-right corner is the end ( ).
3. The application should provide options to print the path, generate another
puzzle, or exit the game.
4. The number of random walls should be restricted to be less than or equal to
% of the total cells to increase the likelihood of a solvable maze.
Guidelines:
1. Generate a random maze of size with walls and open spaces.
2. Implement a pathfinding algorithm to find a path from the start to the end.
3. Visualize the maze and the path in the terminal.
4. Provide options to the user for further actions.
Code Structure:
Maze Generation Function: Generates a random maze and returns it as a
array.
Maze Printing Function: Prints the maze in the terminal.
Pathfinding Function: Finds a path from the start to the end using a suitable
algorithm like BFS or DFS.
Path Printing Function: Prints the path in a readable format.
Path Marking Function: Marks the path on the maze for visualization
