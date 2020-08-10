#!/usr/bin/env python3

# create a list called list1
list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]
# display list1
print(list1)

# display second item in the list
print(list1[1])

# Create a new list 
list2 = ["juniper"]

# extend list1 by list2
list1.extend(list2)

# display list1 again
print(list1)

# create list 3
list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

# use append on list1 with list3
list1.append(list3)

# display new list1
print(list1)

# display the list of IP addresses
print(list1[4])

# display the first IP address
print(list1[4][0])
