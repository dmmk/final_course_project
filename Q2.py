"""
Uniform Cost Search Implementation using PriorityQueue

Map and input taken from
http://www.massey.ac.nz/~mjjohnso/notes/59302/l04.html

Author: Jayesh Chandrapal
Version: 1.0
https://rextester.com/GDQAJ78015
"""
import sys
import time
import queue as Q
import re


graph = {}


def multiple_city_search(graph, start, goals):
    path = ''
    temppath = ''
    m = 0
    tempgoals = goals.copy()
    for goal in goals:
        tempstart = start
        #tempgoal = goal
        cost = 200  
        print("now starting from " + start)
        print (tempgoals)
        path = path +" "+ temppath  
        if start in tempgoals:
            tempgoals.remove(start)
        for tempgoal in tempgoals:
            if tempstart != tempgoal:
                print('calling search with '+ tempstart +' and '+ tempgoal )
                mp = search(graph, tempstart, tempgoal) 
                print(mp)
                #m = re.search(', Cost = (.+?)', mp)
                if mp is not None:
                    m = int(''.join(filter(str.isdigit, mp)))
                    print (m)
                if m is not 0 and m < cost:
                    cost = m
                    start = tempgoal
                    temppath = mp
    print( 'Path is -----' + path +" "+ temppath)
def search(graph, start, end):
    if start not in graph:
        raise TypeError(str(start) + ' not found in graph !')
        return
    if end not in graph:
        raise TypeError(str(end) + ' not found in graph !')
        return
    
    queue = Q.PriorityQueue()
    queue.put((0, [start]))
    
    while not queue.empty():
        node = queue.get()
        current = node[1][len(node[1]) - 1]
        
        if end in node[1]:
            #print("Path found: " + str(node[1]) + ", Cost = " + str(node[0]))
            return "Path found: " + str(node[1]) + ", Cost = " + str(node[0])
            #break
        
        cost = node[0]
        for neighbor in graph[current]:
            temp = node[1][:]
            temp.append(neighbor)
            queue.put((cost + graph[current][neighbor], temp))
        
def readGraph(line):
#    print ('read graph')
#    lines = 78 #int( input() )
#    print(lines)
#    graph = {}
    
#    for line in range(lines):

        print (line)
        #line = input()
            
        tokens = line.split(':')
        node = tokens[0]
        graph[node] = {}
        
        for i in range(1, len(tokens) - 1, 2):
            # print(node, tokens[i], tokens[i + 1])
            # graph.addEdge(node, tokens[i], int(tokens[i + 1]))
            graph[node][tokens[i]] = int(tokens[i + 1])
#    return graph
        return

def main(start, goal):
    mf = open("ucs.txt", "r+")
    print("File to read: ", mf.name)

    for file_line in mf:
        # Print single line
        #print(file_line)
        readGraph(file_line) 
    #graph = readGraph()
    print (graph)
    #search(graph, 'Addis Ababa', 'Gondar')

    #start_time = time.time()
    print (search(graph, start, goal))
    #end_time = time.time()
    #print("Elapsed time: ", end_time - start_time) 
    
    #multiple_city_search(graph, 'Addis Ababa', ['Axum', 'Gondar', 'Lalibella', 'Babile', 'Jimma', 'Bale', 'Sof Oumer', 'Arba Minchi'])
    multiple_city_search(graph, 'Addis Ababa', [ 'Babile', 'Jimma', 'Bale',  'Arba Minchi'])

    
if __name__ == "__main__":
    
      main(sys.argv[1], sys.argv[2])
 #    main('Addis Ababa', 'Gondar')
    