#Advanced qucik sort is combination of 2 algorithms: quick sort and insertion sort
#combination of qucik and insertion sort will create very efficient algorithm regardless of the size of input
#with the time complexity of O(n^2)
#(as insertion sort is better for small arrays and qucik sort for large arrays)



#Algorithm will consist of auxiliary fucntions (qucik sort and insertion sort) and the main advanced sort algorithm
#the main idea of the algorithm will be recursively checking the size of input array and deciding whether we will use qucik sort or insertion sort on array portion
#according to some threshold value, since insertion sort will be implemented its best to set the threshold value to a small number because insertion sort works best
#for such arrays


#we will need to modify both insertion and qucik sort functions for this advamced algorithm to work, each of the functions will have 3 values


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



#quick sort function
#for advanced qucik sort we will be using 2 part qucik sort function instead of the single function one


#partition function
def partition(arr,prime,utmost): #
    pivot=arr[utmost]
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

