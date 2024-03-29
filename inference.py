class Inference:

    def __init__(self, fuzzy_val, rules):
        self.fuzzy_val = fuzzy_val
        self.rules = rules

    def inferMamdani(self):
        self.mamdaniResult = {}
        for i in range(len(self.rules)):
            for key, value in self.fuzzy_val[0].items():
                if key in self.rules[i][0].keys():
                    self.rules[i][0][key] = value
            for key, value in self.fuzzy_val[1].items():
                if key in self.rules[i][1].keys():
                    self.rules[i][1][key] = value

            key = [key for key in self.rules[i][2]]
            key1 = [key for key in self.rules[i][1]]
            key0 = [key for key in self.rules[i][0]]
            self.rules[i][2][
                key[0]] = min(
                self.rules[i][0][key0[0]],
                self.rules[i][1][key1[0]])
            if self.rules[i][2][key[0]] != 0:
                self.mamdaniResult.update({key[0]: self.rules[i][2][
                    key[0]]})
        return self.mamdaniResult
