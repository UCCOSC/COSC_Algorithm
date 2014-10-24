def posterior(prior, likelihood, observation):
	t = 1; f = 1
	for i in range(0, len(likelihood)):
		if observation[i] == False:
			value1 = 1 - likelihood[i][1]
			value2 = 1 - likelihood[i][0]
		else:
			value1 = likelihood[i][1]
			value2 = likelihood[i][0]
		t *= value1; f *= value2
	result_t = t * prior; result_f = f * (1 - prior)
	result = result_t / (result_f + result_t)
	return result

prior = 0.05
likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

observation = (True, True, True)

class_posterior_true = posterior(prior, likelihood, observation)
print("P(C=False|observation) is approximately {:.5f}"
	  .format(1 - class_posterior_true))
print("P(C=True |observation) is approximately {:.5f}"
	  .format(class_posterior_true))  
print("Correct \n P(C=False|observation) is approximately 0.00248 \n P(C=True |observation) is approximately 0.99752")
print("----------------------------------------------------")
prior = 0.05
likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

observation = (True, False, True)

class_posterior_true = posterior(prior, likelihood, observation)
print("P(C=False|observation) is approximately {:.5f}"
	  .format(1 - class_posterior_true))
print("P(C=True |observation) is approximately {:.5f}"
	  .format(class_posterior_true))  

print("correct \n P(C=False|observation) is approximately 0.29845,\n P(C=True |observation) is approximately 0.70155")
print("----------------------------------------------------")
prior = 0.05
likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

observation = (False, False, False)

class_posterior_true = posterior(prior, likelihood, observation)
print("P(C=False|observation) is approximately {:.5f}"
	  .format(1 - class_posterior_true))
print("P(C=True |observation) is approximately {:.5f}"
	  .format(class_posterior_true))  
print("Correct \n P(C=False|observation) is approximately 0.99987, \n P(C=True |observation) is approximately 0.00013")
