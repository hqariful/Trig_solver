import math

class Trig:
    def __init__(self,A=None, B=None, C=None, a=None, b=None, c=None):
        self.angle = {
            "A":A,
            "B":B,
            "C":C
        }
        self.side = {
            "a":a,
            "b":b,
            "c":c
        }
        self.angleUnknown = 0
        self.sideUnknown = 0
        for each in self.angle:
            if self.angle[each] is None:
                self.angleUnknown+=1
        for each in self.side:
            if self.side[each] is None:
                self.sideUnknown+=1

    def solve(self):
        a = self.side['a']
        b = self.side['b']
        c = self.side['c']
        A = self.angle['A']
        B = self.angle['B']
        C = self.angle['C']

        if self.sideUnknown + self.angleUnknown > 3:
            print("Not much data given")
            return 0
        if self.sideUnknown + self.angleUnknown < 3:
            print("Excess information given")
            return 0

        if self.angleUnknown == 3:
            if a + b < c or b + c < a or c + a < b:
                print("sum of 2 side should be greater than third")
                return 0
            C = math.degrees(math.acos((a**2+b**2-c**2)/(2*a*b)))
            B = math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c)))
            A = math.degrees(math.acos((b**2+c**2-a**2)/(2*c*b)))
            print("A:",round(A,2),"B:",round(B,2),"C:",round(C,2))

        if self.angleUnknown == 2:
            pass

        if self.angleUnknown == 1:
            pass
    
p1 = Trig(a=3,b=4,c=15)
p1.solve()