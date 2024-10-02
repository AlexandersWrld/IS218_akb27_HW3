from calculator.arithmetic import add, subtract, multiply, divide

class Calculation:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def get_result(self):
        return self.operation(self.a, self.b)
    
    @staticmethod    
    def newcalculation(a, b, operation):
        return Calculation(a, b, operation)
    
    def docalculation(self):
        return self.operation(self.a, self.b)
