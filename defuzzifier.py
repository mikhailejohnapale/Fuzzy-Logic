class Defuzzifier:

    def __init__(self, label, inference_result):
        self.label = label
        self.inference_result = inference_result

    def getCentroid(self):
        divn = 0
        divs = 0
        self.stat_lbl = []
        for index in range(len(self.label)):
            for key_stat in self.label[index][0].keys():
                for key_infer in self.inference_result.keys():
                    if key_stat == key_infer:
                        divn = divn + \
                            (self.label[index][0][key_stat][1] *
                             self.inference_result[key_infer])
                        divs = divs + self.inference_result[key_infer]
                        self.stat_lbl.append(key_infer)
        self.crisp_output = '{0} ---->>> {1} - {2} '.format(
            round((divn / divs), 2),
            self.stat_lbl[0],
            self.stat_lbl[
                len(self.stat_lbl) - 1])
        return self.crisp_output

    def getStatus_lbl(self):
        return self.stat_lbl
