import random
import unittest

def split(items, ratios):
    total_items = len(items)
    result = []
    start_index = 0

    for ratio in ratios:
        num_items = max(1, round(total_items * ratio))
        result.append(items[start_index:start_index + num_items])
        start_index += num_items

    return result

class TestSplitFunction(unittest.TestCase):
    def test_split_example1(self):
        items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ratios = [0.5, 0.4, 0.1]
        expected_output = [[1, 2, 3, 4, 5], [6, 7, 8, 9], [10]]
        self.assertEqual(split(items, ratios), expected_output)
    


if __name__ == '__main__':
    unittest.main()

