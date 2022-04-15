def MySumBonus(numbers):
    if (numbers == None):
        return 0
    result = 0
    if (len(numbers) == 0):
        return 0
    else:
        number = numbers[0]
        del numbers[0]
        result += number + MySumBonus(numbers)
    return result


# Tests :
# -------

numbers = [1,2]
result = MySumBonus(numbers)
print("EXPECTED VALUE : 3")
print("OBTAINED VALUE :", result)
print("--------")

numbers = [1,2,3,4,5]
result = MySumBonus(numbers)
print("EXPECTED VALUE : 15")
print("OBTAINED VALUE :", result)
print("--------")

numbers = [-1,2,3]
result = MySumBonus(numbers)
print("EXPECTED VALUE : 4")
print("OBTAINED VALUE :", result)
print("--------")

numbers = []
result = MySumBonus(numbers)
print("EXPECTED VALUE : 0")
print("OBTAINED VALUE :", result)
print("--------")

numbers = None
result = MySumBonus(numbers)
print("EXPECTED VALUE : 0")
print("OBTAINED VALUE :", result)
print("--------")