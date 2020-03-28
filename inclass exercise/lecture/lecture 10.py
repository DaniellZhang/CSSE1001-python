##def int_exception1(in_num):
##    num= input('Enter a number:')
##    try:
##        num = int(num)
##        return in_num/num
##    except Exception as e:
##        print ('Error: ', str(e))
##        return -1
##
##def int_exception2(in_num):
##    num= input('Enter a number:')
##    try:
##        num = int(num)
##        return in_num/num
##    except ValueError:
##        print('That is not a number')
##    except ZeroDivisionError:
##        print('Division by zero')
##    except Exception as e:
##        print('Error:', str(e))
##    return -1
##
##def addNumber():
##    num1= input('Enter a number1:')
##    num2= input('Enter a number2:')
##    try:
##        num1 = int(num1)
##        num2 = int(num2)
##        return num1 + num2
##    except Exception as e:
##        print ('Error: ', str(e))
##        return -1
##
##def function1(number1):
##    if number == 0:
##        raise ZeroDivisionError('Divide by zero')
##    return 15/number
##
##try:
##    function1(0)
##except Exception:
##    print('Divide by zero')
##
##
x= 12
y =24

print("First no is {:_>10}, second no is {}".format(x,y))
