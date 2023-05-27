from queue import PriorityQueue
from datetime import datetime

def get_successors(state):
    success_moves = []
    # get the position of the blank tile
    initial_position = state.index(0)
    # get the initial row and column of the intial tile
    initial_row = initial_position // 3
    initial_col = initial_position % 3
    with open(f'ucs_trace_{datetime.now().strftime("%d_%m_%Y_%H_%M")}.txt', 'a+') as file:
        # generate success move by swapping the initial tile with its neighboring tiles
        for moving_row, moving_col, action in [(-1, 0, 'Up'), (1, 0, 'Down'), (0, -1, 'Left'), (0, 1, 'Right')]:
            new_row = initial_row + moving_row
            new_col = initial_col + moving_col
            
            if new_row < 0 or new_row >= 3 or new_col < 0 or new_col >= 3:
                # the new position is out of bounds, so skip this success move
                continue
            
            # swap the initial tile with the neighbor tile
            new_pos = new_row * 3 + new_col
            new_state = state[:]
            new_state[initial_position], new_state[new_pos] = new_state[new_pos], new_state[initial_position]
            
            # calculate the cost of the move as the value of the tile being moved
            cost = new_state[initial_row]
            # add the success move to the list
            success_moves.append((action, new_state, cost, initial_position))
            file.write(f"\n{success_moves}")
    return success_moves

def ucs(start_state, goal_state):                                    #starting ucs method
    no_of_nodes_popped,no_of_nodes_expanded,no_of_nodes_generated,max_fringe_size= 0,0,0,0   #assigning required values to 0
    
    visit_node = set()                     #took visited as empty set      
    frontier = PriorityQueue()
    frontier.put((0, [start_state, [], 0, []])) 
    
    while not frontier.empty():
        current_node = frontier.get()[1]
        current_state, current_path, current_cost, current_position = current_node
        no_of_nodes_popped += 1
        
        if current_state == goal_state:              #writing down the results
            with open('ucs_result.txt', 'w') as f:
                f.write(f'No of Nodes Popped: {no_of_nodes_popped}\n')
                print(f'No of Nodes Popped: {no_of_nodes_popped}')
                f.write(f'No of Nodes Expanded: {no_of_nodes_expanded}\n')
                print(f'No of Nodes Expanded: {no_of_nodes_expanded}')
                f.write(f'No of Nodes Generated: {no_of_nodes_generated}\n')
                print(f'No of Nodes Generated: {no_of_nodes_generated}')
                f.write(f'Max Fringe Size: {max_fringe_size}\n')
                print(f'Max Fringe Size: {max_fringe_size}')
                f.write(f'Solution Found at depth level of {len(current_path)} with cost {current_cost}.\n')
                print(f'Solution Found at depth level of  {len(current_path)} with cost {current_cost}.')
                f.write('Steps:\n')
                print('Steps:')
                for step, position in zip(current_path, current_position):
                    f.write(f'\tMove {position} {step}\n')
                    print(f'\tMove {position} {step}')
                print("Dumped the output results sucessfully!")
            return current_path
        
        visit_node.add(tuple(current_state))       #adding current node into the visited node set
        no_of_nodes_expanded += 1
        
        for work_done, new_state, cost_value, position in get_successors(current_state):
            if tuple(new_state) not in visit_node:
                no_of_nodes_generated += 1
                newest_path = current_path + [work_done]
                newest_cost = current_cost + cost_value
                newest_pos = current_position + [position]
                frontier.put((newest_cost, [new_state, newest_path, newest_cost, newest_pos]))
        
        if frontier.qsize() > max_fringe_size:
            max_fringe_size = frontier.qsize()
    
    return None

# example usage
# start_state = [2, 3, 6, 1, 0, 7, 4, 8, 5]
# goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
# ucs(start_state, goal_state)
