def suffix_sum(array: list[int]) ->  list[int]:
    result = [0] * len(array)

    result[-1] = array[-1]
    for i in range((len(array)-2), 0, -1):
        result[i] = result[i + 1] + array[i]
    return result

if __name__ == "__main__":
    print(suffix_sum([1, 2, 3, 4, 5]))
    assert len(suffix_sum([1, 2, 3, 4, 5])) == len([1, 2, 3, 4, 5]), "Lengths are never the same"
