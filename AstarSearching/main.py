from search import *

class MapGraph(Graph):
	def __init__(self, graph):
		self.row = 0;self.col = 0;tmp_estimate = 0;self.graph = graph
		self.x_list = []
		self.starting_list = []
		self.goal_nodes = []
		self.all_possible_position = []

		graph_array = self.graph.strip().splitlines()
		for i in range(len(graph_array)):
			graph_array[i] = list(graph_array[i].strip())
			
		self.row = len(graph_array)
		self.col = len(graph_array[0])
		for i in range(self.row):
			for j in range(self.col):
				if graph_array[i][j] in [' ', 'S', 'G']:
					self.all_possible_position.append((i, j))
				if graph_array[i][j] in ['G', 'g']:
					self.goal_nodes.append((i, j))
				if graph_array[i][j] in ['S', 's']:
					self.starting_list.append((i, j))
				if graph_array[i][j] in ['X', 'x']:
					self.x_list.append((i, j))

	def starting_nodes(self):
		"""Returns (via a generator) a sequece of starting nodes."""
		for node in self.starting_list: yield node
		
	def is_goal(self, node):
		"""Returns true if the given node is a goal node."""
		#return node in self.goal_nodes
		if (len(self.goal_nodes) > 0):
			return (node == self.goal_nodes[0])
		else:
			return False

	def outgoing_arcs(self, node):
		pos = ''; tail = node; head = ''; cost = 0
		UP = (tail[0]-1,tail[1]); RIGHT = (tail[0],tail[1]+1)
		DOWN = (tail[0]+1,tail[1]); LEFT = (tail[0],tail[1]-1)
		if (UP in self.all_possible_position) and (UP not in self.x_list):
			pos = 'up'; cost = 1; head = (UP)
			yield Arc(tail, head, pos, cost)
		if (RIGHT in self.all_possible_position) and (RIGHT not in self.x_list):
			pos = 'right'; cost = 1; head = (RIGHT)
			yield Arc(tail, head, pos, cost)
		if (DOWN in self.all_possible_position) and (DOWN not in self.x_list):
			pos = 'down'; cost = 1; head = (DOWN)
			yield Arc(tail, head, pos, cost)
		if (LEFT in self.all_possible_position) and (LEFT not in self.x_list):
			pos = 'left'; cost = 1; head = (LEFT)
			yield Arc(tail, head, pos, cost)

	def estimated_cost_to_goal(self, node):
        #Manhattan distance
		tmp = list(self.goal_nodes)
		if len(tmp) != 0:
			goal = self.goal_nodes[0]
			distance = abs(goal[0] - node[0]) + abs(goal[1] - node[1])
			return distance
		else:
			return False


class AStarFrontier(Frontier):
	def __init__(self,graph):
		"""The constructor takes no argument. It initialises the
		container to an empty list."""
		self.container = []
		self.graph = graph
		self.startnode = list(graph.starting_nodes())
		if len(self.startnode) != 0:
			self.node = sorted(graph.starting_nodes())[0]
			
		self.visited = []
		
	def add(self, path):
		if(path[-1].head not in self.visited):
			self.container.append(path)
		
	def __iter__(self):
		while len(self.container) != 0:
			count = 0
			lowest = 999999
			for i in range(len(self.container)):
				self.g = 0
				for a in range(len(self.container[i])):
					self.g += self.container[i][a].cost
				self.node = self.container[i][-1].head
				self.huristics = self.graph.estimated_cost_to_goal(self.node)
				self.f = self.huristics+self.g
				if (self.f < lowest):
					count = i;
					lowest = self.f
			remove_node = self.container.pop(count)
			if (remove_node[-1].head not in self.visited):
				self.visited.append(remove_node[-1].head)
				yield remove_node
			
def print_map(map_str, frontier, solution):
	x=0;y=1;m=[]; length_line=0; tmp_estimate=0; node=(1,5)
	local_map = map_str; tmp_map = list(local_map); result = ''

	tmp_map = map_str.strip().splitlines()
	for i in range(len(tmp_map)):
		tmp_map[i] = list(tmp_map[i].strip())	

	for i in map_str:
		m.append(i)
		if (i == '\n' and tmp_estimate == 0):
			tmp_estimate = 1; length_line=len(m)-1

	for i in frontier.visited:
		#~ print (tmp_map)
		if tmp_map[i[0]][i[1]] == ' ' and tmp_map[i[0]][i[1]] != 'S' and tmp_map[i[0]][i[1]] != 'G':
			tmp_map[i[0]][i[1]] = '.'

	if solution != None:
		for i in solution:
			node = i.tail
			if node != None:
				if tmp_map[node[0]][node[1]] != 'S' and tmp_map[node[0]][node[1]] != 'G':
					tmp_map[node[0]][node[1]] = '*'
	for r in range(len(tmp_map)):
		for c in range(len(tmp_map[0])):
			print(tmp_map[r][c],end='')
		print()
		
