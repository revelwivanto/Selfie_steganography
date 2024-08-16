def calculate_ratio(bit_string):
    # Ensure the bit string length is a multiple of 3
    if len(bit_string) % 3 != 0:
        bit_string = bit_string.ljust(len(bit_string) + (3 - len(bit_string) % 3), '0')
    
    # Group the bit string into 3-bit segments
    groups = [bit_string[i:i+3] for i in range(0, len(bit_string), 3)]
    
    # Initialize counters
    count_0 = 0
    count_7 = 0
    count_others = 0
    
    # Count the occurrences of each group
    for group in groups:
        if group == '000':
            count_0 += 1
        elif group == '111':
            count_7 += 1
        else:
            count_others += 1
    
    # Calculate the ratio
    total_groups = len(groups)
    ratio_0 = count_0
    ratio_7 = count_7
    ratio_others = count_others
    
    return f"Ratio = {ratio_0}:{ratio_7}:{ratio_others}"

# Example usage
bit_string = "101111010101000011"
print(calculate_ratio(bit_string))
