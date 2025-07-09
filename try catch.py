def divide(a,b):
    try:
        result = a/b
        return result
    except ZeroDivisionError:
        return"the number is not divisible by Zero"
print(divide(5,3))
print(divide(8,0))