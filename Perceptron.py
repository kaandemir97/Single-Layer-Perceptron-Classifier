import random as rand
import numpy as np

class Perceptron:

    def __init__(self, imagepool, featurepool):
        self.imagepool = imagepool
        self.featurepool = featurepool
        self.weights = np.concatenate((np.array([1]),np.random.randint(-1,3,50)),axis=0) # We do 0, -1, bias = 1
        self.weights = self.weights.astype(float)
        self.LR = 0.05 #This learning rate minimizes number of iterations for completion, i found it by trial and error
        print("INITIAL WEIGHTS | w0 = b = 1")
        print(self.weights)
        return

    def run(self):
        acc = 0.0
        iter = 1
        converge = 0
        # LOOP UNTIL ITERATION NOT 100XNUMIMAGES AND NOT 100% ACCURATE
        while iter < 100*(len(self.imagepool)) and acc != 1:
            correct =  0.0
            for i in range(len(self.imagepool)):
                # ACTIVATE NEURON
                prediction = self.fire(self.imagepool[i])
                if prediction==self.imagepool[i].cl:
                    correct +=1.0
                elif prediction == 0:
                    self.adjustWeights(self.imagepool[i],1,prediction)
                else:
                    self.adjustWeights(self.imagepool[i],0,prediction)
            correct = correct/float(len(self.imagepool))
            acc = correct
            print("##################### Accuracy: %2f"%acc)
            iter +=1
        print("Convergence at iteration: %d"%iter)
        print("Final accuracy: %f"%acc)
        return

    def predict(self,img):
        return self.fire(img)

    def fire(self,img):
        sum = 0.0
        for i in range(51):
            sum+= self.weights[i]*self.featurepool[i].value(img)
        # STEP FUNCTION
        return 1 if sum >0 else 0

    def adjustWeights(self,img,actual,y):
        # WEIGHTS ADJUSTED ACCORDING TO POSITIVE/NEGATIVE PREDICTION
        sign = self.featurepool[0].value(img)
        self.weights[0] = self.weights[0]+self.LR*(actual-y)*sign
        for i in range(1,51):
            sign = self.featurepool[i].value(img)
            self.weights[i] = self.weights[i]+self.LR*(actual-y)*sign
        return
