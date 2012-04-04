class Fibo:
    def __init__(self, data):
        self.data = data
        self.index = -1
        self.lastElem = 1;
        self.secondLastElem = 1;
    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        if (self.index == 0 or self.index == 1):
            return 1
        currentFibNumber =  self.secondLastElem + self.lastElem
        self.secondLastElem = self.lastElem
        self.lastElem = currentFibNumber
        if (self.lastElem > self.data) :
            raise StopIteration
        return self.lastElem
        
if __name__ == "__main__":
    #import imp
    #imp.reload(sys)
    #try:
    #f = Fraction("spaghetti",3)
    #except TypeError as e:
    #    print(e)
    for f in Fibo(30):
        print(f)

    #autre main