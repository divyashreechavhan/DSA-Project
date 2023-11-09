#include <iostream>
#include <vector>
#include <random>
#include <ctime>

using namespace std;

const char WALL_CHAR = '▓';
const char OPEN_CHAR = '◌';
const char PATH_CHAR = '◍';
const char START_CHAR = 'S';
const char END_CHAR = 'E';

// Define maze size
const int N = 10; // Change this as needed

// Function to generate a random maze
vector<vector<char>> generateMaze() {
    vector<vector<char>> maze(N, vector<char>(N, OPEN_CHAR));
    // Randomly place walls
    int numWalls = N * N * 0.3; // Adjust the percentage as needed
    while (numWalls > 0) {
        int x = rand() % N;
        int y = rand() % N;
        if (maze[x][y] == OPEN_CHAR) {
            maze[x][y] = WALL_CHAR;
            numWalls--;
        }
    }
    // Place start and end points
    maze[0][0] = START_CHAR;
    maze[N - 1][N - 1] = END_CHAR;
    return maze;
}

// Function to print the maze
void printMaze(const vector<vector<char>>& maze) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << maze[i][j] << " ";
        }
        cout << endl;
    }
}

// Function to find a path using depth-first search (DFS)
bool findPath(vector<vector<char>>& maze, int x, int y) {
    if (x < 0 || x >= N || y < 0 || y >= N || maze[x][y] == WALL_CHAR || maze[x][y] == PATH_CHAR) {
        return false;
    }
    if (maze[x][y] == END_CHAR) {
        return true;
    }
    maze[x][y] = PATH_CHAR;
    if (findPath(maze, x + 1, y) || findPath(maze, x - 1, y) || findPath(maze, x, y + 1) || findPath(maze, x, y - 1)) {
        return true;
    }
    maze[x][y] = OPEN_CHAR;
    return false;
}

// Function to mark and print the path
void markAndPrintPath(vector<vector<char>>& maze) {
    if (findPath(maze, 0, 0)) {
        cout << "Path found:" << endl;
        printMaze(maze);
    } else {
        cout << "No path found." << endl;
    }
}

int main() {
    srand(time(nullptr)); // Initialize random seed
    vector<vector<char>> maze = generateMaze();
    cout << "Generated Maze:" << endl;
    printMaze(maze);
    markAndPrintPath(maze);
    return 0;
}
