import math

class ComplexCalculator:
    def __init__(self, n1, n2, operation):
        self.n1 = n1
        self.n2 = n2
        self.operation = operation

    def calculate(self):
        c1 = self.n1
        c2 = self.n2
        op = self.operation
        c1 = [int(v.strip()) for v in c1]
        c2 = [int(v.strip()) for v in c2]
        
        if op == '+':
            result = c1[0] + c2[0], c1[1] + c2[1]
        elif op == '-':
            result = c1[0] - c2[0], c1[1] - c2[1]
        elif op == '*':
            result = c1[0]*c2[0] - c1[1]*c2[1], c1[0]*c2[1] + c1[1]*c2[0]
        elif op == '/':
            result = (c1[0]*c2[0] + c1[1]*c2[1])/(c2[0]**2 + c2[1]**2), (c1[1]*c2[0] - c1[0]*c2[1])/(c2[0]**2 + c2[1]**2)
        elif op == 'modulos':
            result = math.sqrt(c1[0]**2 + c1[1]**2), math.sqrt(c2[0]**2 + c2[1]**2)
        else:
            result = "Invalid operation"
                    

        if op != "modulos" and result != "Invalid operation":
            print(f"The result of the operation is: {result}")
            print(f"The conjulgate of the result is: {result [0],result [1]*-1}")
        elif op == "modulos":
            print(f"The modulos of the first complex number is: {result[0]:.2f}")
            print(f"The modulos of the second complex number is: {result[1]:.2f}")

def main():

    c1 = input("Enter the first complex number, with its real and imaginarium parts separeted by coma (ex: 10,25): ").split(',')
    c2 = input("Enter the firsecond complex number, with its real and imaginarium parts separeted by coma (ex: 10,25): ").split(',')
    op = input("Enter the operation to be performed (+, -, *, /, or modulos):")

    calculator = ComplexCalculator(c1, c2, op)
    result = calculator.calculate()
    
    

    
if __name__ == "__main__":

    main()
