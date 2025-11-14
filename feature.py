class FeatureExtraction:
    def __init__(self, url):
        self.url=url
    def getFeaturesList(self):
        import random
        return [random.choice([-1,0,1]) for _ in range(30)]
