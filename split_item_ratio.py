import random

def split(items, ratios):
    total_items = len(items)
    result = []
    start_index = 0

    for ratio in ratios:
        num_items = round(total_items * ratio)
        if num_items == 0:
            num_items = 1
        result.append(random.sample(items[start_index:], num_items))
        start_index += num_items

    return result

# Example 1
items = [1,2,3,4,5,6,7,8,9,10]
ratios = [0.5, 0.4, 0.1]
result = split(items, ratios)
print(result)




