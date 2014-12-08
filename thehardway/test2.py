n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lst):
    final_list = []
    for each_item in range(len(lst)):
        final_list += lst[each_item]
    print final_list

print flatten(n)