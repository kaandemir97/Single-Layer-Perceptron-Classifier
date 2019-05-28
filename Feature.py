import random as rand
import numpy as np

class features:

    def __init__(self, imagepool):
        rand.seed(12345)
        self.featurepool = self.constructFeatures(imagepool)
        return

    def constructFeatures(self, imagepool):
        featurepool = []
        featurepool.append(bias())
        for i in range(50):
            # 50 random features, sgn is either 1 or 0 (true/false) - this makes comparisons easier
            sgn = np.array(rand.choices(range(2),k=4))
            featurepool.append(feature(rand.sample(range(10),4),rand.sample(range(10),4),sgn))
        return featurepool

class feature:

    def __init__(self, row, col, sgn):
        self.row = row
        self.col = col
        self.sgn = sgn
        return

    #Get pixel at X,Y
    def value(self, image):
        sum = 0
        for i in range(4):
            if image.getPixel(self.row[i],self.col[i]) == self.sgn[i]:
                sum += 1
        return 1 if sum>2 else 0;

    def toString(self):
        print(str(self.row) +" "+ str(self.col) +" "+ str(self.sgn) +"\n")
        return

class bias:

    def __init__(self):
        return

    def value(self, image):
        return 1
