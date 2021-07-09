# -*- coding: utf-8 -*-
"""
Created on Sat May 30 18:32:09 2020

@Author: Wong Jun Kang
@StudentID: 29801036
"""
from math import inf
from queue import Queue
import heapq

class Graph:
    """ 
    A class for the construction of an undirected graph
    """
    def __init__(self, gfile):
        """
        Constructor of undirected Graph object.
        
        @Arguments              :   gfile, a text file representing an undirected graph.
                                
        @Precondition           :   gfile must only represent graphs that are connected
                                    and simple
                                    
        @Postcondition          :   a connected, undirected and simple graph based
                                    on gfile is created
                                    
        @Time complexity        :   Best and Worst O(V+E), where:
                                    V is the number of vertices in the gfile(graph).
                                    E is thse number of edges in the gfile(graph).
                                    Worst case can also be represented
                                    as O(V^2)for densed graph when E is densed(V^2).
                                    (omit the complexity of file opening)
                                    
        @Space complexity       :   O(V+E), where:
                                    V is the number of vertices in the graph.
                                    E is the number of edges in the graph.
                                    With O(V^2) as upperbound.
        
        @Aux space complexity   :   O(1)
        """
        self.vertex_count= 0
        self.vertices = []
        self.extract_file(gfile)
        
    def __str__(self):
        """
        String output of graph (in gfile).
        @Postcondition          :   graph is converted into a string representation of graph.
                                    
        @Time complexity        :   Best and Worst O(V+E), where:
                                    V is the number of vertices in the graph.
                                    E is the number of edges in the graph.
                                    
        @Space complexity       :   O(V+E), where:
                                    V is the number of vertices in the graph.
                                    E is the number of edges in the graph.
                                    With O(V^2) as upperbound.
        
        @Aux space complexity   :   O(V+E), where:
                                    V is the number of vertices in the graph.
                                    E is the number of edges in the graph.
                                    With O(V^2) as upperbound.
        """
        return_string = ""
        for vertex in self.vertices:
            return_string += "Vertex " + str(vertex) + "\n"
        return return_string
    
    def __len__(self):
        """
        This function return the length of the graph (gfile)/ vertex_count.
        @return:                :   self.vertices, the number of vertex in the
                                    graph(gfile).
        @Time complexity        :   O(1)
        
        @Space complexity       :   O(1)
        
        @Aux space complexity   :   O(1)
        """
        return self.vertex_count

    def extract_file(self, gfile):
        """
        extract gfile and create an undirected graph based on gfile representation. 
        
        @Arguments              :   gfile, a text file representing an undirected graph.
                                
        @Precondition           :   gfile must only represent graphs that are connected
                                    and simple
                                    
        @Postcondition          :   a connected, undirected and simple graph based
                                    on gfile is created
                                    
        @Time complexity        :   Best and Worst O(V+E), where:
                                    V is the number of vertices in the gfile(graph).
                                    E is the number of edges in the gfile(graph).
                                    Worst case can also be represented
                                    as O(V^2)for densed graph when E is densed(V^2).
                                    (omit the complexity of file opening)
                                    
        @Space complexity       :   O(V+E), where:
                                    V is the number of vertices in the graph.
                                    E is the number of edges in the graph.
                                    With O(V^2) as upperbound.
        
        @Aux space complexity   :   O(1)
        """
        with open(gfile) as file:
            # retrieve number of vertices and create an array to store vertices.
            self.vertex_count = int(file.readline())
            self.vertices = [Vertex(i) for i in range(len(self))]

            # for all the edges
            for line in file:
                edge = line.split()
                u, v, w = int(edge[0]), int(edge[1]), int(edge[2])
                # create an 2 edge objects for 2 different directions (undirected).
                e = Edge(u, v, w)       
                e2 = Edge(v, u, w)
                
                # Add a new edge to vertex at position u/ v
                self.vertices[u].add_edge(e) 
                self.vertices[v].add_edge(e2)
                
                
    def shallowest_spanning_tree(self):
        """
       This function returns a tuple containing two items. The first item is the
       vertex ID of the root which gives the shallowest spanning tree. The second
       item is an integer, representing the height of the shallowest spanning tree.
                        
                                    
        @Postcondition          :   a connected, undirected and simple graph based
                                    on gfile is created
                                    
        @Time complexity        :   O(V(V+E))
                                    Best case O(V^2)
                                    Worst case O(V^3), where:
                                    V is the number of vertices in the gfile(graph).
                               
        @Space complexity       :   O(V), where:
                                    V is the number of vertices in the graph.
        
        @Aux space complexity   :   O(V), where:
                                    V is the number of vertices in the graph. 
        
        @Return                 :   a tuple containing two items.
                                    The first item is the vertex ID of the root 
                                    which gives the shallowest spanning tree.
                                    
                                    The second item is an integer, representing 
                                    the height of the shallowest spanning tree.                
        """
        minimum, ret_id = len(self), None
        
        for vertex in self.vertices:
            vertex_id = vertex.id
            # calculate the longest shortest paths of current vertex
            k = self.bfs_longest_shortest_paths(vertex_id)
            # get minimum from all the longest_shortest_paths of all vertices.
            if k < minimum: 
                minimum, ret_id = k, vertex_id
                
        return ret_id, minimum
                
    
    def bfs_longest_shortest_paths(self, source):
        """
        This function returns the longest path from all the shortest paths
        returned by a bfs.
        
        @Arguments              :   Source, the source vertex to calculate the
                                    longest shortest path from
                                
        @Precondition           :   Source, must be a valid vertex from graph gfile.
                                    
        @Postcondition          :   The longest path from all shortest paths from source
                                    of graph(gfile) is returned.
                                    
        @Time complexity        :   Best and Worst O(V+E), where:
                                    V is the number of vertices in the gfile(graph).
                                    E is the number of edges in the gfile(graph).
                                    Worst case can also be represented
                                    as O(V^2)for densed graph when E is densed(V^2).
                                    
        @Space complexity       :   O(V), where:
                                    V is the number of vertices in the graph.
        
        @Aux space complexity   :   O(V), where:
                                    V is the number of vertices in the graph.
        
        @Return                 :   maximum, the longest path of all the shorest paths.
        """
        dist = [inf] * len(self)
        queue = Queue(len(self))
        queue.put(source)       # push source into a queue
        dist[source] = 0        # source to source is 0 distance
        maximum = 0
        
        # while queue still contain vertex.
        while not queue.empty():
            u = queue.get()
            vertex = self.vertices[u]
            
            # loop through all neighbouring vertices
            for edge in vertex.edges:
                v = edge.v
                
                # update shortest paths if infinity is detected
                if dist[v] == inf:
                    dist[v] = dist[u] + 1
                    queue.put(v)
                    
                    # record maximum from all shortest paths
                    if dist[v] > maximum:
                        maximum = dist[v]
        return maximum
    
    
    
    def shortest_errand(self, home, destination, ice_locs, ice_cream_locs):
        """
        Given a home, destination, a list of ice_locs and a list of ice cream locs
        shortest arrand will return a shortest path and its visited vertices
        from home to destination that passes through ice first then ice cream locs.
        
        @Arguments              :   home, the source vertex to start from
                                    destination, the vertex to reach/ to get
                                    shortest distance of
                                    ice_locs, list of vertices that has ice_locs
                                    ice_cream_locs, list of vertices that has ice_cream_locs
                                
        @Precondition           :   ice_locs and ice_cream locs must not be empty
                                    provided if graph is not empty.
                                    
        @Postcondition          :   graph is not modified
                                    a shortest path from home to destination 
                                    and the its visited vertices that passes 
                                    through ice first then ice cream locs is returned.
                                    
        @Time complexity        :   Best and Worst O(ElogV), where:
                                    V is the number of vertices in the gfile(graph).
                                    E is the number of edges in the gfile(graph).
                                    Worst case can also be represented
                                    as O(V^2logV)for densed graph when E is densed(V^2).
                                    
        @Space complexity       :   Best and Worst O(V+E), where:
                                    V is the number of vertices in the gfile(graph).
                                    E is the number of edges in the gfile(graph).
                                    Worst case can also be represented
                                    as O(V^2)for densed graph when E is densed(V^2).
        
        @Aux space complexity   :   Best and Worst O(V+E), where:
                                    V is the number of vertices in the gfile(graph).
                                    E is the number of edges in the gfile(graph).
                                    Worst case can also be represented
                                    as O(V^2)for densed graph when E is densed(V^2).
        
        @Return                 :   a shortest path and its visited vertices
                                    from home to destination that passes through
                                    ice first then ice cream locs.
        """
        # create copies of gfile graph with where each graphs have a different 
        # vertices in all graphs has different vertex id.
        if(len(self)) == 0:
            return None, []
        
        # 1 vertex: meaning home, destination, ice_locs and ice_cream_locs are
        # located at the same spot, at vertex 1.
        if(len(self)) == 1:
            return 0, [0]
        
        # avoid modifying original graph, hence, use deep copy.
        graph1 = self.duplicate_graph(self.vertices, 0)
        graph2 = self.duplicate_graph(self.vertices, len(self))
        graph3 = self.duplicate_graph(self.vertices, len(self) * 2)
        
        # equals length of graph1/ graph2/ graph3
        length = len(self) 
        
        # link graph1 and 2 with ice_locs and graph1 and 3 with ice_cream_locs
        self.connect_graph(ice_locs, graph1, graph2) 
        self.connect_graph(ice_cream_locs, graph2, graph3) 
        
        # run dijstra on the connected graphs, and return distance and predecessor list.
        dist, pred = self.dijkstra_multigraph(graph1, graph2, graph3, home)
        index = (length * 2) + destination  # get destination in the 3rd graph
        
        pred_output = []
        cur_index = index
        adj_index = None
        
        # back tracking pred_output.
        while cur_index != home:
            if(cur_index % length != adj_index):
                visited_index = cur_index % length
                pred_output.append(visited_index)
                adj_index = visited_index
            cur_index = pred[cur_index]
        pred_output.append(home)
        
        return dist[index], pred_output[::-1]
    
    def duplicate_graph(self, graph, start):
        """
        Given a graph, duplicate graph will return another graph containing the 
        same edges and vertices with vertex_id + len(graph) and edges of edge + len(graph).
        
        @Arguments              :   graph, graph to be copied.
                                
        @Precondition           :   graph must be represented in a list of vertices.
                                    
        @Postcondition          :   graph is not modified
                                    a new duplicated graph is returned.
                                    
        @Time complexity        :   Best and Worst O(V+E), where:
                                    V is the number of vertices in the gfile(graph).
                                    E is the number of edges in the gfile(graph).
                                    Worst case can also be represented
                                    as O(V^2)for densed graph when E is densed(V^2)..
                                    
        @Space complexity       :   Best and Worst O(V+E), where:
                                    V is the number of vertices in the gfile(graph).
                                    E is the number of edges in the gfile(graph).
                                    Worst case can also be represented
                                    as O(V^2)for densed graph when E is densed(V^2).
        
        @Aux space complexity   :   Best and Worst O(V+E), where:
                                    V is the number of vertices in the gfile(graph).
                                    E is the number of edges in the gfile(graph).
                                    Worst case can also be represented
                                    as O(V^2)for densed graph when E is densed(V^2).
        
        @Return                 :   new_graph, a new duplicated graph with different vertex_id
                                    but same % id.
        """
        # ice_locs stores location vertex id of ice
        l = len(graph)
        end = start + l
        new_graph = [Vertex(i) for i in range(start, end)]
        for vertex in graph:
            for edge in vertex.edges:
                u, v, w = edge.u + start, edge.v + start, edge.w
                # add edge into new graph.
                new_graph[u % l].add_edge(Edge(u, v, w))
        return new_graph

      
    def connect_graph(self, link_vertices, graph1, graph2):
        """
        Given a list of link vertices, this function will Link graph1 with graph2
        via link vertices of weight 0.
        
        @Arguments              :   graph1, graph to be updated with new edges
                                    graph2, graph to be updated with new edges
                                
        @Precondition           :   graph must be represented in a list of vertices.
                                    
        @Postcondition          :   graph1 and graph2 is modified
                                    graph1 is linked with graph2
                                    
        @Time complexity        :   Best and Worst O(n), where:
                                    n is the number of vertices in link vertices
                                    to be linked.
                                    
        @Space complexity       :   Best and Worst O(V+E), where:
                                    V is the number of vertices in the gfile(graph).
                                    E is the number of edges in the gfile(graph).
                                    Worst case can also be represented
                                    as O(V^2)for densed graph when E is densed(V^2).
        
        
        @Aux space complexity   :   O(1)
        
        """
        # Loop through given vertex_id (based on graph1) in link vertices.
        for vertex_id in link_vertices:
            u  = vertex_id                      # vertex_id of graph 1
            v  = graph2[vertex_id].id           # vertex_id of graph 2
            
            # "u" will always be valid, provided link_vertices is based on a valid
            # self.vertices vertex, hence no mod is required.
            graph1[u].add_edge(Edge(u, v, 0))   
            graph2[v % len(graph2)].add_edge(Edge(v, u, 0))
    
            
    
    def dijkstra_multigraph(self, arr1, arr2, arr3, s):
        """
        Given 3 different graphs and a source, this function will calculate the
        shortest path from source to all other vertices in all 3 graphs.
        
        @Arguments              :   arr1, graph to find shortest path on.
                                    arr2, graph to find shortest path on.
                                    arr3, graph to find shortest path on.
                                
        @Precondition           :   All three graphs (arr1, arr2, arr3) must contain
                                    the sam number of vertices and same % vertex id
                                    at their corresponding position.
                                    
        @Postcondition          :   The shortest path to all nodes in the 3 graphs is returned.
                                    The pred list containing their predecessor is returned.
                                    
        @Time complexity        :   Best and Worst O(ElogV), where:
                                    V is the number of vertices in the gfile(graph).
                                    E is the number of edges in the gfile(graph).
                                    Worst case can also be represented
                                    as O(V^2logV)for densed graph when E is densed(V^2).
                                    
        @Space complexity       :   Best and Worst O(V+E), where:
                                    V is the number of vertices in the gfile(graph).
                                    E is the number of edges in the gfile(graph).
                                    Worst case can also be represented
                                    as O(V^2)for densed graph when E is densed(V^2).
        
        @Aux space complexity   :   O(V), where: 
                                    V is the number of vertices in the gfile(graph).
        
        @Return                 :   dist, a list of distances indicating the shortest
                                    distance to each of the correspinding vertices.
                                    
                                    pred, a list of indices indicating the predecessor
                                    of each node that build up the shortest path.
        """
        length = len(arr1)
        l = length * 3      # total length of 3 graphs.
        # create distance list and pred list to output for3 graphs
        dist = [inf] * l    
        pred = [0] * l
        dist[s] = 0
        q = []
        # push source and its distance(0) into a minheap (ordered by distance)
        heapq.heappush(q, (dist[s], s))
        
        # While there is still vertex in queue (will loop through v times)
        # which v is the number of vertices in the graph.
        while len(q) > 0:
            key, u = heapq.heappop(q)
            if dist[u] <= key:      # skip out of date entry
                if u < l*1/3:       # vertex from first graph
                    vertex = arr1[u]
                elif u < l*2/3:     # vertex from second graph
                    vertex = arr2[u%length]
                else:               # vertex from third graph
                    vertex = arr3[u%length]         
                
                for edge in vertex.edges:
                    # relaxation
                    v, w = edge.v, edge.w
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        heapq.heappush(q, (dist[v], v))
                        pred[v] = u
        return dist, pred
    

