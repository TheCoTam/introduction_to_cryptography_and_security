my_list = []

if my_list:
    most_common_element = max(my_list, key=my_list.count)
else:
    most_common_element = 'deo co gi ca'
print(most_common_element)