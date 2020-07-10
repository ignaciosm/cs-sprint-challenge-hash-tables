def intersection(arrays):
    length = len(arrays)
    combined_array = []
    result = []

    for i in arrays:
        combined_array = combined_array + i

    arr_dict = {}

    for i in combined_array:
        if i not in arr_dict:
            arr_dict[i] = 1
        else:  # already in dict
            arr_dict[i] = arr_dict[i] + 1
            if arr_dict[i] == length:
                result.append(i)

    return result


if __name__ == "__main__":
    # arrays = [
    #     [1, 2, 3, 4, 5],
    #     [12, 7, 2, 9, 1],
    #     [99, 2, 7, 1]
    # ]

    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
