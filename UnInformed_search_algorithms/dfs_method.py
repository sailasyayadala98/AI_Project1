from datetime import datetime

class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost


def dfs(initial_state, goal_state):                              #starting the dfs method
    # Initialize the frontier with the initial state
    frontier = [Node(initial_state)]                             #frontier is initialised
    explored = set()                                             #an empty set is assigned to explored
    max_fringe_size = 1                                          #taking fringe size 1 as max 
    no_of_nodes_popped , no_of_nodes_expanded ,no_of_nodes_generated,solution  = 0,0,1, None

    while frontier:
        # Select the deepest node from the frontier
        node = frontier.pop()                                  #poping out the deepest node from the frontier
      
        if node.state == goal_state:                            # Checking if the goal state is reached
            solution = node
            break
       
        explored.add(node.state)                                # Adding the node to the explored set after visiting

        
        for action, state in expanded(node.state):             # Expanding  the node and add its children to the frontier
            no_of_nodes_generated += 1
            if state not in explored:
                child = Node(state, node, action, node.cost + 1)
                frontier.append(child)

        
        no_of_nodes_expanded += 1
        no_of_nodes_popped += 1
        max_fringe_size = max(max_fringe_size, len(frontier))

    # Writing down the trace to file
    with open("dfs_result.txt", "w") as f:
        f.write("No of Nodes Popped: {}\n".format(no_of_nodes_popped))
        print("NO of Nodes Popped: {}".format(no_of_nodes_popped))
        f.write("No of Nodes Expanded: {}\n".format(no_of_nodes_expanded))
        print("No of Nodes Expanded: {}".format(no_of_nodes_expanded))
        f.write("No of Nodes Generated: {}\n".format(no_of_nodes_generated))
        print("No of Nodes Generated: {}".format(no_of_nodes_generated))
        f.write("Max Fringe Size: {}\n".format(max_fringe_size))
        print("Max Fringe Size: {}".format(max_fringe_size))

        if solution:
            f.write("Solution Found at depth level {} with cost  {}.\n".format(solution.cost, solution.cost))
            print("Solution Found at depth level {} with cost {}.".format(solution.cost, solution.cost))
            f.write("Steps:\n")
            print('Steps:')
            empty_list= []
            while solution.parent is not None:
                sol_state_split=solution.state.split('\n')
                empty_list.append("\tMove {} {}\n".format(solution.action[2], [[int(x) for x in row.split()] for row in sol_state_split]))
                print("\tMove {} {}".format(solution.action[2], [[int(x) for x in row.split()] for row in sol_state_split]))
                solution = solution.parent
            empty_list.reverse()
            for steps in empty_list:
                f.write(steps)
            print("Dumped the output results sucessfully!")
        else:
            f.write("No solution is found.")

    return solution


def expanded(state):
    # Convert the state string to a list of integers
    split_state =state.split('\n')
    state = [[int(y) for y in row.split()] for row in split_state]

    # Find the position of the empty space (0)
    p, q = next((p, q) for p, row in enumerate(state) for q, x in enumerate(row) if x == 0)

    # Generate the possible moves
    possible_moves = []
    if p > 0: possible_moves.append((-1, 0, 'up'))  # Move empty space up
    if q > 0: possible_moves.append((0, -1, 'left'))  # Move empty space left
    if p < 2: possible_moves.append((1, 0, 'down'))   # Move empty space down
    if q < 2: possible_moves.append((0, 1, 'right'))   # Move empty space right

    # Apply the moves and generate the new states
    states = []
    with open(f'dfs_trace_{datetime.now().strftime("%d_%m_%Y_%H_%M")}.txt', 'a+') as file:
        for dp, dq, mov in possible_moves:
            new_state = [row.copy() for row in state]
            new_state[p][q], new_state[p+dp][q+dq] = new_state[p+dp][q+dq], new_state[p][q]
            states.append('\n'.join(' '.join(str(x) for x in row) for row in new_state))
            file.write(f'\n{(new_state[p][q], new_state[p+dp][q+dq], state, new_state, (dp, dq), mov, state)}')
    # Return the list of (action, state) pairs

    return [((dp, dq, mov), new_state) for (dp, dq, mov), new_state in zip(possible_moves, states)]



# Example usage:
# initial_state = "2 3 6\n1 0 7\n4 8 5" 
# goal_state = "1 2 3\n4 5 6\n7 8 0"
# dfs(initial_state, goal_state)

