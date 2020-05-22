num=int(input("enter size of list: "))
list1=[int(input())for x in range(num)]
print("unsorted list :",list1)
for j in range(len(list1)-1):
    for i in range(len(list1)-1):
        if list1[i]>list1[i+1]:
            list1[i],list1[i+1]=list1[i+1],list1[i]
print("sorted list is : ",list1)
          
