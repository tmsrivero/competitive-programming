def count_groups(n, numbers):
    groups = {}  # Dictionary to store groups based on bit values

    # Iterate over each number
    for num in numbers:
        curr_group = 0  # Current group for the number

        # Iterate over each bit position
        for i in range(31):
            bit_value = (num >> i) & 1  # Extract the bit value at position i

            # If the bit value exists in the current group, update the group number
            if bit_value in groups.get(i, {}):
                curr_group = groups[i][bit_value]
                break
        else:
            curr_group += 1  # If no matching bit value found, create a new group

        # Update the group for each bit position
        for i in range(31):
            bit_value = (num >> i) & 1
            if i not in groups:
                groups[i] = {}
            groups[i][bit_value] = curr_group

    # Return the count of distinct groups
    return len(set(groups[i][bit_value] for i in range(31) for bit_value in groups[i]))


# Input handling
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    numbers = list(map(int, input().strip().split()))
    print(count_groups(n, numbers))
