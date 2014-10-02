from csp import *
from itertools import *

def generate_and_test(cs):
	result = []; dic = cs.domains
	tmp_value = []; tmp_key = []
	total = []; total1 = []; total2 = []; total3 = []

	for i in dic.keys():
		tmp_key.append(i)
	for key in tmp_key:
		total.append(list(product([key],cs.domains[key])))
	total3 = list(product(*total))
	for i in total3:
		temp=[]
		for y in i:
			temp.append(y)
		total2.append(temp)
	for i in total2:
		i = dict(i); total1.append(i)
	for solution in total1:
		works = True
		for i in cs.constraints:
			args = scope(i)
			temp = dict()
			for arg in args:
				temp[arg] = solution[arg]
			if not i(**temp):
				works = False
		if works:
			yield solution

#~ simple_csp = CSP(
	#~ domains={x: list(range(1, 5)) for x in 'abc'},
	#~ constraints={
		#~ lambda a, b: a < b,
		#~ lambda b, c: b < c,
		#~ })
#~ 
#~ solutions = sorted(str(sorted(solution.items())) for solution 
				   #~ in generate_and_test(simple_csp))
#~ print("\n".join(solutions))
#~ 
#~ 
#~ import itertools
#~ 
#~ crossword_puzzle = CSP( # from slide 14
	#~ domains={
		#~ # read across:
		#~ 'a1': "ant,big,bus,car".split(','),
		#~ 'a3': "book,buys,hold,lane,year".split(','),
		#~ 'a4': "ant,big,bus,car,has".split(','),
		#~ # read down:
		#~ 'd1': "book,buys,hold,lane,year".split(','),
		#~ 'd2': "ginger,search,symbol,syntax".split(','),
		#~ },
	#~ constraints={
		#~ lambda a1, d1: a1[0] == d1[0],
		#~ lambda d1, a3: d1[2] == a3[0],
		#~ lambda a1, d2: a1[2] == d2[0],
		#~ lambda d2, a3: d2[2] == a3[2],
		#~ lambda d2, a4: d2[4] == a4[0],
		#~ })
#~ 
#~ solution = next(iter(generate_and_test(crossword_puzzle)))
#~ 
#~ # printing the puzzle similar to the way it actually  looks 
#~ pretty_puzzle = ["".join(line) for line in itertools.zip_longest(
	#~ solution['d1'], "", solution['d2'], fillvalue=" ")]
#~ pretty_puzzle[0:5:2] = solution['a1'], solution['a3'], "  " + solution['a4']
#~ print("\n".join(pretty_puzzle))
