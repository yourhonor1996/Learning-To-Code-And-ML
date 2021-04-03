n = input()
list_of_people = input().split(' ')

def say_hello (l:list):
    for i, person in enumerate(l):
        for j in range(i-1,-1,-1):
            print(f'{person}: salam {l[j]}!')

def say_goodbye(l:list):
    for i, person in enumerate(l):
        print(f'{person}: khodafez bacheha!')
        for j in range(i+1, len(l)):
            print(f'{l[j]}: khodafez {person}!')
            
    
    
say_hello(list_of_people)
say_goodbye(list_of_people)