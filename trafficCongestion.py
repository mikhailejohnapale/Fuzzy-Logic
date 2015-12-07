class TrafficCongestion:
    rules = []
    velocitySet = [
        [
            "very slow", 0, 0.4], [
            "slow", 0.2, 0.6], [
            "moderate", 0.4, 0.8], [
            "fast", 0.6, 1]]
    densitySet = [
        [
            "low", 0, 0.4], [
            "moderate", 0.2, 0.6], [
            "high", 0.4, 0.8], [
            "very high", 0.6, 1]]

    congestionSet = [
        [
            "free", 0, 0.4], [
            "low", 0.2, 0.6], [
            "moderate", 0.4, 0.8], [
            "high", 0.6, 1]]

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
