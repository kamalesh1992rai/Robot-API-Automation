try:

    user_input1= input("please enter first number : - ")
    user_input2= input("please enter second number : - ")
    c=int(user_input1) + int(user_input2)
    print(c)

except:
    print("Your input is incorrect, please enter correct data")

finally:
    print("This code i want to excute always at the end")


