from fuzzifier import *
from trafficCongestion import *


class FuzzyLogic:

    def __init__(self, input_):
        self.input_ = input_

    def getResult(self):
        self.fuzzyVal = [[], []]
        self.fuzzyVal[0] = Fuzzifier(self.input_[0],
                                     TrafficCongestion().getDensitySet()
                                     ).getFuzzy()
        self.fuzzyVal[1] = Fuzzifier(self.input_[1],
                                     TrafficCongestion().getVelocitySet()
                                     ).getFuzzy()
        return self.fuzzyVal


print(FuzzyLogic([0.3, 0.6]).getResult())
