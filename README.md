
# Maze Solver using A* Algorithm




This project implements an AI-powered solution to solve randomly generated mazes using the A* algorithm, which combines the benefits of Dijkstra's algorithm and greedy best-first search to efficiently determine the shortest path from the start to the destination while avoiding obstacles and dead ends.


## Introduction
Navigating complex mazes, whether physical or digital, presents a significant challenge. The goal of this project is to build an intelligent solver capable of efficiently navigating randomly generated mazes by finding the shortest path between a starting point and a destination.

The A* algorithm is used in this project because of its efficiency and optimality in pathfinding. It estimates the cost from the current position to the goal using a heuristic function (Manhattan distance) and prioritizes the most promising paths. This makes it ideal for navigating mazes of various structures and complexities, avoiding unnecessary exploration of dead ends and obstacles.
## Key Objectives

- Implement the A* algorithm to solve randomly generated mazes.
- Ensure the AI solver determines the shortest and most efficient path between the start and end points.
- Avoid obstacles, dead ends, and efficiently manage complex maze structures.
## Methodology 

The project utilizes the A* algorithm, a popular AI search method that evaluates the cost of moving to the goal (h-score) and the cost to reach the current node (g-score). A priority queue manages the exploration of the maze, with cells being explored based on their f-score (the sum of g-score and h-score).

The heuristic function uses Manhattan distance, which calculates the absolute differences in the x and y coordinates of two cells, guiding the algorithm towards the goal efficiently. The program uses the *pyamaze* library to generate random mazes and implement the A* algorithm to find the optimal path.






## Screenshots
![1](https://github.com/user-attachments/assets/d6a313a2-a8de-48e1-a477-1ba0e232ff33)

![maze_img](https://github.com/user-attachments/assets/c6d74bd4-41dc-41cc-955f-9547cdecede8)


## Conclusion
The A* algorithm is highly effective for solving maze problems due to its ability to prioritize promising paths while ensuring optimal and efficient navigation. By intelligently managing both the cost of reaching nodes and estimating the cost to the goal, the A* algorithm delivers an optimal solution for complex and randomly generated mazes. This implementation demonstrates the algorithm's potential for solving real-world navigation problems, providing a solid foundation for more advanced AI applications in fields such as robotics, gaming, and logistics.
