

# solution.py
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i
    return [nums, target] 
    print(nums, target)     
# This function finds two indices in the list 'nums' such that their values add up to 'target

