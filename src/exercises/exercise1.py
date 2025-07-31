# Exercise 1: Detecting Two Consecutive Identical Numbers in Array
def contains_consecutive(array_of_numbers: list[int], number_to_find: int = 7) -> bool:
    for i in range(len(array_of_numbers) - 1):
        if array_of_numbers[i] == number_to_find and array_of_numbers[i+1] == number_to_find:
            return True

    return False

if __name__ == "__main__":
    contains_consecutive()