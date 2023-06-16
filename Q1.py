#import queue
import sys
import time

# Using a Python dictionary to act as an adjacency list
graph = {
'Addis Ababa': set(['Adama', 'Ambo', 'Debre Berhan']),
'Adama': set(['Matahara', 'Asella', 'Batu', 'Addis Ababa']), 
'Ambo': set(['Wolkite', 'Addis Ababa', 'Nekemte']), 
'Debre Berhan': set(['Addis Ababa', 'Debre Sina']), 
'Matahara': set(['Adama', 'Awash']), 
'Asella': set(['Adama', 'Assasa']), 
'Batu': set(['Adama', 'Buta Jirra', 'Shashamene']), 
'Wolkite': set(['Ambo', 'Worabe', 'Jimma']), 
'Nekemte': set(['Ambo', 'Bedelle', 'Gimbi']), 
'Debre Sina': set(['Debre Berhan', 'Kemise', 'Debre Markos']), 
'Awash': set(['Chiro', 'Gobi Rasu', 'Matahara']), 
'Assasa': set(['Asella', 'Dodolla']), 
'Buta Jirra': set(['Batu', 'Worabe']), 
'Shashamene': set(['Batu', 'Hawassa', 'Dodolla', 'Hossana']), 
'Worabe': set(['Wolkite', 'Hossana', 'Buta Jirra']), 
'Jimma': set(['Wolkite', 'Bonga', 'Bedelle']), 
'Bedelle': set(['Nekemte', 'Gore', 'Jimma']), 
'Gimbi': set(['Nekemte', 'Dambidollo']), 
'Kemise': set(['Debre Sina', 'Dessie']), 
'Debre Markos': set(['Debre Sina', 'Finote Selam']),
'Chiro': set(['Awash', 'Dire Dawa']), 
'Gobi Rasu': set(['Awash', 'Samara']), 
'Dodolla': set(['Assasa', 'Shashamene', 'Bale']), 
'Hawassa': set(['Shashamene', 'Dilla']), 
'Hossana': set(['Shashamene', 'Worabe', 'Wolaita Sodo']), 
'Bonga': set(['Jimma', 'Dawro', 'Tepi', 'Mizan Teferi']), 
'Gore': set(['Tepi', 'Gambella', 'Bedelle']), 
'Dambidollo': set(['Gimbi', 'Assosa', 'Gambella']), 
'Dessie': set(['Kemise', 'Woldia']), 
'Finote Selam': set(['Debre Markos', 'Bahirdar', 'Injibara']), 
'Dire Dawa': set([ 'Chiro', 'Harar']), 
'Samara': set([ 'Gobi Rasu', 'Fanti Rasu', 'Alamata', 'Woldia']),
'Bale': set(['Liben', 'Dodolla', 'Goba', 'Sof Oumer']), 
'Dilla': set(['Hawassa', 'Bulehora']), 
'Wolaita Sodo': set(['Arba Minchi', 'Dawro', 'Hossana']), 
'Dawro': set([ 'Bonga', 'Basketo', 'Wolaita Sodo']), 
'Tepi': set(['Gore', 'Bonga', 'Mizan Teferi']), 
'Mizan Teferi': set(['Tepi', 'Bonga', 'Basketo']), 
'Gambella': set(['Gore', 'Dambidollo']), 
'Assosa': set(['Dambidollo', 'Metekel']), 
'Woldia': set(['Dessie', 'Lalibella', 'Samara', 'Alamata']),
'Bahirdar': set(['Finote Selam', 'Injibara', 'Metekel', 'Azezo', 'Debre Tabor']), 
'Injibara': set(['Bahirdar', 'Finote Selam']), 
'Harar': set([ 'Dire Dawa', 'Babile']), 
'Fanti Rasu': set(['Samara', 'Kilbet Rasu']), 
'Alamata': set(['Samara', 'Woldia', 'Mekelle', 'Sekota']), 
'Liben': set(['Bale']), 
'Goba': set(['Bale', 'Sof Oumer', 'Dega Habur']), 
'Sof Oumer': set(['Goba', 'Bale', 'Kebri Dehar']), 
'Bulehora': set([ 'Dilla', 'Yabello']), 
'Arba Minchi': set(['Wolaita Sodo', 'Konso', 'Basketo']), 
'Basketo': set([ 'Arba Minchi', 'Dawro', 'Mizan Teferi', 'Benchi Maji']), 
'Metekel': set([ 'Assosa', 'Bahirdar']),
'Lalibella': set(['Woldia', 'Debre Tabor', 'Sekota']),
'Debre Tabor': set(['Lalibella', 'Bahirdar']), 
'Azezo': set(['Gondar', 'Bahirdar', 'Metema']), 
'Babile': set([ 'Harar', 'Jigjiga']), 
'Kilbet Rasu': set(['Fanti Rasu' ]), 
'Mekelle': set(['Alamata', 'Adwa', 'Adigrat', 'Sekota']), 
'Sekota': set(['Alamata', 'Mekelle', 'Lalibella']), 
'Dega Habur': set(['Goba', 'Jigjiga', 'Kebri Dehar']), 
'Kebri Dehar': set(['Gode', 'Sof Oumer', 'Dega Habur', 'Werdez']), 
'Yabello': set([ 'Bulehora', 'Konso', 'Moyale']), 
'Konso': set(['Arba Minchi', 'Yabello']), 
'Benchi Maji': set([ 'Basketo']), 
'Gondar': set([ 'Azezo', 'Metema', 'Debarke']),
'Metema': set([ 'Azezo', 'Gondar']),  
'Jigjiga': set([ 'Babile', 'Dega Habur']), 
'Adwa': set([ 'Mekelle', 'Axum', 'Adigrat']),
'Adigrat': set([ 'Mekelle', 'Adwa']), 
'Gode': set([ 'Dollo', 'Kebri Dehar' ]), 
'Werdez': set([ 'Kebri Dehar']), 
'Moyale': set([ 'Yabello']), 
'Debarke': set([ 'Gondar', 'Shire']), 
'Axum': set(['Shire', 'Adwa']), 
'Dollo': set([ 'Gode']), 
'Shire': set([ 'Axum', 'Humera', 'Debarke']),
'Humera': set([ 'Shire', 'Gondar'])
}


def dfs(g, v, goal, explored, path_so_far):
    """ Returns path from v to goal in g as a string (Hack) """
    explored.add(v)
    if v == goal: 
        return path_so_far + " " + v
    for w in g[v]:
        if w not in explored:
            p = dfs(g, w, goal, explored, path_so_far + " " + v)
            if p: 
                return p
    return ""

'''
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
                break
            else:
                stack.append((next, path + [next]))
    return path 
'''
#https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/
# finds shortest path between 2 nodes of a graph using BFS

def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]
 
    # return path if start is goal
    if start == goal:
        return "That was easy! Start = goal"
 
    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path
 
            # mark node as explored
            explored.append(node)
 
    # in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist :("
 


#print(dfs(graph, 'Addis Ababa', 'Harar', set(), ""))

#print ("Called with a para :" +sys.argv[1] + " " + sys.argv[2]+ " "+ sys.argv[3])

if sys.argv[3] == "DFS":
    start_time = time.time()
    print(dfs(graph, sys.argv[1],sys.argv[2],set(),""))
    end_time = time.time()
    print("Elapsed time: ", end_time - start_time) 
elif sys.argv[3] == "BFS":
    start_time = time.time()    
    print(bfs_shortest_path(graph, sys.argv[1],sys.argv[2]))
    end_time = time.time()
    print("Elapsed time: ", end_time - start_time) 
else:
    print ("not implemented")     


