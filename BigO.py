#Question 1
#computes the product of a and b
def product(a,b):
  sum=0
  for i in range (0,b):
      sum+=a
  return sum
  #The runtime for this function is b, because the loop iterates b times

#Question 2
#returns a to the power of b    -> a^b
def power(a,b):
    if(b<0):
        return 0
    elif(b==0):
        return 1
    else:
        return a * power(a,b-1)
    #There will be b-1 recursive calls of power, so the runtime of the function is O(b)

#Question 3
#returns a%b
def mod(a,b):
    if(b<=0):
        return -1
    div=a/b
    print(div)
    return a - div*b
    #The runtime for this function is O(1), constant time because it does a constant calculation

#Question 4
#perfroms integer division
def div(a,b):
    count=0
    sum=b
    while sum<=a:
        sum+=b
        count+=1
    return count
# The runtime for this function is O(a/b) or O(count), this is because the loop will run "count" times or the number of times that b goes into a (a/b)

#Question 5
# The following code computes the [integer] square root of a number. If the number is not a
# perfect square (there is no integer square root), then it returns -1. It does this by successive
# guessing. If n is 100, it first guesses SO. Too high? Try something lower - halfway between 1
# and SO. What is its runtime?

def sqrt(n):
    return sqrt_helper(n,1,n)

def sqrt_helper(n, min,max):
    if(max<min):
        return -1
    guess=(min+max)/2

    #found it
    if(guess*guess ==n):
        return guess
    #too low
    elif guess*guess < n:
        return sqrt_helper(n, guess+1, max)
    #too high
    else:
        return sqrt_helper(n, min, guess-1)
#The runtime of the function is O(log(n)) because it is performing a binary search
# 2^x = n  ,   log(2^x) = log(n)   ,    x= log(n) , refer to pg 44 or 55

#Question 6
# The following code computes the [integer] square root of a number. If the number is not
# a perfect square (there is no integer square root), then it returns -1. It does this by trying
# increasingly large numbers until it finds the right value (or is too high). What is its runtime?

def sqrt2(n):
    for guess in range(1,n):
        if guess * guess <=n:
            if guess * guess == n:
                return guess
    return -1
#runtime for this funciton is the value of guess, in this case it is O(sqrt(n)), at worst it is n

#Question 7:
# If a binary search tree is not balanced, how long might it take (worst case) to find an element
# in it?

#Answer: The worst case runtime would be O(n), it would traverse through all the nodes

#Question 8
# You are looking for a specific value in a binary tree, but the tree is not a binary search tree.
# What is the time complexity of this?
# O(n) because you would have to traverse through all nodes

#Question 9
# The appendToNew method appends a value to an array by creating a new, longer array and
# returning this longer array. You've used the appendToNew method to create a copyArray
# function that repeatedly calls appendToNew. How long does copying an array take?

# int[] copyArray(int[] array) {
#     int[] copy= new int[0];
#     for (int value : array) {
#         copy= appendToNew(copy, value);
#     }
#     return copy;
# }
# int[] appendToNew(int[] array, int value) {
#     // copy all elements over to new array
#     int[] bigger= new int[array.length + 1];
#     for (int i= 0; i < array.length; i++) {
#         bigger[i] = array[i];
#     }
#     // add new element
#     bigger[bigger.length - 1] = value
#     return bigger;

#The run time of this function is O(n^2) where n is the size of the array

#Question 10
#The following code sums the digits in a number. What is its big O time?
def sumDigits(n):
    sum=0
    while(n>0):
        sum+= n%10
        n/=10
    return sum
#The function runs for however long the number is, 3 digit number -> 3 times, thus the runtime O(log(n)) because
# A number with d digits can have a value up to 10^d, so 10^d=n    ->   d=(log(n))


#Question 12
# The following code computes the intersection (the number of elements in common) of two
# arrays. It assumes that neither array has duplicates. It computes the intersection by sorting
# one array (array b) and then iterating through array a checking (via binary search) if each
# value is in b. What is its runtime?

# int intersection(int[] a, int[] b) {
#     mergesort(b);
#     int intersect = 0;
#     for (int x : a) {
#         if (binarySearch(b, x) >= 0) {
#             intersect++;
#         }
#     }
#     return intersect;
# }

# Where b is the length of array b, a is the length of array a. The runtime of this function is O(b*log(b) + a*log(b)) or O(log(b)[a*b])
# This is because it takes blog(b) for mergesort on b, the you iterate through all the elements of array a -> a and run a binary search on b -> log(b)
# Thus you get a runtime of blog(b) + alog(b)

def main():
    #print(product(3,5))
    #print(power(2,5))
    #print(mod(32,5))
    print(sqrt(81))
    print(sqrt2(64))
    print(sumDigits(137))


main()
