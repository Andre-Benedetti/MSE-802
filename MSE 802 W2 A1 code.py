import math

def main():

    c1 = input("Enter the first complex number, with its real and imaginarium parts separeted by coma (ex: 10,25): ").split(',')
    c2 = input("Enter the firsecond complex number, with its real and imaginarium parts separeted by coma (ex: 10,25): ").split(',')
    op = input("Enter the operation to be performed (+, -, *, /, or modulos):")

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

    print(f"The result of the operation is: {result}") 
    

    
if __name__ == "__main__":

    main()
