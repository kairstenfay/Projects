class Difference:
    def __init__(self, a):
        self.__elements = a


# End of Difference class

# Add your code here
    
    def computeDifference(self): 
        maximum = max(self.__elements)
        minimum = min(self.__elements)
        self.maximumDifference = maximum - minimum
        return 
        
            

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)