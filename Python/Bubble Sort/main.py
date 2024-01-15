def bubble_sort(nums):
    nums_size = len(nums)
    for outer_loop in range(nums_size):
        for inner_loop in range(nums_size-1):
            if nums[inner_loop] > nums[inner_loop+1]:
                nums[inner_loop], nums[inner_loop+1] = nums[inner_loop+1], nums[inner_loop]
        print(f"Step {outer_loop+1}: {nums}")
    return nums

nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("Sorted array:", bubble_sort(nums))