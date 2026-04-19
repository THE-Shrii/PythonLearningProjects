# ✅ 1. Even-Odd Checker
# 🎯 What it does:
# User enters a number → program tells Even or Odd

# num = int(input("Enter a number: "))
#
# if (num % 2 == 0):
#     print("even")
# else:
#     print("odd")






# ✅ 2. Simple Calculator
# 🎯 What it does:
# Performs +, -, *, /

# num1 = int(input("Enter first one: "))
# num2 = int(input("Enter second two: "))
# operation = input("Enter operation(+, -, *, /): ")
#
# if operation == "+":
#     print(num1+num2)
# elif operation == "-":
#     print(num1-num2)
# elif operation == "*":
#     print(num1*num2)
# elif operation == "/":
#     print(num1/num2)
# else:
#     print("Operation not supported")




# ✅ 3. Largest of 3 Numbers
# 🎯 What it does:
# Find biggest number
#
#
# input1 = int(input("Enter 1st no.:"))
# input2 = int(input("Enter 2nd no.:"))
# input3 = int(input("Enter 3rd no.:"))
#
# if input1 > input2 and input1 > input3:
#     print("1st Number is biggest")
# elif input2 > input1 and input2 > input3:
#     print("2nd Number is biggest")
# elif input3 > input1 and input3 > input2:
#     print("3rd Number is biggest")
# else:
#     print("All numbers are equal or two numbers are same")
#


# sor/t
# print("Biggest number is:", max(input1, input2, input3))


#  FOR EQUAL NUMBERS


# input1 = int(input("Enter 1st no.:"))
# input2 = int(input("Enter 2nd no.:"))
# input3 = int(input("Enter 3rd no.:"))
#
# if input1 == input2 == input3:
#     print("All numbers are equal")
#
# elif input1 == input2:
#     print("1st and 2nd numbers are equal")
#
# elif input2 == input3:
#     print("2nd and 3rd numbers are equal")
#
# elif input1 == input3:
#     print("1st and 3rd numbers are equal")
#
# elif input1 > input2 and input1 > input3:
#     print("1st Number is biggest")
#
# elif input2 > input1 and input2 > input3:
#     print("2nd Number is biggest")
#
# else:
#     print("3rd Number is biggest")





# ✅ 4. String Reverser
# 🎯 What it does:
#
# Reverse a word

# word = input("Enter a word: ")
# print(word[::-1])






# ✅ 5. Count Vowels
# 🎯 What it does:
#
# Counts vowels in a word

# s = input("Enter a string:")
# count = 0
#
# for ch in s:
#     if ch.lower() in "aeiou":
#         count += 1
#
# # check AFTER loop
# if count == 0:
#     print("No Vowels found")
# else:
#     print("Vowels:", count)






# ✅ 6. Remove Duplicates (List)
# 🎯 What it does:
#
# Remove duplicate numbers

# l1 = [1,2,2,2,2,4]
# uniquel1 = list(set(l1))
# print(uniquel1)





# ✅ 7. Simple Password Checker
# 🎯 What it does:
#
# Checks if password is strong

# password = input("Enter Your Password:")
#
# if len(password) < 8:
#     print("Too short")
# elif not any(ch.isdigit() for ch in password):
#     print("Add a number")
# elif not any(ch.isupper() for ch in password):
#     print("Add uppercase letter")
# elif not any(ch in "#$&@!*" for ch in password):
#     print("Add special character")
# else:
#     print("Strong password ")





# ✅ 8. Sum of List
# 🎯 What it does:
#
# Find total of numbers

# l1 = [1,2,3]
# l2 = [1,2,3]
#
# print (sum(l1 +l2))



# ✅ 9. Check Palindrome
# 🎯 What it does:
#
# Check same forward/backward
#
# s = input("Enter word: ")
#
# if s == s[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
#
# # Explanation:
# # Compare string with reverse




