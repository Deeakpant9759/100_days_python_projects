arr = []  # empty 2D list

# Append empty rows up to 4 rows
for _ in range(4):
    arr.append([])

# Now you have 4 empty rows, you can append elements to any row
arr[0].append(10)
arr[1].append(20)

print(arr)
# Output: [[10], [20], [], []]
