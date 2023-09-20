def candy(ratings):
    """
    There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

    You are giving candies to these children subjected to the following requirements:

    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.
    Return the minimum number of candies you need to have to distribute the candies to the children.
    """
    candies = [1] * len(ratings)
    for i in range(len(ratings) - 1):
        if ratings[i + 1] > ratings[i]:
            candies[i + 1] = candies[i] + 1
    # print(candies)
    for i in range(len(ratings) - 1, 0, -1):
        if ratings[i - 1] > ratings[i]:
            candies[i - 1] = candies[i] + 1
    print(candies)
    return sum(candies)


candy([1, 2, 2])

# can = [1, 1, 1]
