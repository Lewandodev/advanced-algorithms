#Advanced qucik sort is combination of 2 algorithms: quick sort and insertion sort
#combination of qucik and insertion sort will create very efficient algorithm regardless of the size of input
#with the time complexity of O(n^2)
#(as insertion sort is better for small arrays and qucik sort for large arrays)



#Algorithm will consist of auxiliary fucntions (qucik sort and insertion sort) and the main advanced sort algorithm
#the main idea of the algorithm will be recursively checking the size of input array and deciding whether we will use qucik sort or insertion sort on array portion
#according to some threshold value, since insertion sort will be implemented its best to set the threshold value to a small number because insertion sort works best
#for such arrays


#we will need to modify both insertion and qucik sort functions for this advamced algorithm to work, each of the functions will have 3 values


#some of the variable names will be repeated in further functions, their properties will be constant exmp.:variable arr occurs in all functions and has the same meaning
#modified insertion sort
def insertion_sort(arr,prime,n): #arr is array, prime is the first index, n is size of array but value we will input will be the last index
    for i in range(prime+1,n+1):
        val=arr[i]
        j=i #the "pivot value" of outer loop which checks others

        while j>prime and arr[j-1]>val:
            arr[j]=arr[j-1]
            j-=1
        arr[j]=val

    return arr

aba=[5,3,6,9,1,2,4]
#qucik check if modified insertion sort works
print(aba)
print('insertion sort',insertion_sort(aba,0,6))#or len(aba)-1


print()

#quick sort function
#for advanced qucik sort we will be using 2 part qucik sort function instead of the single function one


#partition function
def partition(arr,prime,utmost): #utmost is last index or length of array-1
    pivot=arr[utmost]#!!!REMINDER VARIABLE PRIME ISN'T PRIME NUMBER IT'S THE "START" OF ARRAY FIRST INDEX !!!
    i=prime
    j=prime

    for i in range(prime,utmost):
        if arr[i]<pivot:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
    arr[j],arr[utmost]=arr[utmost],arr[j]

    return j


#proper qucik sort function

def qucik_sort(arr,prime,utmost):
    if prime<utmost:
        pivot=partition(arr,prime,utmost)
        qucik_sort(arr,prime,pivot-1) #qucik sort of left part
        qucik_sort(arr,pivot+1,utmost) #qucik sort of right part

        return arr

#check if our quick sort works properly

cbc=[9,5,7,1,4,3,2,6,8]
print(cbc)
print('Quick sort:',qucik_sort(cbc,0,len(cbc)-1))




#Advanced qucik sort function (fusion of insertion sort and quick sort)

def advanced_quick_sort(arr,prime,utmost):
    while prime<utmost:
        #If array size is less than our threshold we will use insertion sort
        if utmost-prime+1<10: #10 is our threshold value but it can be any "small" value we could even add it as variable for our function
            insertion_sort(arr,prime,utmost)
            break

        else:#in else case we will recursively call qucik sort
            pivot=partition(arr,prime,utmost)

            if pivot-prime<utmost-pivot:#left part is less than right part of array we sort left
                advanced_quick_sort(arr,prime,pivot-1)
                prime=pivot+1 #we move to the right part of array

            else:#right side is less than left we sort the right part
                advanced_quick_sort(arr,pivot+1,utmost)
                utmost=pivot-1 #we move to the left



ara=[10,12,1,5,17,7,2,3,4,13,8,14,6,15,9,16,19,18,20,11]
print('\nSorting via Advanced qucik sort:')
print('unsorted',ara)
advanced_quick_sort(ara,0,len(ara)-1)
print('sorted:',ara)
