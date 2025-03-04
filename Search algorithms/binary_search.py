def binary_search(numbers, number, first, last):
    mild_number = numbers[(first + last // 2)]
    if mild_number == number:
        print("The number was found")
    else:
        if mild_number > number:
            binary_search(numbers, number, first, numbers.index(mild_number))
        else:
            binary_search(numbers, number, numbers.index(mild_number), last)


if __name__ == "__main__":
    array = [10, 45, 80, 90, 100, 120, 130, 180, 200]
    binary_search(array, 45, 0, len(array)-1)