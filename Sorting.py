def bubble_sort(): #Bubble sort
    n=int(input('How many elements are there in the list: '))
    x = []
    for i in range(n):
        s = int(input('Enter element: '))
        x.append(s)
    print('Original list is: ', x)
    l = len(x)
    for j in range(l):
        for k in range(0, l-j-1):
            if x[k] < x[k+1]:
                x[k+1], x[k] = x[k], x[k+1]
    print('list ater sorting: ', x)
    
def selection_sort(): #Selection sort 
    x=[]
    n = int(input('Enter number of elements: '))
    for i in range(0, n):
        ele = int(input('Enter an element: '))
        x.append(ele)
    l = len(x)
    for i in range(l):
        for j in range(i+1, l):
            if x[i]>x[j]:
                x[i], x[j] = x[j], x[i]
    print(x)

def insertion_sort(): #insertion sort
    x=eval(input("Enter a list: "))
    for j in range(1,len(x)):
        z=x[j]
        for i in range(j-1,-1,-1):
            if z<x[i]:
                x[i+1]=x[i]
            elif z>x[i]:
                x[i+1]=z
                break
            x[i]=z
    print(x)

def merge_sort(): #merge sort
    x=eval(input("Enter ascending list: "))
    y=eval(input("Enter descending list: "))
    z=[]
    j=len(x)-1
    i=0
    while True:
        if y[i] > x[j]:
            z.append(y[i])
            i=i+1
        else:
            z.append(x[j])
            j=j-1
        if i >(len(y)-1) or j <0:
            break
    if i <=(len(y)-1):
        z.extend(y[i:])
    if j >=0:
        z.extend(x[j::-1])
    print(z)

while True: #Menu Driven Program
    ch = int(input(":::::::::Sorting Options:::::::::\n\t1. Bubble Sort\n\t2. Selection Sort\n\t3. Insertion Sort\n\t4. Merge Sort\n\t5. Exit\n\nEnter choice: "))
    if ch==1:
        bubble_sort()
    elif ch==2:
        selection_sort()
    elif ch==3:
        insertion_sort()
    elif ch==4:
        merge_sort()
    elif ch==5:
        exit()
    else:
        print('Invalid input!')
        pass
