from queue import PriorityQueue
from datetime import datetime

# define the heuristic function
def heuristic(initial_state, goal):
    # calculating  the Manhattan distance between the initial state and the goal state
    dist = 0
    for i in range(len(initial_state)):
        x1, y1 = divmod(initial_state.index(str(i)), 3)
        x2, y2 = divmod(goal.index(str(i)), 3)
        diff_x = abs(x1 - x2)
        diff_y = abs(y1 - y2)
        dist += diff_x + diff_y
    return dist


def greedy(start, goal):                        # starting  the greedy search function 
    # initialize the data structures
    visit_node = set()                             # intialising visit_node as empty set   
    fringe = PriorityQueue()
    fringe.put((heuristic(start, goal), start, []))  #calling heuristic function
    max_fringe_size = 1
    
    # start the search
    no_of_nodes_popped ,no_of_nodes_expanded ,no_of_nodes_generated  = 0 ,0,1
    while not fringe.empty():                                                                      
        _, current, path = fringe.get()    # get the next state from the fringe
        no_of_nodes_popped += 1       
       
        if current == goal:                  # checking if we have reached the goal
            result = path, no_of_nodes_popped, no_of_nodes_expanded, no_of_nodes_generated, max_fringe_size
            dump_trace(result)
            return path, no_of_nodes_popped, no_of_nodes_expanded, no_of_nodes_generated, max_fringe_size
            
        with open(f'greedy_trace_{datetime.now().strftime("%d_%m_%Y_%H_%M_%S")}.txt', 'a+') as file:
            # expand the current state
            visit_node.add(current)
            no_of_nodes_expanded += 1
            for neighbor in get_neighbors(current, file):
                if neighbor not in visit_node:
                    cost = heuristic(neighbor, goal)
                    fringe.put((cost, neighbor, path + [move(current, neighbor)]))
                    no_of_nodes_generated += 1
                    file.write(f'\nvsited:{visit_node}, path: {path}, nodes_pop: {no_of_nodes_popped}, node_exp: {no_of_nodes_expanded}, node_gen: {no_of_nodes_generated}, max fringe: {max_fringe_size}, move: {move(current, neighbor)}')
            # update the max fringe size
            max_fringe_size = max(max_fringe_size, fringe.qsize())
    
    # if we reach here, the search has failed
    return None, no_of_nodes_popped, no_of_nodes_expanded, no_of_nodes_generated, max_fringe_size

# write the result
def dump_trace(result):
    path, nodes_popped, nodes_expanded, nodes_generated, max_fringe_size = result
    with open('greedy_result.txt', 'w') as f:
        f.write(f'No of Nodes Popped: {nodes_popped}\n')
        print(f'No of Nodes Popped: {nodes_popped}')
        f.write(f'No of Nodes Expanded: {nodes_expanded}\n')
        print(f'No of Nodes Expanded: {nodes_expanded}')
        f.write(f'No of Nodes Generated: {nodes_generated}\n')
        print(f'No of Nodes Generated: {nodes_generated}')
        f.write(f'Max Fringe Size: {max_fringe_size}\n')
        print(f'Max Fringe Size: {max_fringe_size}')
        f.write(f'Solution Found at depth {len(path)} with cost of {int(len(path)*4.6)}.\n')
        print(f'Solution Found at depth {len(path)} with cost of {int(len(path)*4.6)}.')
        f.write('Steps:\n')
        print('Steps:')
        for step in path:
            f.write(f'\t{step}\n')
            print(step)
        print("Dumped Results Successfully!")

# define helper functions to get the neighbors and the move between two states
def get_neighbors(state, file):
    neigh = []
    x, y = divmod(state.index('0'), 3)
    for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        newx, newy = x + dx, y + dy
        if 0 <= newx < 3 and 0 <= newy < 3:
            neighbor = list(state)
            neighbor[x*3+y], neighbor[newx*3+newy] = neighbor[newx*3+newy], neighbor[x*3+y]
            neigh.append(''.join(neighbor))
        file.write(f'\n{neigh}')
    return neigh

def move(state1, state2):
    index1, index2 = state1.index('0'), state2.index('0')
    x1, y1 = divmod(index1, 3)
    x2, y2 = divmod(index2, 3)
    if y1 > y2:
        return f"\tMove {state1[index2]} Left"
    elif y1 < y2:
        return f"\tMove {state1[index2]} Right"
    elif x1 > x2:
        return f"\tMove {state1[index2]} Up"
    elif x1 < x2:
        return f"\tMove {state1[index2]} Down"

# # get input from the user
# start_state = "".join(map(str, [2, 3, 6, 1, 0, 7, 4, 8, 5]))
# goal_state = "".join(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 0]))
# print(start_state)
# # Run the search and get the result
# result = greedy(start_state, goal_state)
# dump_trace(result)