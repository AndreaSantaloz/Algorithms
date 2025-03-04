

def iteration_search(array, number):
    for i in range(0, len(array)):
        if array[i] == number:
            return "You find the number "+str(number)
    return "You don't find the number "+str(number)


if __name__ == "__main__":
    print(iteration_search([89, 10, 33, 45], 45))