def main():
    ###################path_test#######################
    map_str = """\
    +-------+
    |     XG|
    |X XXX  |
    | S     |
    +-------+
    """

    graph = MapGraph(map_str)

    print("Starting nodes:", sorted(graph.starting_nodes()))
    print("Outgoing arcs (available actions) at the start:")
    for s in graph.starting_nodes():
        for arc in graph.outgoing_arcs(s):
            print ("  " + str(arc))

    node = (1,1)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print ("  " + str(arc))

    node = (1,7)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print ("  " + str(arc))
    
    map_str = """\
    +--+
    |GS|
    +--+
    """

    graph = MapGraph(map_str)

    print("Starting nodes:", sorted(graph.starting_nodes()))
    print("Outgoing arcs (available actions) at the start:")
    for start in graph.starting_nodes():
        for arc in graph.outgoing_arcs(start):
            print ("  " + str(arc))

    # Although the robot can never be in wall positions, just to test the
    # graph logic:
    node = (0,0)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print ("  " + str(arc))

    node = (1,1)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print ("  " + str(arc))

    map_str = """\
    +----+
    |    |
    | SX |
    | X G|
    +----+
    """

    graph = MapGraph(map_str)

    print("Starting nodes:", sorted(graph.starting_nodes()))
    print("Available actions at the start:")
    for s in graph.starting_nodes():
        for arc in graph.outgoing_arcs(s):
            print ("  " + arc.label)
    map_str = """\
    +------+
    |S    S|
    |  GXXX|
    |S     |
    +------+
    """

    graph = MapGraph(map_str)
    print("Starting nodes:", sorted(graph.starting_nodes()))

    map_str = """\
    +----+
    | X  |
    |XSX |
    | X G|
    +----+
    """

    graph = MapGraph(map_str)

    print("Starting nodes:", sorted(graph.starting_nodes()))
    print("Available actions at the start:")
    for s in graph.starting_nodes():
        for arc in graph.outgoing_arcs(s):
            print ("  " + arc.label)

    ##################AStarFrontier test################
    map_str = """\
    +-------+
    |     XG|
    |X XXX  |
    | S     |
    +-------+
    """

    map_graph = MapGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = generic_search(map_graph, frontier)
    print_actions(solution)
    
    
    map_str = """\
    +--+
    |GS|
    +--+
    """
    map_graph = MapGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = generic_search(map_graph, frontier)
    print_actions(solution)
    
    map_str = """\
    +----+
    |    |
    | SX |
    | X G|
    +----+
    """

    map_graph = MapGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = generic_search(map_graph, frontier)
    print_actions(solution)
    map_str = """\
    +----+
    | X  |
    |XSX |
    | X G|
    +----+
    """

    map_graph = MapGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = generic_search(map_graph, frontier)
    print_actions(solution)

    ##################print_map test####################
    map_str = """\
    +-------+
    |     XG|
    |X XXX  |
    | S     |
    +-------+
    """
    map_graph = MapGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = generic_search(map_graph, frontier)
    print_map(map_str, frontier, solution)
    
    map_str = """\
    +--+
    |GS|
    +--+
    """
    map_graph = MapGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = generic_search(map_graph, frontier)
    print_map(map_str, frontier, solution)

    map_str = """\
    +----+
    |    |
    | SX |
    | X G|
    +----+
    """

    map_graph = MapGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = generic_search(map_graph, frontier)
    print_map(map_str, frontier, solution)

    map_str = """\
    +----+
    | X  |
    |XSX |
    | X G|
    +----+
    """

    map_graph = MapGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = generic_search(map_graph, frontier)
    print_map(map_str, frontier, solution)
    
    map_str = """\
    +-------+
    |S X S  |
    |  X X  |
    |     G |
    +-------+
    """

    map_graph = MapGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = generic_search(map_graph, frontier)
    print_map(map_str, frontier, solution)

if __name__ == "__main__":
		main()
