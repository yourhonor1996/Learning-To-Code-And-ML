def func1(fList:list):
    for i,item in enumerate(fList):
        if(i>0):
            print(f'Curren Number {int(fList[i])} Previous Number {int(fList[i-1])} Sum: {int(fList[i])+int(fList[i-1])}')
        
        
inputList = input('Enter the list items seperated bu space: ').split()

func1(inputList)