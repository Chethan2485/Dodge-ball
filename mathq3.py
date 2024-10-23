tuples_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
new_value = 100
#modified_result = replace_last_value(tuples_list, new_value)
modified_list = []
for tpl in tuples_list:
# Replace the last value of the tuple with new_value
    modified_tuple = tpl[:-1] + (new_value,)
# Append the modified tuple to the new list
    modified_list.append(modified_tuple)
print("Original list of tuples:", tuples_list)
print("Modified list of tuples:", modified_list)