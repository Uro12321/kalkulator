firstNum = int(input("Vnesi prvo stevilo: "))
secondNum = int(input("Vnesi drugo stevilo: "))
operation = input("Izberi operacijo +,-,*,/ : ")

if operation == "+":
    print(firstNum+secondNum)
elif operation == "-":
    print(firstNum-secondNum)
elif operation == "*":
    print(firstNum*secondNum)
elif operation == "/":
    print(firstNum/secondNum)

