#various methods of getting n-th number rom fibonacci sequence fast


#finding n-th fibonacci number via array method
def fibo_arr(n):

    #base cases
    if n==0:
        return 0
    elif n==1:
        return 1

    f=(n+1)*[0] #we create array containing n+1 copies of 0
    f[1]=1

    for i in range(2,n+1):#we will be iterating through indexes from 2 (since 1 and 0 are described) in order to fill them with appropriate values
        f[i]=f[i-1]+f[i-2] #standard fibonacci number calculation pattern
    #now we have array with all the number corresponding to n-th values of fibonacci

    return f[n] #last element is the one we are looking for

#linear runtime O(n)
print('400 number in fibonacci :',fibo_arr(400))
