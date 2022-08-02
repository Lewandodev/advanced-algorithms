

def recursive_binary_search(lsit,target):
    if len(lsit) == 0:
            return False
    else:
        middle = (len(lsit) // 2)

        if lsit[middle] == target:
            return True
        else:
            if lsit[middle] < target:  # function will be called recursively on a slice of our list
                return recursive_binary_search(lsit[middle + 1:],
                                                   target)  # slices work by using square brackets and defining what part of list we want to take
                # additionally we can modify wether we want to reverse the list (list[::-1]) or take elemn. which occur every few numbers (list[::2])
            else:  # not typing any number after colons suggests we either want to start from beginning or go till the end (or not modify at all if type nothing after second col)
                return recursive_binary_search(lsit[:middle], target)

# recursive binary search calls itself inside the body of function
# python prefers iterative solution rather than recursive

def verify(result):
    print('Target found: ', result)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = recursive_binary_search(numbers, 123)
verify(result)

result = recursive_binary_search(numbers, 4)
verify(result)

