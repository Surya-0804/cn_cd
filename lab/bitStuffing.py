def bitstuffing(pattern):
    one_count = 0  # Counter for consecutive ones
    stuffed_pattern = []
    
    for bit in pattern:
        stuffed_pattern.append(bit)
        if bit == '1':
            one_count += 1
            if one_count == 5:
                stuffed_pattern.append('0')  # Insert 0 after five 1s
                one_count = 0
        else:
            one_count = 0
    
    return ''.join(stuffed_pattern)

def destuffing(stuffed_pattern):
    one_count = 0  # Counter for consecutive ones
    destuffed_pattern = []
    
    i = 0
    while i < len(stuffed_pattern):
        bit = stuffed_pattern[i]
        destuffed_pattern.append(bit)
        
        if bit == '1':
            one_count += 1
            if one_count == 5:
                i += 1  # Skip the next 0
                one_count = 0
        else:
            one_count = 0
        
        i += 1
    
    return ''.join(destuffed_pattern)

# Example of usage
bit_pattern = input('Enter bit pattern: ')
print('Original bit pattern:', bit_pattern)
stuffed = bitstuffing(bit_pattern)
print('Bit pattern after stuffing:', stuffed)
destuffed = destuffing(stuffed)
print('Bit pattern after destuffing:', destuffed)