import math

class Complex_converter:# Class to convert complex numbers between cartesian and polar forms
    def __init__(self, n1, operation):# Constructor to initialize complex number and operation
        self.n1 = n1
        self.operation = operation

    def calculate(self):# Method to convert complex numbers
        co = self.n1
        op = self.operation

        try:# Convert input strings to floats
            co = [float(v.strip()) for v in co]
        except ValueError:
            return "Error: Coordinates must be valid numbers."
                     
        if op == 'C':# Convert from cartesian to polar
            r = math.sqrt(co[0]**2 + co[1]**2)
            theta = math.degrees(math.atan2(co[1], co[0]))
            result = (r, theta)
            print(f"The polar coordinates are: Modulus = {r:.2f}, Angle = {theta:.2f} degrees")
        elif op == 'P':# Convert from polar to cartesian
            x = co[0] * math.cos(math.radians(co[1]))
            y = co[0] * math.sin(math.radians(co[1]))
            result = (x, y)
            print(f"The cartesian coordinates are: x = {x:.2f}, y = {y:.2f}")
        else:
            result = "Invalid operation"

        return result
    
def main():

    co = input("Enter the coordination type (C for cartesian or P for polar): ").upper()
    if co not in ['C', 'P']:
        print("Invalid coordination type. Please enter 'C' or 'P'.")
        return  
    cn = input("Enter the complex number, with its coordenates separeted by ',':").split(',')
    
    converter = Complex_converter(cn, co) # Create an instance of Complex_converter
    result = converter.calculate() # Perform the conversion

if __name__ == "__main__":

    main()