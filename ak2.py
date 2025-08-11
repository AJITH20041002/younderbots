#merging two sorted lists to a single sorted list
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
print("Sorted List 1:", list1)
print("Sorted List 2:", list2)
merged_list =sorted(list1 + list2)
print("Merged Sorted List:", merged_list)
