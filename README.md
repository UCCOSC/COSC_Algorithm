COSC367
=======

Computational intelligence 


Introduction
In this searcing assignment you apply the search techniques you have learnt in the course to routing problems.

You have a number driverless cabs (agents) scattered across a city. The objective is, to when a customer 
calls, navigate an agent that is closest to the customer, from its current position to the location of 
the customer. The city is a flat rectangular grid with a number of building blocks.

In the first step you have to write a subclass of Graph that represent the map of a city in the form of a graph. 
The map is given in the form of a multiline string of characters. The following shows an example map. 

map_str = """\
+--------+
|       G|
|  XXX   |
|  S X   |
|    X   |
+--------+
"""


The map is always rectangular. We refer to positions in the map by a pair of numbers (row, col) which correspond
to the row and column number of the position. Row numbers start from 0 for the first (topmost) line, 1 for the 
second line, and so on. The column numbers start from 0 for the first (leftmost) position (character) in the line,
1 for the second position, and so on. The city is always surrounded by walls which are represented with characters
'+' or '-' or '|'. For example the position (0,0) is always a '+' (i.e. wall) and so are all other three corners 
of the map. The first and last rows and the first and last columns are '-' and '|' except for the corners which 
are '+'. The building blocks are marked by 'X'.  If a position (cell in the grid) odes not have a building, it is
represented by a ' ' (space) character.

The agents (starting positions) are marked by an 'S'. The location of the customer (goal) position is marked by a
'G'. For simplicity in textual representation, we assume that a starting position and a goal position are never 
the same. There is always one and only one 'G' on the map. There might be zero or more 'S's on the map.

The agent can move in four directions: 'up', 'right', 'down', and 'left' unless there is a building block or wall
in the way. The order of actions is clockwise. For example if from a position all possible moves are possible then
the first arc in the sequence of arcs returned by outgoing_arcs is for going up, then an arc for going right, then
an arc for going down and finally an arc for going left.

AStarFrontier that is appropriate for performing an A* search on a graph. An instance of AStarFrontier together 
with an instance of MapGraph that you wrote in the previous question will be passed to generic_search to find the 
shortest path (if one exist) from the closest agent to the goal node.

a function print_map that takes three parameters: a map string, an AStartFrontier object, and a solution (which is
a sequence of Arc objects that make up a path from a starting position to the goal position) and then prints a map
such that:

the position of the walls, obstacles, agents, and the goal point are all unchanged and they are marked by the same
set of characters as in the original map string; and those free spaces (space characters) that have been expanded 
during the search are marked with a '.' (a period character); and those free spaces (spaces characters) that are 
part of the solution (best path to the goal) are marked with '*' (an asterisk character).
