#error is any problem in a program
#exception
#syntax error (break Python's grammar rules)

if 5 > 3: # if you forget to put : at last syntax error
    print("Hello")


#IndentationError (space error)
x = 10

if x > 5:
    print(x)

#Runtime Error (Exception) [happens while the program is running]
print(10/10) #zerodivisionerror if divide by 0



#AttributeError
#number = 10
#number.append(20)


#Logical Error (python gives no error but answer is wrong)
length = 20
width = 10
area = length + width #wrong as area = lenght * width
print(area)


#Traceback (read all error)

#Exception Handling(handle runtime errors)
#TRY (block contains the code that might cause an error)
#EXCPET (if error happens inside try, Python jumps to except)
try:
    number = int(input("Enter a number: "))
    print(100 / number)

except:
    print("Cannot divide by zero.")

#ELSE (block runs only if NO exception occurs)

#FINALLY always runs, whether an error happens or not

#RAISE lets YOU create an exception intentionally

marks = -10
if marks < 0:
    raise ValueError("Marks cannot be negative.")


#Custom Exceptions own error
class AgeError(Exception):
    pass
age = 15
if age < 18:
    raise AgeError("Not eligible.")



try:
    age = int(input("Enter age: "))
    if age < 18:
        raise ValueError("Too young.")
except ValueError as error:
    print(error)
else:
    print("Access Granted")

finally:
    print("Program Ended")
