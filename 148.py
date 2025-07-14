def list_array_functions():
    arr = [10, 20, 30, 40, 50]

    print("Original array:", arr)
    arr.append(60)                  # Add element
    print("After append:", arr)

    arr.insert(2, 25)               # Insert at index 2
    print("After insert:", arr)

    arr.remove(30)                  # Remove element
    print("After remove 30:", arr)


list_array_functions()