# 🎯 What it does:
#
# Grade system
#
# marks = int(input("Enter marks: "))
#
# if marks >= 90:
#     print("A")
# elif marks >= 75:
#     print("B")
# elif marks >= 50:
#     print("C")
# else:
#     print("Fail")
#
# # Explanation:
# # Multiple conditions using elif






# food = "Pasta"
# food.replace("a","e")
# print(food)



# PROBLEMS BASED ON LOOPS



# Q1. Find second largest number in list
lst = [10, 20, 5, 8]
first = second = float('-inf')

for num in lst:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print(second)
# Explanation:
# track largest and second largest
# Output: 10


# Q2. Check if list is sorted
lst = [1,2,3,4]
is_sorted = True

for i in range(len(lst)-1):
    if lst[i] > lst[i+1]:
        is_sorted = False
        break

print(is_sorted)
# Output: True


# Q3. Move zeros to end
lst = [0,1,0,3,12]
res = []

for i in lst:
    if i != 0:
        res.append(i)

zeros = len(lst) - len(res)
res.extend([0]*zeros)

print(res)
# Output: [1,3,12,0,0]


# Q4. Find duplicate elements
lst = [1,2,3,2,4,1]
seen = set()
dup = set()

for i in lst:
    if i in seen:
        dup.add(i)
    else:
        seen.add(i)

print(dup)
# Output: {1,2}


# Q5. Rotate list right by 1
lst = [1,2,3,4]
last = lst[-1]

for i in range(len(lst)-1,0,-1):
    lst[i] = lst[i-1]

lst[0] = last
print(lst)
# Output: [4,1,2,3]


# Q6. Count frequency manually
lst = [1,2,2,3]
freq = {}

for i in lst:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)
# Output: {1:1,2:2,3:1}


# Q7. Find missing number (1–n)
lst = [1,2,4,5]
n = 5
total = n*(n+1)//2
print(total - sum(lst))
# Output: 3


# Q8. Reverse words in sentence
s = "hello world"
words = s.split()
res = ""

for w in words[::-1]:
    res += w + " "

print(res.strip())
# Output: world hello


# Q9. Check anagram
s1 = "listen"
s2 = "silent"

print(sorted(s1) == sorted(s2))
# Output: True


# Q10. First non-repeating character
s = "aabbc"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch,0)+1

for ch in s:
    if freq[ch] == 1:
        print(ch)
        break
# Output: c


# Q11. Remove duplicates without set
lst = [1,2,2,3]
res = []

for i in lst:
    if i not in res:
        res.append(i)

print(res)
# Output: [1,2,3]


# Q12. Find intersection of lists
a = [1,2,3]
b = [2,3,4]
res = []

for i in a:
    if i in b:
        res.append(i)

print(res)
# Output: [2,3]


# Q13. Find pair with sum
lst = [2,7,11,15]
target = 9
seen = {}

for i in lst:
    if target - i in seen:
        print(i, target-i)
        break
    seen[i] = True
# Output: 7 2


# Q14. Check palindrome string (loop)
s = "madam"
is_pal = True

