# Exercise 3: Finding the Largest Number
def find_largest_number(array_of_numbers: list[int]) -> int:
    if not array_of_numbers:
        raise ValueError("The array cannot be empty")
    
    largest: int = array_of_numbers[0]

    for i in range(1, len(array_of_numbers)):
        if array_of_numbers[i] > largest:
            largest = array_of_numbers[i]
    
    return largest

if __name__ == "__main__":
    find_largest_number()