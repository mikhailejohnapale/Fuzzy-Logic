from fuzzifier import *
from trafficCongestion import *
from inference import *
from defuzzifier import *


class FuzzyLogic:

    def __init__(self, input_):
        self.input_ = input_

    def getResult(self):
        """
        self.fuzzyVal stores a list  dictionary of fuzzy values.
        self.mamdaniResult stores a dictionary of of result from inference.
        self.ouput stores the crisp ouput from defuzzifier.
        """
        self.fuzzyVal = [{}, {}]
        self.fuzzyVal[0] = Fuzzifier(self.input_[0],
                                     TrafficCongestion().getDensitySet()
                                     ).getFuzzy()
        self.fuzzyVal[1] = Fuzzifier(self.input_[1],
                                     TrafficCongestion().getVelocitySet()
                                     ).getFuzzy()

        self.mamdaniResult = Inference(
            self.fuzzyVal,
            TrafficCongestion().getRules()).inferMamdani()

        """
        self.ouput = {
            Defuzzifier(
                TrafficCongestion().getCongestionSet(),
                self.mamdaniResult).getCentroid()}

        return self.ouput"""
x = FuzzyLogic([0.6, 0.43]).getResult()
i = 1
for list in x:
    print(i, list, '\n')
    i = i + 1
