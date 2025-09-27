# Calculator:

def sum():
    try:
        usr_inp_1 = int(input("Enter the 1st number here: "))
        usr_inp_2 = int(input("Enter the 2nd number here: "))
        print(f"Total sum is : {usr_inp_1+usr_inp_2}")
    except ValueError:
        print("Please Enter a Number!")

def sub():
    try:
        usr_inp_1 = int(input("Enter the 1st number here: "))
        usr_inp_2 = int(input("Enter the 2nd number here: "))
        print(f"Total substitution is : {usr_inp_1-usr_inp_2}")
    except ValueError:
        print("Please Enter a Number!")

def mul():
    try:
        usr_inp_1 = int(input("Enter the 1st number here: "))
        usr_inp_2 = int(input("Enter the 2nd number here: "))
        print(f"Total multiplication is : {usr_inp_1*usr_inp_2}")
    except ValueError:
        print("Please Enter a Number!")

def div():
    try:
        usr_inp_1 = int(input("Enter the 1st number here: "))
        usr_inp_2 = int(input("Enter the 2nd number here: "))
        print(f"Total divition is : {usr_inp_1/usr_inp_2}")
    except ValueError:
        print("Please Enter a Number!")
    except ZeroDivisionError:
        print("Cannot Divide By Zero!")

def pow():
    try:
        usr_inp_1 = int(input("Enter the number here: "))
        print(f"Square is : {usr_inp_1**2}")
    except ValueError:
        print("Please Enter a Number!")

def mod():
    try:
        usr_inp_1 = int(input("Enter the 1st number here: "))
        usr_inp_2 = int(input("Enter the 2nd number here: "))
        print(f"Total modulas is : {usr_inp_1%usr_inp_2}")
    except ValueError:
        print("Please Enter a Number!")
            

def calculator():
    print("Welcome To Simple Python Calculator")
    print("Please Select The Operation You Want to do: Enter any of this Sum(+), Substitution(-), Multiplication(*), Division(/), pow(^2), modulas(%)")
    user_input = input("")
    if user_input == "+" :
       sum()
    elif user_input == "-":
       sub()
    elif user_input == "*":
        mul()
    elif user_input == "/":
        div()
    elif user_input == "^2":
        pow()
    elif user_input == "%":
        mod()
    else:
        print("Please Enter a Valid Operation")

    while True:
        calculator()
        ask = input("Do you want to continue? (yes/no)")
        if ask == "yes":
            continue
        else:
            print("Thank your for using me!!!")
            break

calculator()