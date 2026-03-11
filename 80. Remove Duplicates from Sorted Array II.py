"""
80. Remove Duplicates from Sorted Array II
Medium
Topics
premium lock icon
Companies
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""
nums = [1,1,1]

k= 0
_len = len(nums)
print(_len)
if _len>=2:
    i= nums[0]
    j= nums[1]
else:
    i,j = nums[0], nums[0]

for x in range(_len):
    print(x) # note that the range starts from 0
    k+=1
    if x>=2:
        print( i, j, nums[x-1])
        if nums[x]==i and nums[x]==j:
            print(i,j, "pos ",x)
            nums[x]= 999999
            k-=1
        else:
            i,j = j,nums[x]

print( nums, k)
if 999999 in nums:
    while 999999 in nums:
        nums.remove(999999)
print( nums, k)
# return k

"""
Good Solution from leet
        k = 2

        for i in range(2, len(nums)):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
            else:
                pass
        return k
"""