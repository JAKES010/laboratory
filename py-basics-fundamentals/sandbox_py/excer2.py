def rotate_right(nums: list, k: int) -> None:
    if not nums:
        return
    n = len(nums)
    k %= n 
    nums[:] = nums[-k:] + nums[:-k]


# --- Verification ---
data = [1, 2, 3, 4, 5]
rotate_right(data, 2)
print("After k=2 rotation:", data)  # Output: [4, 5, 1, 2, 3]

# Test Edge Case: k > len(data)
data2 = [10, 20, 30]
rotate_right(data2, 4)  # 4 % 3 = 1 rotation
print("After k=4 rotation:", data2)  # Output: [30, 10, 20]