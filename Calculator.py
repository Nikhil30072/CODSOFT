#calculator 
def calculator():
    print("calculator")
    print("addition")
    print("Subtraction")
    print("Multiplication") 
    print("Division")
    print("exit")
    while True:
        try: 
            a=int(input("enter the choice from 1-5:" )) 
            if a in [1,2,3,4]:
                b=int(input("enter First Number:"))
                c=int(input("enter Second number:"))
                if a==1: 
                    print(f'Addition of two numbers {b} and {c} is:',b+c) 
                elif a==2: 
                    print(f'subtraction of two numbers {b} and {c} is:',b-c) 
                elif a==3: 
                    print(f'multiplication of two numbers {b} and {c} is:',b*c) 
                elif a==4: 
                    if c!=0:
                        print(f'Division of two numbers {b} and {c} is:',b/c)
                    else:
                        print("not divisible") 
            elif a==5:
                print("Exit Calculator!,Take Care")
                break 
            else: 
                print("invalid choice")
        except ValueError:
            print("enter a valid value")
calculator()
