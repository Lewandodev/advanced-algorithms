#various methods of getting n-th number rom fibonacci sequence fast


#modyfing standard recursive fibonacci algorithm
#naturally the algorithm is very slow since its redundantly repeats itself while calling
#in order to avoid this we can create a dictionary to cache the values and avoid repeating

fibo_cache={}
def fibonacii_recur(n):
    #if the value we are looking for is in the cache we will return it but first we need to check
    if n in fibo_cache:
        return fibo_cache[n]

    #we will compute the value cahe it then return
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n>1:
        value= fibonacii_recur(n-1)+fibonacii_recur(n-2)
    #store the value
    fibo_cache[n]=value
    return value


print('399 value of sequence:',fibonacii_recur(389))

#getting n-th value of sequence via array method
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
print('\n400 number in fibonacci :',fibo_arr(400))


#there exist however much faster method that posses constant runtime of O(1)
#it's purely mathematical method which uses golden ratio formula

def fib_omega(n):
    from math import sqrt #we import only sqrt function from library as we don't need anything else
    goldenratio=(1+sqrt(5))/2.0 #golden ratio formula
    return int(round(goldenratio**n/sqrt(5)))#we take golden ratio power it to the n and divide by square root of 2 and round it to nearest integer

print('\n1000 number of fibonacci sequence:')
print(fib_omega(1000))

#this is the fastest way of getting n-th fibonacci sequence number
#as we compute only one term without calculating the previous terms

