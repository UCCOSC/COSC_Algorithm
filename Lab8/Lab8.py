alarm_net = {
    'Burglary': {
        'Parents': [],
        'CPT': {
            (): 0.001
            }},
            
    'Earthquake': {
        'Parents': [],
        'CPT': {
            (): 0.002,
            }},
    'Alarm': {
        'Parents': ['Burglary','Earthquake'],
        'CPT': {
            (True,True): 0.95,
            (True,False): 0.94,
            (False,True): 0.29,
            (False,False): 0.001,
            }},

    'John': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.9,
            (False,): 0.05,
            }},

    'Mary': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.7,
            (False,): 0.01,
            }},
    }

def joint_prob(network, assignment):
    nodes = assignment.keys()
    individual_probs = {node:None for node in nodes}
    solved = False
    while not solved:
        for node in nodes:
            if not individual_probs[node]:
                parents = network[node]['Parents']
                if parents == []:
                    individual_probs[node] = network[node]['CPT'][()]
                    if assignment[node] == False: #assignment says false
                        individual_probs[node] = 1 - individual_probs[node]
                else:
                    if all([individual_probs[par] for par in parents]):
                        cond = tuple((assignment[par] for par in parents))
                        individual_probs[node] = network[node]['CPT'][cond]
                        if assignment[node] == False: #assignment says false
                            individual_probs[node] = 1 - individual_probs[node]
        if all([individual_probs[node] for node in nodes]):
            solved = True
    joint_probability = 1.0
    for _,prob in individual_probs.items(): joint_probability *= prob
    return joint_probability

def query(network, query_var, evidence):
    hidden_vars = network.keys() - evidence.keys() - {query_var}
    
    print(hidden_vars)
    
network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2
            }},
}

answer = query(network, 'A', {})
print("P(A=true)={:.5f}".format(answer[True]))
print("P(A=false)={:.5f}".format(answer[False]))
