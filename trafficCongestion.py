class TrafficCongestion:
    rules = [
        [{"low": 0}, {"very low": 0}, {"low": 0}],
        [{"moderate": 0}, {"very slow": 0}, {"moderate": 0}],
        [{"high": 0}, {"very slow": 0}, {"high": 0}],
        [{"very high": 0}, {"very slow": 0}, {"high": 0}],
        [{"low": 0}, {"slow": 0}, {"low": 0}],
        [{"moderate": 0}, {"slow": 0}, {"low": 0}],
        [{"high": 0}, {"slow": 0}, {"moderate": 0}],
        [{"very high": 0}, {"slow": 0}, {"high": 0}],
        [{"low": 0}, {"moderate": 0}, {"free": 0}],
        [{"moderate": 0}, {"moderate": 0}, {"low": 0}],
        [{"high": 0}, {"moderate": 0}, {"moderate": 0}],
        [{"very high": 0}, {"moderate": 0}, {"moderate": 0}],
        [{"low": 0}, {"fast": 0}, {"free": 0}],
        [{"moderate": 0}, {"fast": 0}, {"free": 0}],
        [{"high": 0}, {"fast": 0}, {"low": 0}],
        [{"very high": 0}, {"fast": 0}, {"moderate": 0}]
    ]
    # last 2 index of dictionary denotes the funtion to be used 1 for
    # trapezoid and 0 for triangular
    velocitySet = {
        "very slow": [0, 0.2, 0.4, 1, 0],
        "slow": [0.2, 0.4, 0.6, 0, 0],
        "moderate": [0.4, 0.6, 0.8, 0, 0],
        "fast": [0.6, 0.8, 1, 1, 1]}
    densitySet = {
        "low": [0, 0.2, 0.4, 1, 0],
        "moderate": [0.2, 0.4, 0.6, 0, 0],
        "high": [0.4, 0.6, 0.8, 0, 0],
        "very high": [0.6, 0.8, 1, 1, 1]}

    congestionSet = {
        "free": [0, 0.2, 0.4, 1, 0],
        "low": [0.2, 0.4, 0.6, 0, 0],
        "moderate": [0.4, 0.6, 0.8, 0, 0],
        "high": [0.6, 0.8, 1, 1, 1]}

    def __init__(self):
        pass

    def getRules(self):
        return self.rules

    def getVelocitySet(self):
        return self.velocitySet

    def getDensitySet(self):
        return self.densitySet

    def getCongestionSet(self):
        return self.congestionSet
