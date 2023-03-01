import math

def freeFall(var) :
    #var is the variable to find
    var = var.lower()
    match var :
        case "f" :
            #F = (p*d*A)/2 * v^2
            p = float(input("Enter air density: "))
            d = float(input("Enter drag coefficient: "))
            A = float(input("Enter the area of the object: "))
            v = float(input("Enter the velocity: "))
            F = ((p*d*A) / 2) * v**2
            print("Drag is: ", F)
        case "p" :
            d = float(input("Enter drag coefficient: "))
            A = float(input("Enter the area of the object: "))
            v = float(input("Enter the velocity: "))
            F = float(input("Enter drag: "))
            p = (2*F) / (d*A*v**2)
            print("Air density is: ")
        case "d" :
            A = float(input("Enter the area of the object: "))
            v = float(input("Enter the velocity: "))
            F = float(input("Enter drag: "))
            p = float(input("Enter air density: "))
            d = (2*F) / (A*p*v**2)
            print("Drag coefficient is: ", d)
        case "a" :
            p = float(input("Enter air density: "))
            d = float(input("Enter drag coefficient: "))
            v = float(input("Enter the velocity: "))
            F = float(input("Enter drag: "))
            A = (2*F) / (d*p*v**2)
            print("The area of the object is: ", A)
        case "v" :
            p = float(input("Enter air density: "))
            d = float(input("Enter drag coefficient: "))
            F = float(input("Enter drag: "))
            A = float(input("Enter the area of the object: "))
            v = math.sqrt(((2*F) / (d*p)))
            print("The velocity of the object is: ", v)
        case default :
            print("Unable to complete request - aborting...")


var = input("Enter which variable you want to find for air resistance(f,a,p,d,v): ")
freeFall(var)