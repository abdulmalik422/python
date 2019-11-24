# Name: Abdul Malik 
# Email: abdulmalik422@gmail.com

#Program 1:
print('1) Make a calculator using Python with addition, subtraction, multiplication, division and power.');

num1 = int(input('Enter Number One:'))
num2 = int(input('Enter Number Two:'))
operator = raw_input('Enter Operator:')
result = 0

if operator == '+':
    result = num1 + num2
    print(result)
elif operator == '-':
    result = num1 - num2
    print(result)
elif operator == '*':
    result = num1 * num2
    print(result)
elif operator == '/':
    result = num1 / num2
    print(result)
elif operator == '**':
    result = num1 ** num2
    print('The Power Expression is: '+ str(num1) +'**'+ str(num2))
    print(result)
else:
    print('Please enter correct operator.')


#Program 2
print('2) Write a program to check if there is any numeric value in list using for loop')

mylist = [1,'abc',34,'dfc']
isNumeric = False;
for index in mylist:
    if(type(index)== int):
        isNumeric = True
        print ("Numeric Value is ", index)
if(isNumeric):
    print('Numeric values Exist is the List')
else:
    print('Numeric value doesnot Exist in the List')


#Program 3
print('3) Write a Python script to add a key to a dictionary')
dict = { 'a':2, 'b':4 }
dict.update({'c':6})
print(dict)


#Program 4
print('4) Write a Python program to sum all the numeric items in a dictionary')
dictItem = { 'num1':3, 'num2':4, 'num3':6 }
sumValues = sum(dictItem.values())
print(sumValues)


#Program 5
print('5) Write a program to identify duplicate values from list')
listofEle = [10, 5, 4, 3, 7, 4, 2 , 10]
uniqueList = []
dupList = []
for elem in listofEle:
        if elem not in uniqueList:
            uniqueList.append(elem)  # unique List
        else:
            dupList.append(elem)  # duplicate List
print(dupList)


#Program 6
print('6) Write a Python script to check if a given key already exists in a dictionary')
dupList = {'a':3,'b':5,'c':7,'d':8}
inputVal = 'a'
if inputVal in dupList:
    print('key is present in the dictionary')
else:
    print('Key is not present in the dictionary')


