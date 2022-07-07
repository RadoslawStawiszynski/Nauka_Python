# 1 sposób zapisu odwołania do liczb

nums = [4, 5, 6]
nums2 = "+"
nums3 = [2.3, 2.44, 3.987]

msg = "Numbers: {0} {1} {2}".format(nums[0], nums2[0], nums3[2])

print(msg)

# 2 sposób zapisu

nums = [4, 5, 6]

msg = f"Numbers: {nums[0]} {nums[1]} {nums[2]}"

print(msg)

# 3 sposób zapisu

a = "{x} + {y} = ".format(x=5, y=12.3,)
print(a)

# 4 sposób zapisu
x = 5
y = 12.3
z = x+y
a = f"{x} + {y} = {z}"
print(a)