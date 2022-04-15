from functools import reduce

def addition(nb1, nb2):
    return nb1 + nb2

def MySum(numbers):
    if (numbers == None or len(numbers) <= 0):
        return 0
    return reduce(addition, numbers)


# Tests :
# -------

# MySum function.

numbers = [1,2,3,4,5]
sum = MySum(numbers)
print("EXPECTED VALUE : 15")
print("The result of the sum is", sum)
print("-----------------------")

numbers = [-1,1,-2,2,-3,3]
sum = MySum(numbers)
print("EXPECTED VALUE : 0")
print("The result of the sum is", sum)
print("-----------------------")

numbers = []
sum = MySum(numbers)
print("EXPECTED VALUE : 0")
print("The result of the sum is", sum)
print("-----------------------")

numbers = None
sum = MySum(numbers)
print("EXPECTED VALUE : 0")
print("The result of the sum is", sum)
print("-----------------------")