for i in range(len(s)//2):
    if s[i] != s[-i-1]:
        is_pal = False
        break

print(is_pal)
# Output: True


# Q15. Flatten nested list
lst = [[1,2],[3,4]]
flat = []

for sub in lst:
    for i in sub:
        flat.append(i)

print(flat)
# Output: [1,2,3,4]


# Q16. Count vowels and consonants
s = "hello"
v = c = 0

for ch in s:
    if ch in "aeiou":
        v += 1
    else:
        c += 1

print(v, c)
# Output: 2 3


# Q17. Longest word in sentence
s = "I love python programming"
longest = ""

for word in s.split():
    if len(word) > len(longest):
        longest = word

print(longest)
# Output: programming


# Q18. Check prime (optimized)
num = 29
is_prime = True

for i in range(2, int(num**0.5)+1):
    if num % i == 0:
        is_prime = False
        break

print(is_prime)
# Output: True


# Q19. Fibonacci nth
n = 7
a,b = 0,1

for _ in range(n-1):
    a,b = b,a+b

print(a)
# Output: 8


# Q20. Spiral sum (simple)
lst = [1,2,3,4]
print(sum(lst))
# Output: 10


# Q21. Matrix transpose
mat = [[1,2],[3,4]]
res = [[0,0],[0,0]]

for i in range(2):
    for j in range(2):
        res[j][i] = mat[i][j]

print(res)
# Output: [[1,3],[2,4]]


# Q22. Find max difference
lst = [2,3,10,6]
max_diff = 0
min_val = lst[0]

for i in lst:
    if i < min_val:
        min_val = i
    elif i - min_val > max_diff:
        max_diff = i - min_val

print(max_diff)
# Output: 8


# Q23. Group even/odd
lst = [1,2,3,4]
even, odd = [], []

for i in lst:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print(even, odd)
# Output: [2,4] [1,3]


# Q24. Remove consecutive duplicates
s = "aaabbc"
res = ""

for ch in s:
    if not res or res[-1] != ch:
        res += ch

print(res)
# Output: abc


# Q25. Count subarrays sum = k
lst = [1,2,3]
k = 3
count = 0

for i in range(len(lst)):
    s = 0
    for j in range(i,len(lst)):
        s += lst[j]
        if s == k:
            count += 1

print(count)
# Output: 2


# Q26. Maximum subarray sum (Kadane's Algorithm)
lst = [-2,1,-3,4,-1,2,1,-5,4]
max_sum = curr = lst[0]

for i in lst[1:]:
    curr = max(i, curr + i)
    max_sum = max(max_sum, curr)

print(max_sum)
# Explanation:
# At each step, decide whether to continue subarray or start new
# Output: 6  (subarray: 4,-1,2,1)


# Q27. Find all pairs with given sum
lst = [1,2,3,4,5]
target = 6

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] + lst[j] == target:
            print(lst[i], lst[j])
# Output:
# 1 5
# 2 4


# Q28. Longest substring without repeating characters
s = "abcabcbb"
seen = set()
left = 0
max_len = 0

for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1
    seen.add(s[right])
    max_len = max(max_len, right-left+1)

print(max_len)
# Output: 3


# Q29. Check if two lists are rotations
a = [1,2,3,4]
b = [3,4,1,2]

is_rotation = False

for i in range(len(a)):
    if a[i:] + a[:i] == b:
        is_rotation = True
        break

print(is_rotation)
# Output: True


# Q30. Find equilibrium index
lst = [1,3,5,2,2]
total = sum(lst)
left_sum = 0

for i in range(len(lst)):
    total -= lst[i]
    if left_sum == total:
        print(i)
        break
    left_sum += lst[i]
# Output: 2


# Q31. Count inversions
lst = [2,4,1,3]
count = 0

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] > lst[j]:
            count += 1

print(count)
# Output: 3


# Q32. Merge two sorted lists
a = [1,3,5]
b = [2,4,6]
i=j=0
res=[]

while i<len(a) and j<len(b):
    if a[i] < b[j]:
        res.append(a[i]); i+=1
    else:
        res.append(b[j]); j+=1

res.extend(a[i:])
res.extend(b[j:])
print(res)
# Output: [1,2,3,4,5,6]


# Q33. Find peak element
lst = [1,3,20,4,1]
for i in range(1,len(lst)-1):
    if lst[i] > lst[i-1] and lst[i] > lst[i+1]:
        print(lst[i])
# Output: 20


# Q34. Longest increasing subsequence (basic)
lst = [10,9,2,5,3,7]
res = [lst[0]]

for i in lst[1:]:
    if i > res[-1]:
        res.append(i)

print(res)
# Output: [10] (basic greedy, not full LIS)


