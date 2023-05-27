from queue import Queue
from datetime import datetime

def bfs(initial_start, goal):                          #starting the bfs search function
    start = tuple(map(tuple, initial_start))
    goal = tuple(map(tuple, goal))
    queue_state = Queue()
    queue_state.put(start)
    visit_node = set()
    parent = {}
    depth = {start: 0}
    cost = {start: 0}
    max_fringe_size = 1
    result = []
    
    while not queue_state.empty():
        node = queue_state.get()
        visit_node.add(node)            #add the node into visited node
        
        if node == goal:
            set_path = []              #taking path as empty list
            while node in parent:
                set_path.append(node)
                node = parent[node]
            set_path.append(start)
            set_path.reverse() 
            with open("bfs_result.txt", "a+") as file:     #writing down the output file
                file.write(f"\nNo of Nodes Popped: {len(visit_node)}\n")
                print(f"No of Nodes Popped: {len(visit_node)}")
                file.write(f"No of Nodes Expanded: {len(visit_node)-1}\n")
                print(f"No of Nodes Expanded: {len(visit_node)-1}")
                file.write(f"No of Nodes Generated: {len(parent)}\n")
                print(f"No of Nodes Generated: {len(parent)}")
                file.write(f"Max Fringe Size: {max_fringe_size}\n")
                print(f"Max Fringe Size: {max_fringe_size}")
                file.write(f"Solution Found at depth level {depth[goal]} with cost {cost[goal]}.\n")
                print((f"Solution Found at depth level {depth[goal]} with cost {cost[goal]}."))
                file.write("Steps:\n")
                print('Steps:')
                for step in result:
                    # res.append(step[0])
                    move_cost, move_name = step[1], step[2]
                    file.write(f"\tMove {move_cost} {move_name}\n")
                    print(f"\tMove {move_cost} {move_name}")
                file.write(f'\n{set_path}')
                # file.write("Stages:\n")
                # for s in res:
                #     file.write(f"\t{s}\n")
                print("Result Found Successfully!")
            return
        
        for move in moves(node):
            if move[0] not in visit_node:
                queue_state.put(move[0])
                visit_node.add(move[0])
                parent[move[0]] = node
                depth[move[0]] = depth[node] + 1
                cost[move[0]] = cost[node] + move[1]
                max_fringe_size = max(max_fringe_size, queue_state.qsize())
                result.append(move)
    print("No solution found.")
    
    
def moves(node):                  #defining a function for moves to reach the expected goal 
    moves = []
    with open(f'bfs_trace_{datetime.now().strftime("%d_%m_%Y_%H_%M")}.txt', 'a') as file:
        let_row, let_col = get_blank_pos(node)
        for dr, dc, move_name in [(-1, 0, "Up"), (1, 0, "Down"), (0, -1, "Left"), (0, 1, "Right")]:
            newest_row, newest_col = let_row + dr, let_col + dc
            if 0 <= newest_row < len(node) and 0 <= newest_col < len(node[0]):
                new_node = swaping_positions(node, let_row, let_col, newest_row, newest_col)
                move_cost = node[newest_row][newest_col]
                moves.append((new_node, move_cost, move_name))
                file.write(f'\n{moves}')
    return moves


def get_blank_pos(node):
    for r, rows in enumerate(node):
        for c, value in enumerate(rows):
            if value == 0:
                return r, c
    raise ValueError("Invalid node: no initial tile found")


def swaping_positions(node, row1, col1, row2, col2):
    node = [list(i) for i in node]
    node[row1][col1], node[row2][col2] = node[row2][col2], node[row1][col1]
    return tuple(map(tuple, node))
    

# Example usage
# start = [[2, 3, 6], [1, 0, 7], [4, 8, 5]]
# goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
# bfs(start, goal)