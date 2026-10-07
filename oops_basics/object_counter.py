class ObjectCounter:
    noOfObjects = 0

    def __init__(self):
        ObjectCounter.noOfObjects += 1

    @staticmethod
    def displayCount():
        print(ObjectCounter.noOfObjects)

o1 = ObjectCounter()
o2 = ObjectCounter()
ObjectCounter.displayCount()