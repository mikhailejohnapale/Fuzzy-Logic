class Fuzzifier:
    label = []
    fuzzy_val = []

    def __init__(self, input_, label):
        self.crisp_input = input_
        self.label = label

    def getFuzzy(self):
        # call detSubset and geTriMf and store it in fuzzy_val
        for i in self.label:
            if self.crisp_input in i:
                print(i)

    def detSubset(self):
        # scan  the fuzzy set and
        pass

    def getTriMf(self):
        # formula triMf
        #(x = input,a,b,c) feet and peak
        #max(min((x - a) / (b - a), (c - x) / (c - b)), 0)

        pass


velocitySet = [
    [
        "very slow", 0, 0.4], [
        "slow", 0.2, 0.6], [
        "moderate", 0.4, 0.8], [
        "fast", 0.6, 1]]

Fuzzifier(0.4, velocitySet).getFuzzy()
