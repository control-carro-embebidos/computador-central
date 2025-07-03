from pop_corn.matrix import Matrix, Vec
import random

class Perceptron:
    def __init__(self, name_or_input_size, output_size=None):
        if isinstance(name_or_input_size,str):
            self.weights = Matrix.load_file(name_or_input_size)
        else:
            self.weights = Matrix(name_or_input_size+1, output_size,  [random.random() for _ in range((name_or_input_size+1) * (output_size))])  

    def predict(self, inputs):
            return inputs.tail() * self.weights

    def train(self, inputs, labels, learning_rate=0.1, epochs=1):
        for epoch in range(epochs):
            predictions = self.predict(inputs)
            error = labels - predictions
            self.weights +=  inputs.tail().T() * error * learning_rate
            
    def save_file(self,name):
        self.weights.save_file(name)
