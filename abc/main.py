from src.add import add
from src.multi import multi
from src.div import div
from src.sub import sub

num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
choice = input("Enter choice + - / *  : ")



def main():         #funtion definition / entry point /orchestrator
    if choice == '+' :
        sum = add(num1,num2)
        print(sum)
    elif choice == '-':
        minus = sub(num1,num2)
        print(minus)
    elif choice == '*':
        multiplication = multi(num1,num2)
        print(multiplication)
    elif choice == '/' :
        division = div(num1,num2)
        print(division)
    else :
        print("Enter correct choices ")
            
main()
