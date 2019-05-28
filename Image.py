class imge:
    def __init__(self, cl, X, Y, pixels):
        #class of image
        self.cl = cl
        self.X = X
        self.Y = Y
        self.pixels = pixels
        if self.cl == 'X':
            self.cl = 1
        else:
            self.cl = 0
        return
    def getPixel(self, row, col):
        return int(self.pixels[row][col])
