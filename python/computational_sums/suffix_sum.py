def suffix_sum(array: list[int]) ->  list[int]:
    result = [0] * len(array)

    for i in range(1,  len(array)):
        result[i] = result[i - 1] + array[i - 1]
    return result

if __name__ == "__main__":
    print(suffix_sum([1, 2, 3, 4, 5]))
    assert len(suffix_sum([1, 2, 3, 4, 5])) == len([1, 2, 3, 4, 5]), "Lengths are never the same"
