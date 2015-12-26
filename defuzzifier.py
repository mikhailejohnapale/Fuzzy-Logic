class Defuzzifier:

    def __init__(self, label, inference_result):
        self.label = label
        self.inference_result = inference_result
        self.getCentroid()

    def getCentroid(self):
        divn = 0
        divs = 0
        stat_lbl = []
        for index in range(len(self.label)):
            for key_stat in self.label[index][0].keys():
                for key_infer in self.inference_result.keys():
                    if key_stat == key_infer:
                        divn = divn + \
                            (self.label[index][0][key_stat][1] *
                             self.inference_result[key_infer])
                        divs = divs + self.inference_result[key_infer]
                        stat_lbl.append(key_infer)
        if len(stat_lbl) > 1:
            self.crisp_output = divn / divs
            self.stat_output = stat_lbl[0], stat_lbl[len(stat_lbl) - 1]
        else:
            self.crisp_output = divn / divs
            self.stat_output = stat_lbl[0]

    def getStatus(self):
        return self.stat_output

    def getLevel(self):
        return self.crisp_output

    def getValue(self):
        status = {'free': 1, 'low': 2, 'moderate': 3, 'high': 4}
        for key in status.keys():
            if isinstance(self.stat_output, tuple):
                self.value = status[
                    self.stat_output[len(self.stat_output) - 1]]
            else:
                self.value = status[self.stat_output]
        return self.value
