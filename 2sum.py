#Two sum problem

def twoSum(nums, target):
    nums = sorted(nums)

    for i in xrange(len(nums)-2):
        print 'i---', i
        for j in xrange(len(nums)-1,0,-1):
            if i < j:
                print 'j----',j
                print nums[j]
                print nums[i]
                sum = nums[i] + nums[j]
                if sum > target:
                    j -= 1
                elif sum < target:
                    i += 1
                else: return [i,j]

print twoSum([2,6,1,9,10],19)



