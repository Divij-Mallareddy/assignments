def interest(p,t,r):
    I = p*t*r/100
    print(I)
def rectangle(l,w):
    area = l*w
    perimeter = (l+w)*2
    print("Area of rectangle: ",area)
    print("Perimeter of rectangle: ",perimeter)
def speed_calucation(u,t,a):
    s = u*t + 1 / 2*a*t**2
    print("displacement of the object: ",s)
def celcius_to_fahrenheit(C):
    F = C*(9/5) + 32
    print("Temperature in farenheit: ",F)
def BMI(weight,height):
    BMI = weight/height**2
    print("Your BMI: ",BMI)
def ecommerce_app(p,n,t):
    tax = (p*n)*(t)/100
    print("Your total amount is : ",tax + (p*n))
def EMI(p,r,n):
    r = r/(12*100)
    EMI = p * r * (1+r)**n/((1+r)**n-1)
    print("your EMI is: ",EMI)
