#binary search works only for sorted array of elements
#we can sort an array either via built-in functions or our own functions

Array=[59,21,5,2,44,125,90,10,1,3,8,64,212,551,30,31,93,39,59,60,11,15,14,28]

sortedlist_auto=sorted(Array)

def quciklognsort(array):
    lower=[]
    equal=[]
    higher=[]

    if len(array)>1:
        pivot=array[0]
        for i in array:
            if i>pivot:
                higher.append(i)
            elif i==pivot:
                equal.append(i)
            else:
                lower.append(i)

        return quciklognsort(lower)+equal+quciklognsort(higher)
    else:
        return array

#alternatively it could be replaced with array[i] (and new helping value like place=array[i])
#if so the for loop iterations are within range of (0,len(array))
'''        for i in range(0,len(array)):
            tab=array[i]
            if tab>pivot:
                higher.append(tab)
            elif tab==pivot:
                equal.append(tab)
            else:
                lower.append(tab)'''
#rest of the function is same


sortedlist_ownfunction=quciklognsort(Array)

print('array sorted by built-in function:',sortedlist_auto)
print('array sorted by user created function:',sortedlist_ownfunction)

#in binary search we will be looking for our target value by dividing our list in halfs via finding the middle
#next we will look if the target value is higher or lower than the middle point of our array
#we will be searcging for the target value in the correct half and repeat the process of dividing in half till we find target

def binary_search(list,targetval):
    first=0
    last=len(list)-1 #position numbers start at 0 making it first elem. therefore last elm. is len(your list)-1

    while first<=last:
        middle=(first+last)//2

        if list[middle]==targetval:
            return targetval
        elif list[middle]<targetval:
            first=middle+1
        else: #list[middle]>targetval
            last=middle-1

    return None
