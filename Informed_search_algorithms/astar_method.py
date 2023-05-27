from queue import PriorityQueue
from datetime import datetime

def a_star(initial_state, goal_state):
    def heuristic(init_state):
        distance = 0
        for i in range(len(init_state)):
            if init_state[i] != 0:
                let_k=abs(i // 3 - (init_state[i]-1) // 3)
                let_m=abs(i % 3 - (init_state[i]-1) % 3)
                distance += let_k + let_m
        return distance

    class Node:
        def __init__(self, state, parent=None, move=None, cost=0):
            self.state = state
            self.parent = parent
            self.move = move
            self.cost = cost
            self.heuristic = heuristic(state)  # Compute heuristic value
            if self.parent:
                self.depth = parent.depth + 1
            else:
                self.depth = 0

        def __lt__(self, other):
            return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    start_node = Node(initial_state)

    no_of_nodes_popped ,no_of_nodes_expanded,no_of_nodes_generated, no_of_solution_cost,max_fringe_size = 0,0,0,0,0
    frontier = PriorityQueue()
    frontier.put(start_node)
    explore_node = set()

    while not frontier.empty():
        if frontier.qsize() > max_fringe_size:
            max_fringe_size = frontier.qsize()

        node = frontier.get()
        no_of_nodes_popped += 1

        if node.state == goal_state:
            solution_steps = []
            while node.parent:
                solution_steps.append(node.move)
                node = node.parent
                no_of_solution_cost += node.cost
            solution_steps.reverse()
            solution_depth = len(solution_steps)
            with open("astar_result.txt", "w") as f:
                f.write(f"No of Nodes Popped: {no_of_nodes_popped}\n")
                print(f"No of Nodes Popped: {no_of_nodes_popped}")
                f.write(f"No of Nodes Expanded: {no_of_nodes_expanded}\n")
                print(f"No of Nodes Expanded: {no_of_nodes_expanded}")
                f.write(f"No of Nodes Generated: {no_of_nodes_generated}\n")
                print(f"No of Nodes Generated: {no_of_nodes_generated}")
                f.write(f"Max Fringe Size: {max_fringe_size}\n")
                print(f"Max Fringe Size: {max_fringe_size}")
                f.write(f"Solution Found at depth level {solution_depth} with cost  {no_of_solution_cost}.\n")
                print(f"Solution Found at depth level {solution_depth} with cost  {no_of_solution_cost}.")
                f.write("Steps:\n")
                print("Steps:")
                for step in solution_steps:
                    f.write(f"\t{step}\n")
                    print(f"\t{step}")
                print("Dumped the output results successfully!")
            return
        with open(f'astar_trace_{datetime.now().strftime("%d_%m_%Y_%H_%M")}.txt', 'a+') as file:
            explore_node.add(node.state)
            no_of_nodes_expanded += 1
            for move, state in get_success_astar(node.state, file):
                if state not in explore_node:
                    child = Node(state, parent=node, move=move, cost=node.cost+1)
                    frontier.put(child)
                    no_of_nodes_generated += 1
                file.write(f'\n{explore_node}')
    with open("astar_result.txt", "w") as f:
        f.write("No solution found.")
    return None


def get_success_astar(state, file):
    success_moves = []
    p = state.index(0)
    if p not in [0, 1, 2]:
        new_state = list(state)
        new_state[p], new_state[p-3] = new_state[p-3], new_state[p]
        success_moves.append(("Move {} Down".format(state[p-3]), tuple(new_state)))
    if p not in [6, 7, 8]:
        new_state = list(state)
        new_state[p], new_state[p+3] = new_state[p+3], new_state[p]
        success_moves.append(("Move {} Up".format(state[p+3]), tuple(new_state)))
    if p not in [0, 3, 6]:
        new_state = list(state)
        new_state[p], new_state[p-1] = new_state[p-1], new_state[p]
        success_moves.append(("Move {} Right".format(state[p-1]), tuple(new_state)))
    if p not in [2, 5, 8]:
        new_state = list(state)
        new_state[p], new_state[p+1] = new_state[p+1], new_state[p]
        success_moves.append(("Move {} Left".format(state[p+1]), tuple(new_state)))
    file.write(f'\n{success_moves}\n')
    return success_moves

class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
