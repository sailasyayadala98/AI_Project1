from datetime  import datetime

def dls(initial_state, goal, max_depth, trace_file):    #starting dls function
    no_of_nodes_popped ,no_of_nodes_expanded, no_of_nodes_generated , max_fringe_size = 0 ,0,0,0
    visit_node = set()   #initialising visit node as empty set
    fringe = [(initial_state, [], 0)]
    while fringe:
        node, path, cost = fringe.pop()
        no_of_nodes_popped += 1
        visit_node.add(node)
        if node == goal:
            with open(f'{trace_file.split("_")[0]+"_result.txt"}', 'w') as f:
                f.write(f"No of Nodes Popped: {no_of_nodes_popped}\n")
                print(f"No of Nodes Popped: {no_of_nodes_popped}")
                f.write(f"No of Nodes Expanded: {no_of_nodes_expanded}\n")
                print(f"No of Nodes Expanded: {no_of_nodes_expanded}")
                f.write(f"No of Nodes Generated: {no_of_nodes_generated}\n")
                print(f"No of Nodes Generated: {no_of_nodes_generated}")
                f.write(f"Max Fringe Size: {max_fringe_size}\n")
                print(f"Max Fringe Size: {max_fringe_size}")
                f.write(f"Solution Found at depth {len(path)} with cost of {cost}.\n")
                print(f"Solution Found at depth {len(path)} with cost of {cost}.")
                f.write("Steps:\n")
                print("Steps:")
                for step in path:
                    f.write(f"\t{step}\n")
                    print(f"\t{step}")
                print("Dumped File Successfully!")
            return path
        with open(f'{trace_file}_{datetime.now().strftime("%d_%m_%Y_%H_%M_%S")}.txt', 'a+') as file:
            if len(path) < max_depth:
                for successor, action, step_cost in success_move(node, file):
                    if successor not in visit_node:
                        no_of_nodes_generated += 1
                        fringe.append((successor, path + [action], cost + step_cost))
                no_of_nodes_expanded += 1
                max_fringe_size = max(max_fringe_size, len(fringe))
                file.write(f'\n{fringe}')
    return None

def success_move(state, file):   
    empty_index = state.index(0)      # Find the index of the empty cell (represented by 0)
    rows = empty_index // 3
    columns = empty_index % 3
    succ_moves = []
    if rows > 0:
        # Move the tile above the empty cell down
        new_state = list(state)
        new_state[empty_index] = state[empty_index-3]
        new_state[empty_index-3] = 0
        succ_moves.append((tuple(new_state), "Move {} Down".format(state[empty_index-3]), 1))
    if rows < 2:
        # Move the tile below the empty cell up
        new_state = list(state)
        new_state[empty_index] = state[empty_index+3]
        new_state[empty_index+3] = 0
        succ_moves.append((tuple(new_state), "Move {} Up".format(state[empty_index+3]), 1))
    if columns > 0:
        # Move the tile to the left of the empty cell right
        new_state = list(state)
        new_state[empty_index] = state[empty_index-1]
        new_state[empty_index-1] = 0
        succ_moves.append((tuple(new_state), "Move {} Right".format(state[empty_index-1]), 1))
    if columns < 2:
        # Move the tile to the right of the empty cell left
        new_state = list(state)
        new_state[empty_index] = state[empty_index+1]
        new_state[empty_index+1] = 0
        succ_moves.append((tuple(new_state), "Move {} Left".format(state[empty_index+1]), 1))
    file.write(f'\n{succ_moves}')
    return succ_moves

def ids(int_start, goal, max_depth, trace_file):
    no_of_nodes_popped,no_of_nodes_expanded ,no_of_nodes_generated,max_fringe_size= 0,0,0,0
    for depth in range(max_depth):
        with open(trace_file, 'w') as f:
            print(f"Searching at depth {depth}")
            f.write(f"Searching at depth {depth}\n")
            result = dls(int_start, goal, depth, trace_file)
            if result is not None:
                print(f'solution found at depth {depth}')
                f.write(f'solution found at depth {depth}\n')
                return
            else:
                print(f"No solution found at depth {depth}")
                f.write(f"No solution found at depth {depth}\n")
    print(f"Failed to find solution within max depth of {max_depth}")
    return None

# start_state = (2, 3, 6, 1, 0, 7, 4, 8, 5)
# goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
# dls(start_state, goal_state, 12, "dls_trace.txt")
# ids(start_state, goal_state, 100, "ids_trace.txt")