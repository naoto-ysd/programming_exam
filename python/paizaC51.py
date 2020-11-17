nums=list(map(int,input().split()))
result = 0
for i in range(4):
  for j in range(4):
    if i !=j:
      result = max(result,(sum(nums)+9*(nums[i]+nums[j])))

print(result)