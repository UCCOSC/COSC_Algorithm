
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

import itertools

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
    query_result = dict()
    hidden_vars = network.keys() - evidence.keys() - {query_var}
    tf = [] #stores a true and a false probability
    for query_state in (True, False):
        hidden_sum = 0
        for values in itertools.product((True, False), repeat=len(hidden_vars)):
            hidden_assignments = {var:val for var,val in zip(hidden_vars, values)}
            assignment = evidence.copy()
            assignment[query_var] = query_state        
            assignment.update(hidden_assignments)
            hidden_sum += joint_prob(network, assignment)
        tf.append(hidden_sum)
   
    query_result[True] = tf[0]/sum(tf)
    query_result[False] = tf[1]/sum(tf)      
    return query_result

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

network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
            }},
            
    'B': {
        'Parents': ['A'],
        'CPT': {
            (True,): 0.8,
            (False,): 0.7,
            }},
    }
 
answer = query(network, 'B', {'A': False})
print("P(B=true|A=false) = {:.5f}".format(answer[True]))
print("P(B=false|A=false) = {:.5f}".format(answer[False]))

network = {
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

answer = query(network, 'Burglary', {'John': True, 'Mary': True})
print("Probability of a burglary when both\n"
      "John and Mary have called: {:.3f}".format(answer[True]))  

print("---------------------------------------------------------")
network = {
    'Disease': {
        'Parents': [],
        'CPT': {
            (): 1.0/100000
            }},
           
    'Test': {
        'Parents': ['Disease'],
        'CPT': {
            (True,): 0.99,
            (False,): 0.01,
            }},
    }
    
answer = query(network, 'Disease', {'Test': True})
print("The probability of having the disease\n"
      "if the test comes back positive: {:.8f}"
      .format(answer[True]))
