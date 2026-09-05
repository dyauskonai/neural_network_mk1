import numpy as np
print("\n")


class Neuron:
    def __init__(self,weights,bias):
        self.weights = weights
        self.bias =  bias
    def feedforward(self,inputs): #feedforward is the technical term for an output.
        total = np.dot(self.weights,inputs) + bias
        return sigmoid(total)

weights = np.array([0,1])
bias = 4
n = Neuron(weights,bias)

x = np.array([2,3]) 
print (n.feedforward(x))

def sigmoid(x):
    #  Activation function (Sigmoid): f(x) = 1 / (1 + e^(-x))
    return 1/(1+np.exp(-x))

print("\n")
