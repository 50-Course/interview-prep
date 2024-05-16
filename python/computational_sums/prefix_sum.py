
def prefix_sum(array: list[int]) -> list[int]:
    sum =  [0] * len(array)

    sum[0] = array[0] # populate forward, first index to first value of input array
    for current in range(1, len(array)): # begin att the next value
        sum[current] = sum[current -  1] + array[current]
    return sum
    


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    print(prefix_sum(array))
    assert len(prefix_sum(array)) ==  len(array), "Lengths are never the same"
    print(len(prefix_sum(array)))
    print(len(array))
