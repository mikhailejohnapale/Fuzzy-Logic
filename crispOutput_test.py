from fuzzylogic import *
import random


class Test:

    def crispOutput():
        density = random.choice([x / 10 for x in range(0, 11, 1)])
        velocity = random.choice([x / 10 for x in range(0, 11, 1)])
        print('Density = ', density, 'Velocity = ', velocity)
        ins = FuzzyLogic([density, velocity])
        if density == 0 and velocity == 0:
            a = ins.getResult()
        else:
            a = ins.getResult()
            Test.fuzzyValue(ins.getFuzzyValue())
            Test.mamdaniRslt(ins.getMamdaniResult())
        return a

    def fuzzyValue(fuzzy_val):
        for value in fuzzy_val:
            print('fuzzy -->', value)

    def mamdaniRslt(result):
        print('mamdani -->', result)

    def testOutput():
        for i in range(1000):
            print(Test.crispOutput(), '\n\n')

Test.testOutput()
