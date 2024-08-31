def read_numbers(file_path):
    with open(file_path, 'r') as file:
        nums = [int(line.strip()) for line in file]
    return nums


def min_moves_to_equal_elements(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    moves = sum(abs(num - median) for num in nums)
    return moves


input_file = input('Путь к файлу с массивом: ')
nums = read_numbers(input_file)

result = min_moves_to_equal_elements(nums)
print(result)
