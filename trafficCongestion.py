class TrafficCongestion:
    rules = [
        [{"low": 0}, {"very low": 0}, {"low": 0}],
        [{"medium": 0, "very slow": 0, "moderate": 0}],
        [{"high": 0, "very slow": 0, "high": 0}],
        [{"very high": 0, "very slow": 0, "high": 0}],
        [{"low": 0, "slow": 0, "low": 0}],
        [{"medium": 0, "slow": 0, "low": 0}],
        [{"high": 0, "slow": 0, "moderate": 0}],
        [{"very high": 0, "slow": 0, "high": 0}],
        [{"low": 0, "medium": 0, "free": 0}],
        [{"medium": 0, "medium": 0, "low": 0}],
        [{"high": 0, "medium": 0, "moderate": 0}],
        [{"very high": 0, "medium": 0, "moderate": 0}],
        [{"low": 0, "fast": 0, "free": 0}],
        [{"medium": 0, "fast": 0, "free": 0}],
        [{"high": 0, "fast": 0, "low": 0}],
        [{"very high": 0, "fast": 0, "moderate": 0}]
    ]
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

    congestionSet = {
        "free": [0, 0.2, 0.4],
        "low": [0.2, 0.4, 0.6],
        "moderate": [0.4, 0.6, 0.8],
        "high": [0.6, 0.8, 1]}

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


print(TrafficCongestion.rules[0][2])
