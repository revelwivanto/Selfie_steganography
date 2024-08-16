from queue import Queue

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
    
    # Initialize queues
    queue_0 = Queue()
    queue_7 = Queue()
    queue_others = Queue()
    
    # Count the occurrences of each group and add to respective queues
    for group in groups:
        if group == '000':
            count_0 += 1
            queue_0.put(group)
        elif group == '111':
            count_7 += 1
            queue_7.put(group)
        else:
            count_others += 1
            queue_others.put(group)
    
    # Calculate the ratio
    total_groups = len(groups)
    ratio_0 = count_0
    ratio_others = count_others
    ratio_7 = count_7
    
    return f"Ratio = {ratio_0}:{ratio_others}:{ratio_7}", queue_0, queue_7, queue_others

# Example usage
bit_string = "101111010101000011"
ratio, queue_0, queue_7, queue_others = calculate_ratio(bit_string)
print(ratio)

# Print the contents of each queue
print("Queue 0 (000 bits):")
while not queue_0.empty():
    print(queue_0.get())

print("Queue 7 (111 bits):")
while not queue_7.empty():
    print(queue_7.get())

print("Queue Others (mixed bits):")
while not queue_others.empty():
    print(queue_others.get())
