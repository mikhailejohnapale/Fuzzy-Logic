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

        output = Defuzzifier(
            TrafficCongestion().getCongestionSet(),
            self.mamdaniResult)
        level = output.getLevel()
        status = output.getStatus()
        value = output.getValue()

        return level, status, value

    def getFuzzyValue(self):
        return self.fuzzyVal

    def getMamdaniResult(self):
        return self.mamdaniResult
