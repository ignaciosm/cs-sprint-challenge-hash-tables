import math

weights = [4, 6, 10, 15, 16]
length = 5
limit = 21

# Your solution should run in linear time. SO IT'S OK TO LOOP THROUGH THE LIST


def get_indices_of_item_weights(weights, length, limit):
    weights_dict = {}
    index = -1

    # create a hash table with key = weight and value = to index
    # {4: 0, 6: 1, 10: 2, 15: 3, 16: 4}
    for i in weights:
        index += 1
        weights_dict[i] = index
        # print(weights_dict)

    # loop through indexes in weights list and find index of complementary weight (if present)
    for i1 in range(length):
        w1 = weights[i1]
        w2 = limit - weights[i1]
        # get the index of the complement, if not present: None
        i2 = weights_dict.get(w2)

        # print(i2)
        if i2 is not None:
            return [max(i1, i2), min(i1, i2)]

    return None


print(get_indices_of_item_weights(weights, length, limit))
