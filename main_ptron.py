import sys
from ImageParser import parse
from Feature import features,bias
from Perceptron import Perceptron

def main(argv):

    if len(argv) != 1:
        print("Invalid function call: main_ptron.py <image.data>")
        return

    parsed = parse(argv[0])
    feat = features(parsed.imagepool)
    ptron = Perceptron(parsed.imagepool, feat.featurepool)
    ptron.run()

    print("PTRON FINAL WEIGHTS: ")
    print(ptron.weights)

    #Prints out the random features created
    i = 1
    for fe in feat.featurepool:
        if isinstance(fe, bias):
            print("################\n")
            print("Feature %d: " % i)
            print("BIAS = %d\n" %fe.value(None))
            i+=1
            continue
        print("################\n")
        print("Feature %d: " % i)
        print("Row:%s"%fe.row)
        print("Col:%s"%fe.col)
        print("Sign:%s\n"%fe.sgn)
        input("more... %d/%d\n"%(i, len(feat.featurepool)))
        i+=1

    #Trials on my own custom images created by the MakeImage.java file - not accurate
    print("My image predictions: ")
    myimgs = parse("myimages.data")
    correct = 0
    for img in myimgs.imagepool:
        prediction = ptron.predict(img)
        actual = img.cl
        if actual == prediction:
            correct += 1
        print("Actual: %d Prediction: %d Correct?: %s" % (actual, prediction, (actual==prediction)))
    print("Overall Accuracy for myimages.data: %f" %(correct/len(myimgs.imagepool)))
    return


if __name__ == "__main__":
    main(sys.argv[1:])
