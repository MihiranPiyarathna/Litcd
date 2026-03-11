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
# idea from leet
0(N) EASY TO UNDERSTAND SOLUTION

Pratay Nandy
50 Days Badge 2024
80218
Sep 19, 2023
Array
Two Pointers
C++
PLEASE UPVOTE MY SOLUTION IF YOU LIKE IT
CONNECT WITH ME
https://www.linkedin.com/in/pratay-nandy-9ba57b229/
https://www.instagram.com/pratay_nandy/
Approach
The goal of this function is to remove duplicates from the nums vector while keeping at most two occurrences of any element. The function returns the length of the modified vector after removing duplicates.

Here's the approach implemented in the code:

Initialize an integer variable i to 0. This variable will keep track of the current position in the modified nums vector.

Use a for loop to iterate through each element ele in the nums vector using the range-based for loop.

Inside the loop, check the following conditions:

i == 0: This condition ensures that the first element is always included in the modified vector.
i == 1: This condition ensures that the second element is always included in the modified vector.
nums[i-2] != ele: This condition checks if the current element ele is not the same as the element two positions before the current position i. This ensures that only two occurrences of any element are included in the modified vector.
If any of the above conditions are met, copy the current element ele to the nums[i] position in the modified vector, and increment i by 1 to move to the next position.

Repeat this process for all elements in the nums vector.

Finally, return the value of i, which represents the length of the modified vector with duplicates removed.

This approach effectively modifies the nums vector in place, removing duplicates while keeping at most two occurrences of each element. The function returns the length of the modified vector, which can be used to access the unique elements in the first i positions of the vector

Complexity
Time complexity:0(N)
Space complexity:0(1)
"""

# nums = [0,0,1,1,1,1,2,3,3]
# nums = [1,1,1]
nums = [1,1,1,2,2,3]
wrt= 0
for rdid in range( len(nums)):
    if rdid ==0 or rdid==1 or nums[rdid]!=nums[wrt-2]: # note the use of wrt-2 instead of rdid
        nums[wrt]= nums[rdid]
        print("write to",wrt, nums)
        wrt+=1
    else:
        print("not writing")   
print(wrt, "to end consider ",nums)