import csv

def learn_prior(file_name, pseudo_count=0):
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]
    span=[]
    not_span=[]
    for i in range(1,len(training_examples)):
        if training_examples[i][-1] == str(1):
            span.append(training_examples[i][-1])
        if training_examples[i][-1] == str(0):
            not_span.append(training_examples[i][-1])
    total_span = len(span); total_not_span = len(not_span)
    p = (total_span+pseudo_count) / (total_span + total_not_span + pseudo_count*2)
    return p
        
prior = learn_prior("spam-labelled.csv")
print("Prior probability of spam is {:.5f}.".format(prior))
prior = learn_prior("spam-labelled.csv")
print("Prior probability of not spam is {:.5f}.".format(1 - prior))	
print("Prior probability of not spam is 0.74500.")
prior = learn_prior("spam-labelled.csv", pseudo_count = 1)
print(format(prior, ".5f"))	
print("correct : 0.25743")
prior = learn_prior("spam-labelled.csv", pseudo_count = 2)
print(format(prior, ".5f"))
print("correct : 0.25980")
prior = learn_prior("spam-labelled.csv", pseudo_count = 10)
print(format(prior, ".5f"))
print("correct : 0.27727")
prior = learn_prior("spam-labelled.csv", pseudo_count = 100)
print(format(prior, ".5f"))
print("correct : 0.37750")
prior = learn_prior("spam-labelled.csv", pseudo_count = 1000)
print(format(prior, ".5f"))
