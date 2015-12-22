class Fuzzifier:

    def __init__(self, input_, label):
        self.crisp_input = input_
        self.label = label

    def getFuzzy(self):
        # call detSubset and geTriMf and store it in fuzzy_val
        self.detSubset()
        self.getTriMf()
        return self.fuzzy_val

    def detSubset(self):
        # scan  the fuzzy set and determine which subset the input belongs
        self.subset = {}
        for key in self.label.keys():
            if self.crisp_input >= self.label[key][
                    0] and self.crisp_input <= self.label[key][2]:
                self.subset.update({key: self.label[key]})

    def getTriMf(self):
        # (x = input,a,b,c) feet and peak
        # max(min((x - a) / (b - a), (c - x) / (c - b)), 0)
        # max(min(((x - a) / (b - a)), 1, ((d - x) / (d - c))), 0)
        # adjust calculations to fit trapezoid function
        self.fuzzy_val = {}
        for a, b in self.subset.items():
            if b[3] == 1:
                if b[4] == 0:
                    a1 = -0.4
                    b1 = -0.2
                    value = max(
                        min(((self.crisp_input - a1) / (b1 - a1)), 1,
                            ((b[2] - self.crisp_input) / (b[2] - b[1]))), 0)
                else:
                    c1 = 1.2
                    d1 = 1.4
                    value = max(
                        min(((self.crisp_input - b[0]) / (b[1] - b[0])), 1,
                            ((d1 - self.crisp_input) / (d1 - c1))), 0)
            else:
                value = max(min(((self.crisp_input -
                                  b[0]) / (b[1] - b[0])), ((b[2] -
                                                            self.crisp_input) /
                                                           (b[2] - b[1]))), 0)
            self.fuzzy_val.update({a: round(value, 2)})

    def getInput(self):
        return self.crisp_input

    def getDetSubset(self):
        return self.subset
