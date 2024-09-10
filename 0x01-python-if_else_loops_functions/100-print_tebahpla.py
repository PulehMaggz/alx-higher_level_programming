#!/usr/bin/python3

def print_tebahpla():
    # Print characters in reverse order, alternating between lowercase and uppercase
    print(''.join(
        chr(122 - i) if i % 2 == 0 else chr(90 - (i // 2)) 
        for i in range(26)
    ), end='')

# Call the function
print_tebahpla()
