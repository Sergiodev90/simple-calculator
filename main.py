theMessage =''' 
    Hello my friend how are you I´m going to give a list to do simple operations
    1. sum
    2. divide
    3. substraction
    4. multiplication


    only tell what do you like and after put the numbers 

    and if you want to do the operation with a way more easy put 5

'''

print(theMessage)

Operation = input("put the operation right here: ")


def operations (operation):
     if operation == "5":
          OperationUser = input("put right here your operation")
          convert = OperationUser.replace(" ", "")
          convert = OperationUser.split()
          print(convert)






print("now tell me the numbers")
Number1 = int(input("first Number: "))
Number2 = int(input("second Number: "))

def sum(number1 ,number2 ,operation): 
    if operation == "1":
        result = number1 + number2
        print(result)
    
def divide(number1,number2,operation):
    if operation == "2":
            result =   number1 / number2
            print(result)

def substraction(number1,number2,operation):
     if operation == "3":
          result = number1 - number2
          print(result)
        
def multiplicattion(number1,number2,operation):
     if operation == "4":
          result = number1 * number2
          print(result)


operations(Operation)

multiplicattion(Number1,Number2,Operation)
substraction(Number1,Number2,Operation)
sum(Number1,Number2,Operation)
divide(Number1,Number2,Operation)