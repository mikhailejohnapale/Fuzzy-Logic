class Fuzzifier:
    test = "test 2"

    def __init__(self, input_, label):
        self.input_ = input_
        self.label = label
        #self.test = "this is a test"

    def getFuzzy(self):
        self.test = "test 3"
        # return self.list

    def detSubset(self):
        pass

    def getTriMf(self):
        pass

a = Fuzzifier(1, 2)
print(a.test)
a.getFuzzy()
print(a.test)