# Q35. Matrix spiral print
mat = [[1,2,3],[4,5,6],[7,8,9]]

while mat:
    print(mat.pop(0))
    mat = list(zip(*mat))[::-1]
# Output:
# [1,2,3]
# (6,9)
# (8,7)
# (4,)
# (5,)


# Q36. Find majority element
lst = [3,3,4,2,3,3]
count = 0
candidate = None

for num in lst:
    if count == 0:
        candidate = num
    count += (1 if num == candidate else -1)

print(candidate)
# Output: 3


# Q37. Sort 0s and 1s
lst = [0,1,0,1,1,0]
zero = 0

for i in range(len(lst)):
    if lst[i] == 0:
        lst[i], lst[zero] = lst[zero], lst[i]
        zero += 1

print(lst)
# Output: [0,0,0,1,1,1]


# Q38. Detect cycle in list (visited logic)
lst = [1,2,3,1]
seen = set()
cycle = False

for i in lst:
    if i in seen:
        cycle = True
        break
    seen.add(i)

print(cycle)
# Output: True


# Q39. Longest common prefix
strs = ["flower","flow","flight"]
prefix = strs[0]

for s in strs[1:]:
    while not s.startswith(prefix):
        prefix = prefix[:-1]

print(prefix)
# Output: fl


# Q40. Subarray with given sum
lst = [1,2,3,7,5]
target = 12
curr = 0
start = 0

for i in range(len(lst)):
    curr += lst[i]
    while curr > target:
        curr -= lst[start]
        start += 1
    if curr == target:
        print(start, i)
# Output: 1 3


# Q41. Count distinct elements
lst = [1,2,2,3,4]
print(len(set(lst)))
# Output: 4


# Q42. Rearrange positives and negatives
lst = [-1,2,-3,4]
pos, neg = [], []

for i in lst:
    (pos if i>0 else neg).append(i)

print(pos + neg)
# Output: [2,4,-1,-3]


# Q43. Find missing + repeating
lst = [1,2,2,4]
seen = set()
rep = miss = None

for i in lst:
    if i in seen:
        rep = i
    seen.add(i)

for i in range(1,len(lst)+1):
    if i not in seen:
        miss = i

print(rep, miss)
# Output: 2 3


# Q44. Next greater element
lst = [4,5,2,25]

for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[j] > lst[i]:
            print(lst[i], "->", lst[j])
            break
    else:
        print(lst[i], "-> -1")
# Output:
# 4->5, 5->25, 2->25, 25->-1


# Q45. Rotate array k times
lst = [1,2,3,4,5]
k = 2

for _ in range(k):
    lst.insert(0, lst.pop())

print(lst)
# Output: [4,5,1,2,3]


# Q46. Count pairs with difference k
lst = [1,5,3,4,2]
k = 2
count = 0

for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if abs(lst[i]-lst[j]) == k:
            count += 1

print(count)
# Output: 3


# Q47. First repeating element
lst = [10,5,3,4,3,5,6]
seen = set()

for i in lst:
    if i in seen:
        print(i)
        break
    seen.add(i)
# Output: 3


# Q48. Check balanced parentheses
s = "()()"
count = 0

for ch in s:
    if ch == "(":
        count += 1
    else:
        count -= 1
    if count < 0:
        print(False)
        break
else:
    print(count == 0)
# Output: True


# Q49. Count triplets with sum
lst = [1,2,3,4,5]
target = 9
count = 0

for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        for k in range(j+1,len(lst)):
            if lst[i]+lst[j]+lst[k]==target:
                count += 1

print(count)
# Output: 2


# Q50. Final: longest consecutive sequence
lst = [100,4,200,1,3,2]
s = set(lst)
max_len = 0

for i in s:
    if i-1 not in s:
        length = 1
        while i+length in s:
            length += 1
        max_len = max(max_len, length)

print(max_len)
# Output: 4  (sequence: 1,2,3,4)