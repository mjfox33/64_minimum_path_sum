from code_64_minimum_path_sum import Solution

def test_example_1():
    s = Solution()
    assert s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]) == 7

def test_example_2():
    s = Solution()
    assert s.minPathSum([[1,2,3],[4,5,6]]) == 12