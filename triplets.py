#!/usr/bin/env python

# Opens a text file with names of all the students
with open('class.txt') as class_names:
  names = class_names.readlines()

# Strips the line breaks
class_list = [name.strip() for name in names]
# print(class_list)

# Function below converts a flat list into a group of n-length tuples.
def group(a_list, n):
  """
  Groups a list into consecutive n- tuples. Incomplete tuples are discarded.

  Eg -> group(range(10), 3)
  [(0,1,2), (3,4,5), (6,7,8)] 

  Note however that incomplete tuples are disregared.
  """
  if  len(a_list) % n != 0:
    for i in range(len(a_list) % n + 1):
      a_list.append("Holder")
    return list(zip(*[a_list[i::n] for i in range(n)]))
     
      

  return zip(*[a_list[i::n] for i in range(n)])



# print(group(class_list, 3), len(class_list))

d = group(class_list, 3)
print(d)


# Creates and writes the name of pairs
with open("triplets.txt", "w") as output_file:
  # Iterates through the list and then extracts the names from the tuples. Puts the pair in new lines.
  output_file.write('\n'.join('{}, {}, {}'.format(
      x[0], x[1], x[2]) for x in group(class_list, 3)))

# print(output_file)

"""
For prep i have estimated that i need 6 randomized pairings before group projects.

So roughly 8 including the first week of prep.

For core i estimate 20 pairings. 4 for the Js, 8 python, 8 django.
This is minus the group project for the python module and capstone for the django module.
"""
