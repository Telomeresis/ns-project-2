""" this is used to generate graphs for the experiment results. """
from typing import List
import matplotlib.pyplot as plt 
import numpy as np

def get_accuracy_list (filename: str) -> List:
    """ get a list of trainning accuracy from a specified text file generated during the trainning process
    
    Note that in the file each line contains three numbers: "average loss, trainning accuracy, testing accuracy"
    """
    test_accuracy_list = []
    f = open(filename, "r")
    for line in f:
        splitted_string = line.split()

        # the trainning accuracy is at the third place of each line
        # to get the different accuracy (trainning at [1]/testing at [2]), just change the positional index below
        test_accuracy = float(splitted_string[2])
        test_accuracy_list.append(test_accuracy)
    
    f.close()

    return test_accuracy_list

GIN_MLP0_accuracy_list = get_accuracy_list("IMDBBINARY_SUM(GIN-MLP0).txt")
GIN_MLPeps_accuracy_list = get_accuracy_list("IMDBBINARY_SUM(GIN-MLPeps).txt")

x = np.linspace(0,350, 350)

fig, ax = plt.subplots()
ax.plot(x, GIN_MLP0_accuracy_list, label ="SUM--MLP (GIN0)")
ax.plot(x, GIN_MLPeps_accuracy_list, label = "SUM--MLP(GINeps)")
ax.set_xlabel('epochs')
ax.set_ylabel("testting accuracy")
ax.set_title("IMDBBINARY")
ax.legend()
plt.show()
