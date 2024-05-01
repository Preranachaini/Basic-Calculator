print("Calculator")

def add(x, y):
    return x + y

def sub(x, y):
    return x- y

def multiply(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Error!"
    else:
        return x/y
    
def percentile(x, y):
    return x % y
    
print("Select Operation")
print("1. Add")
print("2. Sub")
print("3. Multiply")
print("4. Div")
print("5. percentile")

if True:
    selected = input("Enter Choice (1/2/3/4/5)")

    if selected in ("1","2","3","4","5"):
        num1 = float(input("Enter the first number: "))        
        num2 = float(input("Enter the secound number: "))

    if selected == "1":
        print("Result:", add(num1, num2))
    
    if selected == "2":
            print("Result:", sub(num1, num2))
   
    if selected == "3":
            print("Result:", multiply(num1, num2))
   
    if selected == "4":
            print("Result:", div(num1, num2))
   
    if selected == "5":
            print("Result:", percentile(num1, num2))



