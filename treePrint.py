
print("--- My Tree Print Program ---")
size = int(input("Enter the size of the tree: "))

for row_num in range(1, size + 1):
    branch_char = (row_num * 2 - 1)
    space_char = (size - row_num)

    print(" " * space_char + "^" * branch_char)

print(" " * (size - 1) + "##")
print(" " * (size - 1) + "##")


print("End of Program")