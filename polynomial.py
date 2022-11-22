import math

class poly(object):
	def __init__(self, coef):
		self.coef = coef

	def order(self):
		print("The order of the polynom is " + str(len(self.coef)-1) + ".")

	def addition(self, b):
		sentence = []
		if len(self.coef) == len(b.coef):
		 	for i in range(0, (len(self.coef))):
		 		sentence.append(self.coef[i] + b.coef[i])
		 	
		 
		elif len(self.coef) > len(b.coef):
		 	for i in range(0, (len(b.coef))):
		 		sentence.append(self.coef[i] + b.coef[i])
		 	for i in range(len(b.coef), len(self.coef)):
		 		sentence.append(self.coef[i])
		 
		else:
		    for i in range(0, (len(self.coef))):
		    	sentence.append(self.coef[i] + b.coef[i])
		    for i in range(len(self.coef), len(b.coef)):
		    	sentence.append(b.coef[i])
		
		self.sum = sentence
		 

	def derivate(self):
		coefficients = [n for n in range(0, len(self.coef))]
		multiplication = []
		for i in range(1, len(self.coef)):
			multiplication.append(self.coef[i] * coefficients[i])
		self.derivative = multiplication
		
	def integrate(self, c):
		coefficients = [n for n in range(1, len(self.coef) + 1)]
		division = []
		division.append(c)
		for i in range(0, len(self.coef)):
			division.append((self.coef[i]/coefficients[i]))
		self.integral = division

	def represent(self, a):
		representation = []
		for i in range(0, len(self.coef)):
			representation.append('+' + str(self.coef[i]) + '*x^' + str(i))
		str_list = " ".join([str(ele) for ele in representation])
		print("Your " + a + " function is [{0}]".format(str_list))



