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
        for a, b in self.label.items():
            if self.crisp_input >= b[0] and self.crisp_input <= b[2]:
                self.subset.update({a: b})

    def getTriMf(self):
        # (x = input,a,b,c) feet and peak
        # max(min((x - a) / (b - a), (c - x) / (c - b)), 0)
        self.fuzzy_val = {}
        for a, b in self.subset.items():
            value = max(min(((self.crisp_input - b[0]) / (b[1] - b[0])),
                            ((b[2] - self.crisp_input) / (b[2] - b[1]))), 0)
            self.fuzzy_val.update({a: round(value, 2)})
        print(self.fuzzy_val)

velocitySet = {
    "very slow": [0, 0.2, 0.4],
    "slow": [0.2, 0.4, 0.6],
    "moderate": [0.4, 0.6, 0.8],
    "fast": [0.6, 0.8, 1]}

densitySet = {
    "low": [0, 0.2, 0.4],
    "moderate": [0.2, 0.4, 0.6],
    "high": [0.4, 0.6, 0.8],
    "very high": [0.6, 0.8, 1]}

Fuzzifier(0.6, velocitySet).getFuzzy()
Fuzzifier(0.3, densitySet).getFuzzy()
