def min_max(numbers: list[int]) -> tuple[int, int]:
    return min(numbers), max(numbers)



if __name__ == "__main__":

    result = min_max([5, 2, 9, 1, 7])
    print(result)