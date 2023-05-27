from UnInformed_search_algorithms.bfs_method import bfs
from UnInformed_search_algorithms.dfs_method import dfs
from Informed_search_algorithms.astar_method import a_star
from UnInformed_search_algorithms.dls_method import dls, ids
from UnInformed_search_algorithms.ucs_method import ucs
from Informed_search_algorithms.greedy_method import greedy, dump_trace

import sys

def read_as_list2D(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        return [[int(i) for i in line.split()] for line in lines[:3]]

def read_as_list(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        return [int(i) for line in lines[:3] for i in line.split()]

def read_as_tuple(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        return tuple([int(i) for line in lines[:3] for i in line.split()])

def read_as_string(file_name):
    with open(file_name, 'r') as f:
        return "".join(f.readlines()[:3])

if __name__ == '__main__':
    # check for correct number of arguments
    if len(sys.argv) < 3:
        print("Usage: expense_8_puzzle.py <start-file> <goal-file> <method> [<dump-flag>]")
        sys.exit()

    # get input arguments
    start_file = sys.argv[1]
    goal_file = sys.argv[2]
    method = sys.argv[3] if len(sys.argv) > 3 else 'astar'
    dump_flag = True if len(sys.argv) > 4 and sys.argv[4].lower() == 'true' else False

    print(f"***** Executing {method} *****")
    # run the algorithm
    # solve the problem using selected method
    if method == 'bfs':                                 #starting the bfs method
        starting_state = read_as_list2D(start_file)     #reading the start file 
        expected_goal= read_as_list2D(goal_file)        #reading the goal file
        bfs(starting_state, expected_goal)
    if method == 'astar':                               #starting astar method  
        starting_state = read_as_tuple(start_file)      #reading the start file
        expected_goal= read_as_tuple(goal_file)         #reading the goal file
        a_star(starting_state, expected_goal)
    if method == 'dfs':                                 #starting dfs method  
        starting_state = read_as_string(start_file)     #reading the start file
        expected_goal = read_as_string(goal_file)       #reading the goal file
        dfs(starting_state, expected_goal)
    if method ==  'ucs':                                #starting ucs method
        starting_state = read_as_list(start_file)       #reading the start file
        expected_goal = read_as_list(goal_file)         #reading the goal file
        ucs(starting_state, expected_goal) 
    if method == 'dls':                                 #starting dls method
        starting_state = read_as_tuple(start_file)      #reading the start file
        expected_goal = read_as_tuple(goal_file)        #reading the goal file
        dls(starting_state, expected_goal, max_depth=12, trace_file="dls_trace.txt")
    if method == 'ids':                                #starting ids method
        starting_state = read_as_tuple(start_file)     #reading the start file
        expected_goal = read_as_tuple(goal_file)       #reading the goal file
        ids(starting_state, expected_goal, max_depth=100, trace_file="ids_trace.txt")
    if method == 'greedy':                             #starting greedy method
        starting_state = "".join(map(str, read_as_list(start_file)))  #reading the start file
        expected_goal = "".join(map(str, read_as_list(goal_file)))    #reading the goal file
        result = greedy(starting_state, expected_goal)
        dump_trace(result)