class Vertex:
    """A class to create vertex for a graph"""
    def __init__(self, vertex_id):
        """
        Constructor of Vertex object.
        
        @Arguments              :   vertex_id, id to identify each vertex from other vertices.
                                    
        @Postcondition          :   a vertex is constructed.
                                    
        @Time complexity        :   O(1)
                                   
        @Space complexity       :   O(1)
        
        @Aux Space complexity   :   O(1)
        """
        self.id = vertex_id
        self.edges = []
    
    
    def add_edge(self, e):
        """
        This method append a new edge into the edge list
        @Arguments              :   e, edge to be added into edges list.
                                   
        @Time complexity        :   O(1)
                                   
        @Space complexity       :   O(1)
        
        @Aux Space complexity   :   O(1)
        """
        self.edges.append(e)

    
    def __str__(self):
        """
        String output of a vertex.
                                   
        @Time complexity        :   O(e), where e is the number of edges in each edge list.
                                   
        @Space complexity       :   O(e), where e is the number of edges in each edge list.
        
        @Aux Space complexity   :   O(e), where e is the number of edges in each edge list.
        """
        ret = str(self.id)
        for edge in self.edges:
            ret = ret + "\n  " + str(edge)
        return ret
    

class Edge:
    """
    A class to create edges for a vertex
    """
    def __init__(self, u, v, w):
        """
        Constructor of Edge object.
        
        @Arguments              :   u, the "from" vertex
                                    v, the "to" vertex
                                    w, the weight of the edge.
                                    
        @Postcondition          :   an Edge is constructed.
                                    
        @Time complexity        :   O(1)
                                   
        @Space complexity       :   O(1)
        
        @Aux Space complexity   :   O(1)
        """
        self.u = u # from
        self.v = v # to
        self.w = w # weight
    
    def __str__(self):
        """
        String output of an edge
                                   
        @Time complexity        :   O(1)
                                  
        @Space complexity       :   O(1)
        
        @Aux Space complexity   :   O(1)
        """
        return str(self.u) + "," + str(self.v) + "," + str(self.w)
    
        
        