import random as rand   #Imports random for random weight values and training sample selection
import math     #Imports math for activation function

class Structure:

    numAIs = 0                              #A counter for the number of AIs are made

    def __init__(self, inputs, numOfHiddens, numOfLayers,numOfOutputs):
        self.inputs = inputs                #Sets inputs
        self.numOfInputs = len(inputs)      #Sets number of inputs
        self.numOfHiddens = numOfHiddens    #Sets number of hidden nodes
        self.numOfLayers = numOfLayers      #Sets number of hidden layers
        self.numOfOutputs = numOfOutputs    #Sets number of outputs
        self.aiNum = Structure.numAIs       #Sets what the AI number is
        Structure.numAIs += 1               #Increases the counter

    #Initialises the weights for the layers
    def Initialise(self):
        weights = []                        #List of weights


###
# Will use Machine Learning techniques used in dissertation