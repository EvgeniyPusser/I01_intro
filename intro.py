def max_negative_repr(numbers):
    seen = set(numbers)
    result = -1

    for number in numbers:
        if number > 0 and -number in seen:
            result = max(result, number)

    return result


print(max_negative_repr([100, 4, 1, -1, -4, -100]))
print(max_negative_repr([100, 4, 1, -2]))