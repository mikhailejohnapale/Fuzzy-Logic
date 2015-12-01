class Defuzzifier:
    label = []
    inference_result = []
    crisp_output = []

    def __init__(self, label, inference_result):
        self.label = label
        self.inference_result = inference_result

    def getCentroid(self):
        return self.crisp_output
