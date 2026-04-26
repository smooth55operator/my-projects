def func (numbers):
    total_sum =sum(numbers)
    sorted_nums = sorted(numbers)
    length= len(sorted_nums)
    mean = total_sum/length
    mid = length//2
    if length%2==0:
        median = (sorted_nums[mid-1] + sorted_nums[mid])/2
    else:
        median = sorted_nums[mid]
    return mean, median
numbers= [15,4,7,3,2,9,11]
mean, median = func(numbers)
print(f'Mean: {mean}, Median: {median}')
