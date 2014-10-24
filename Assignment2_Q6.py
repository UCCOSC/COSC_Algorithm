def valid_crossover_points(parent1, parent2, depth_limit, var_p1 = 0, var_p2 = 0):
	current_depth = depth_limit
	if isinstance(parent1,list):
		valid_crossover_points(parent1[1], parent2, current_depth-1,var_p1+1)
		valid_crossover_points(parent1[2], parent2, current_depth-1,var_p1+1)
		
	if isinstance(parent2,list):
		valid_crossover_points(parent1, parent2[1], current_depth-1,var_p1, var_p2+1)
	return ((var_p1, var_p2),)
	

parent1 = 11
parent2 = 'x'
depth_limit = 0
print(sorted(valid_crossover_points(
			parent1, parent2, depth_limit)))

print("Example A:")
parent1 = ['+', 11, 22]
parent2 = 'x'
depth_limit = 1
print(sorted(valid_crossover_points(
			parent1, parent2, depth_limit)))

print("Example B:")
parent1 = 'x'
parent2 = ['+', 11, 22]
depth_limit = 1
print(sorted(valid_crossover_points(
			parent1, parent2, depth_limit)))
print("---------------------------------------------------------")
answer = query(network, 'Disease', {'Test': True})
print("The probability of having the disease\n"
      "if the test comes back positive: {:.8f}"
      .format(answer[True]))
