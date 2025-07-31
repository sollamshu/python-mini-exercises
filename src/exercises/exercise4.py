# Exercise 4: Sort Numbers Ascending
def sort_numbers_ascending(array_of_numbers: list[int]) -> list[int]:
    array_of_numbers_copy = array_of_numbers[:]
    array_of_numbers_copy.sort()
    
    return array_of_numbers_copy

if __name__ == "__main__":
    sort_numbers_ascending()