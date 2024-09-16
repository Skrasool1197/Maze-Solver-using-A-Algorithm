from pyamaze import maze, agent, textLabel
from queue import PriorityQueue

# Heuristic function to calculate Manhattan distance
def heuristic(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2)

# A* Algorithm implementation
def a_star(maze_instance):
    start_position = (maze_instance.rows, maze_instance.cols)
    g_cost = {cell: float('inf') for cell in maze_instance.grid}
    g_cost[start_position] = 0
    f_cost = {cell: float('inf') for cell in maze_instance.grid}
    f_cost[start_position] = heuristic(start_position, (1, 1))

    open_cells = PriorityQueue()
    open_cells.put((heuristic(start_position, (1, 1)), heuristic(start_position, (1, 1)), start_position))
    came_from = {}

    while not open_cells.empty():
        current_cell = open_cells.get()[2]
        if current_cell == (1, 1):  # Reached the goal
            break
        for direction in 'ESNW':
            if maze_instance.maze_map[current_cell][direction] == True:
                if direction == 'E':
                    next_cell = (current_cell[0], current_cell[1] + 1)
                if direction == 'W':
                    next_cell = (current_cell[0], current_cell[1] - 1)
                if direction == 'N':
                    next_cell = (current_cell[0] - 1, current_cell[1])
                if direction == 'S':
                    next_cell = (current_cell[0] + 1, current_cell[1])

                temp_g_cost = g_cost[current_cell] + 1
                temp_f_cost = temp_g_cost + heuristic(next_cell, (1, 1))

                if temp_f_cost < f_cost[next_cell]:
                    g_cost[next_cell] = temp_g_cost
                    f_cost[next_cell] = temp_f_cost
                    open_cells.put((temp_f_cost, heuristic(next_cell, (1, 1)), next_cell))
                    came_from[next_cell] = current_cell

    path = {}
    cell = (1, 1)
    while cell != start_position:
        path[came_from[cell]] = cell
        cell = came_from[cell]
    return path

if __name__ == '__main__':
    num_rows = int(input("Enter the number of rows: "))
    num_cols = int(input("Enter the number of columns: "))
    maze_instance = maze(num_rows, num_cols)
    maze_instance.CreateMaze()
    solution_path = a_star(maze_instance)

    # Creating agent with footprints, smaller arrows, and different colors
    bot = agent(maze_instance, footprints=True, shape='arrow', color='blue', filled=True)
    maze_instance.tracePath({bot: solution_path}, delay=100)
    
    # Adding the label to show the path length
    label = textLabel(maze_instance, 'A* Path Length', len(solution_path) + 1)

    maze_instance.run()
