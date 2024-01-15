def selection_sort(nums):
    for outer_loop in range(len(nums)):
        min_idx = outer_loop
        for inner_loop in range(outer_loop+1, len(nums)):
            if nums[inner_loop] < nums[min_idx]:
                min_idx = inner_loop
        nums[outer_loop], nums[min_idx] = nums[min_idx], nums[outer_loop]
        print(f"Step {outer_loop+1}: {nums}")
    return nums

nums = list(map(int, input("Enter numbers separated by space: ").split()))
sorted_nums = selection_sort(nums)
print("Sorted array:", sorted_nums)