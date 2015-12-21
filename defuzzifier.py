class Defuzzifier:

    def __init__(self, label, inference_result):
        self.label = label
        self.inference_result = inference_result

    def getCentroid(self):
        divn = 0
        divs = 0
        stat_lbl = []
        for key_stat in self.label.keys():
            for key_infer in self.inference_result.keys():
                if key_infer == key_stat:
                    divn = divn + \
                        (self.label[key_stat][1] *
                            self.inference_result[key_infer])
                    divs = divs + self.inference_result[key_infer]
                    stat_lbl.append(key_infer)
        self.crisp_output = '{0} ---->>> from {1} - {2} '.format(
            round((divn / divs), 2),
            stat_lbl[0],
            stat_lbl[
                len(stat_lbl) - 1])
        return self.crisp_output
