import csv

def learn_likelihood(file_name, pseudo_count=0):
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]
    span=[]
    not_span=[]
    number_span = 0
    number_not_span = 0
    pos = 0
    result = []
    while(pos < len(training_examples[0])-1):
        for i in range(1,len(training_examples)):
            if training_examples[i][-1] == str(1):
                span.append(training_examples[i][-1])
            if training_examples[i][-1] == str(0):
                not_span.append(training_examples[i][-1])

            if training_examples[i][pos] == str(1) and training_examples[i][-1] == str(1):
                number_span += 1
            if training_examples[i][pos] == str(0) and training_examples[i][-1] == str(0):
                number_not_span += 1

        total_span = len(span); total_not_span = len(not_span)
        p1 = (number_span + pseudo_count) / (total_span + pseudo_count * 2)
        p2 = (number_not_span + pseudo_count) / (total_not_span + pseudo_count * 2)
        result.append([p2,p1])
        pos += 1
    print(result)
    return result


likelihood = learn_likelihood("spam-labelled.csv")
print(len(likelihood))
print([len(item) for item in likelihood])
print("--------------------------------------------------")
print("12 - [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]")

likelihood = learn_likelihood("spam-labelled.csv")

print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))
print("--------")
print("P(X1=True | Spam=False) = 0.35570 \n P(X1=False| Spam=False) = 0.64430\n P(X1=True | Spam=True ) = 0.66667 \n P(X1=False| Spam=True ) = 0.33333")


likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)

print("With Laplacian smoothing:")
print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))
