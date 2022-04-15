from functools import reduce

def addition(nb1, nb2):
    return nb1 + nb2

def MySum(numbers):
    return reduce(addition, numbers)


# Tests :
# -------

# MySum function.

numbers = [1,2,3,4,5]
sum = MySum(numbers)
print("The result of the sum is", sum)
print("-----------------------")

numbers = [-1,1,-2,2,-3,3]
sum = MySum(numbers)
print("The result of the sum is", sum)
print("-----------------------")
