# Create a list
my_list = []

# Read the number of elements
n = int(input("Enter the number of elements: "))

# Insert elements into the list
for i in range(n):
    element = int(input("Enter element: "))
    my_list.append(element)

# Display the list
print("\nElements of the list are:")

# Traverse the list
for i in range(len(my_list)):
    print(my_list[i])
