for row in range(1, 5):
    for colum in range(1, 5):
        print("# ", end="")
    print()

for row in range(6):
    for colum in range(row):
        print("#", end="")
    print()
print()
for row in range(5):
    for colum in range(5-row):
        print("#", end="")
    print()
print()
for row in range(5):
    for colum in range(row):
        print("#", end="")
    print()