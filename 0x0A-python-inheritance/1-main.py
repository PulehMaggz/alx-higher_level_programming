#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)

# Print the original list
print(my_list)

# Print the sorted list using the print_sorted method
my_list.print_sorted()

# Print the list again to show it's unchanged
print(my_list)

