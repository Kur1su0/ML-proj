#test load mnist dataset
from utils import mnist_loader
import numpy as np


training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
training_data = list(training_data)
test_data = list(test_data) 

print("Training: ",len(training_data))
#print(np.shape(training_data))


print("Test: ",len(test_data))
#print(test_data[0])









