from Image import imge

class parse:
    def __init__(self,data):
        self.imagepool = []
        self.data = self.parseData(data)
        return

    def parseData(self,data):
        with open(data) as fp:
            for line in fp:
                line = line.strip("\n")
                if line == "P1":
                    continue
                cl = line.strip("#")
                XY = fp.readline().split()
                dat = fp.readline().strip("\n")
                dat = dat+fp.readline().strip("\n")
                #Split 100 pixels to 10x10 array
                dat = [dat[i:i+10] for  i in range(0, len(dat), 10)]
                self.imagepool.append(imge(cl,XY[0],XY[1],dat))
        return
