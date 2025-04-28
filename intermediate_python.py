# backpack = ["pizza", "frozen custard", "apple crisp", "kale chips"] 

# if("pizza" in backpack):
#     print("eating it")

# healthy = ["kale chips", "broccoli", "pizza"]
# backpack = ["pizza", "frozen custard", "apple crisp", "kale chips"] 

# backpack[:] = [item for item in backpack if item in healthy]
# # slice --> [:] keeps same object id, replacing all the data
# print(backpack)

# healthy_backpack = []

# for item in backpack:
#     if item in healthy:
#         healthy_backpack.append(item.upper())
# print(healthy_backpack)

# squares = [i ** 2 for i in range(10)]
# print(squares)

# squares = [i ** 2 for i in range(10) if i % 2 == 0]
# print(squares)

# backpack = ["pizza slice", "pizza slice", "pizza slice"]

# if (backpack.count("pizza slice")< 6):
#     backpack.append("pizza slice")
#     print("You put a slice of pizza in the backpack")
# else:
#     print("How about you go to the gym")
# print(backpack)


# backpack = ["sword", "rubber duck", "slice of pizza", "parachute",
# "sword", "rubber duck", "slice of pizza", "parachute", 
# "sword", "rubber duck", "slice of pizza", "parachute", 
# "sword", "rubber duck", "slice of pizza", "parachute",
# "cannon", "laser cannon", "Canon 90D", "can of soup"]

# counts = [[backpack.count(item), item] for item in set(backpack)]

# print(counts) 


# from collections import Counter
# print(Counter(backpack))


# backpack2 = {"sword", "rubber duck", "slice of pizza", "parachute", "sword"}
# print(backpack2)
# print("sword" in backpack2)

# work_days = ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"]

# # OVERTIME!
# work_days.insert(2, "Wednesday")

# print(work_days)


# work_days = ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"]

# # VACATION DAY!
# work_days.remove("Saturday")
# print(work_days)

# del work_days[0]
# print(work_days)

# # The benefit here is the method returns the element
# work_days = ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"]
# popped = work_days.pop(3)

# print("You removed " + popped)
# print(work_days)


# work_days = ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"]

# del work_days[0:2] #remove first 2
# print(work_days)

# del work_days[-2:] #remove last 2 (start 2 from right and go to end)
# print(work_days)


# backpack = ["pizza slice", "button", "pizza slice", "fishing pole", 
# "pizza slice", "nunchucks", "pizza slice", "pizza slice", "sandwich from mcdonalds"]

# while("pizza slice" in backpack):
#     backpack.remove("pizza slice")
    
# print(backpack)

# # bad!
# backpack = ["pizza slice", "button", "pizza slice", "fishing pole", 
# "pizza slice", "nunchucks", "pizza slice", "pizza slice", "sandwich from mcdonalds"]

# for item in backpack:
#    if(item == "pizza slice"):
#        backpack.remove(item)

# print(backpack) #['button', 'fishing pole', 'nunchucks', 'pizza slice', 'sandwich from mcdonalds']

# backpack = ["pizza slice", "button", "pizza slice", "fishing pole", 
# "pizza slice", "nunchucks", "pizza slice", "pizza slice", "sandwich from mcdonalds"]

# for item in backpack[:]: #uses a copy to keep index
#     if item == "pizza slice":
#         backpack.remove(item)

# print(backpack)

# backpack = ["pizza slice", "button", "pizza slice", "fishing pole", 
# "pizza slice", "nunchucks", "pizza slice", "pizza slice", "sandwich from mcdonalds"]

# backpack[:] = [item for item in backpack if item != "pizza slice"]

# print(backpack)

# backpack = ["pizza slice", "button", "pizza slice", "fishing pole", 
# "pizza slice", "nunchucks", "pizza slice", "pizza slice", "sandwich from mcdonalds"]

# print(backpack)
# backpack.reverse()
# print(backpack)

# backpack = ["pizza slice", "button", "pizza slice", "fishing pole", 
# "pizza slice", "nunchucks", "pizza slice", "pizza slice", "sandwich from mcdonalds"]

# packback = backpack[::-1]
# print(packback)

# backpack = ["pizza slice", "button", "pizza slice", "fishing pole", 
# "pizza slice", "nunchucks", "pizza slice", "pizza slice", "sandwich from mcdonalds"]

# for item in reversed(backpack):
#     print(item)

# backpack = ["pizza slice", "button", "pizza slice", "fishing pole", 
# "pizza slice", "nunchucks", "pizza slice", "pizza slice", "sandwich from mcdonalds"]

# for index in range(len(backpack) // 2):
#     backpack[index], backpack[-index-1] = backpack[-index-1], backpack[index]

# print(backpack)

# work_days = ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"]
# work_days.sort()

# print(work_days)

# numbers = [1, 11, 115, 13, 1305, 43]
# numbers.sort()
# print(numbers)

# numbers = [1, 11, 115, 13, 1305, 43]
# numbers_sorted = sorted(numbers)
# print(numbers_sorted)

# numbers = sorted([1, 11, 115, 13, 1305, 43])
# print(numbers)

# numbers = sorted([1, 11, 115, 13, 1305, 43])
# numbers.reverse()
# print(numbers)


# numbers = [1, 11, 115, 13, 1305, 43]
# print(sorted(numbers, reverse=True))

# letters = ['a', 'A', 'abc', 'ABC', 'aBc', 'aBC', 'Abc']

# print(sorted(letters)) #Capital is considered first
# print(sorted(letters, key=str.lower))

# random = ["a", "A", "aa", "AAA", "HELLO", "b", "c", "a"]
# print(sorted(random, key=len))

# numbers = [1, 54, 76, 12, 111, 4343, 6, 8888, 3, 222, 1, 0, 222, -1, -122, 5, -30]
# print(sorted(numbers, key=str))

# stuff = [True, False, 0, -1, "0", "1", "10", 5 < 30, "20", "2", "5", "9001", "5.5", "6.0", 6]
# print(sorted(stuff, key=float))


# class solution:
#     def twoSum(self, num: list[int], target: int):
#         nums_map = {}
#         num = 2, 7, 11, 15
#         target = 9
#         for i in range(len(num)):
#             complement = target - num[i]
#             if complement in nums_map:
#                 return [nums_map[complement], i]
#             nums_map[num[i]] = i

#         return[]
   
# if __name__ == "__main__":
#     solution = solution()
#     nums = [2, 7, 11, 15]
#     target = 9
#     result = solution.twoSum(nums, target)
#     print(result)  # Should print [0,1]


# class solution:
#     def twoSum(self, nums: list[int], target: int):
#         seen = set()

#         for num in nums:
#             complement = target - num
#             if complement in seen:
#                 return [complement, num]
#             seen.add(num)
#         return[]
    
# if __name__ == "__main__":
#     solution = solution()
#     nums = [3, 5, -4, 8, 11, 1, -1, 6]
#     target = 10
#     result = solution.twoSum(nums, target)
#     print(result)




# from typing import List, Tuple

# class Solution:
#     def allTwoSumPairs(self, nums: List[int], target: int) -> List[Tuple[int, int]]:
#         seen = set()
#         pairs = []

#         for num in nums:
#             complement = target - num
#             if complement in seen:
#                 pairs.append((complement, num))
#             seen.add(num)

#         return pairs
    
# if __name__ == "__main__":
#     solution = Solution()
#     nums = [1, 2, 3, 4, 5, 6]
#     target = 7
#     result = solution.allTwoSumPairs(nums, target)
#     print(result)
  


# from typing import List

# class Solution:
#     def twoSumNoHash(self, nums: List[int], target: int) -> List[int]:
#         nums.sort()
#         lo, hi = 0, len(nums) -1

#         while lo < hi:
#             curr_sum = nums[lo] + nums [hi]
#             if curr_sum == target:
#                 return [nums[lo], nums[hi]]
#             elif curr_sum < target:
#                 lo += 1
#             else:
#                 hi -= 1
#         return []
    
# if __name__ == "__main__":
#     solution = Solution()
#     nums = [2, 7, 11, 15]
#     target = 9
#     result = solution.twoSumNoHash(nums, target)
#     print(result)
   
# from typing import List          
            
# class Solution:
#     def twoSum(self, nums: List[int], target: int):
#         complements = {}
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in complements:
#               return [complements[complement], i]
#             complements[nums[i]] = i
#         return []
        
# if __name__ == "__main__":
#     solution = Solution()
#     nums = [2, 7, 11, 15]
#     target = 9
#     result = solution.twoSum(nums, target)
#     print(result)  # Should print [0,1]           
# from typing import List
# class Solution:
#     def twoSum(self, nums: List[int], target: int):
#         seen = set()
#         for num in nums:
#             complement = target - num
#             if complement in seen:
#                 return [complement, num]
#             seen.add(num)
#         return []
    
# if __name__ == "__main__":
#     solution = Solution()
#     nums = [2, 8, 12, 15]
#     target = 20
#     result = solution.twoSum(nums, target)
#     print(result)

# from typing import List
# class Solution:
#     def twoSum_pair(self, nums: List[int], target: int) -> List[tuple[int,int]]:
#         seen = set ()
#         pairs = []

#         for num in nums:
#             complement = target - num
#             if complement in seen:
#                 pairs.append((complement, num))
#             seen.add(num)
#         return pairs
    
   
# if __name__ == "__main__":
#     solution = Solution()
#     nums = [1, 2, 3, 4, 5, 6]
#     target = 7
#     result = solution.twoSum_pair(nums, target)
#     print(result)

# from typing import List
# class Solution:
#     def twoSumhash(self, nums: List[int], target: int) -> List[int]:
#         nums.sort()
#         lo, hi = 0, len(nums) - 1

#         while lo < hi:
#             curr_sum = nums[lo] + nums[hi]
#             if curr_sum == target:
#                 return [nums[lo], nums[hi]]
#             elif curr_sum < target:
#                 lo += 1
#             else:
#                 hi -= 1

#         return []

# if __name__ == "__main__":
#     solution = Solution()
#     nums = [10, 2, 3, 7, 5]
#     target = 12
#     result = solution.twoSumhash(nums, target)
#     print(result)

from typing import List
class Solution:
    def twosumSorted(self, nums: List[int], target: int):
        complements = {}
        
        if 
