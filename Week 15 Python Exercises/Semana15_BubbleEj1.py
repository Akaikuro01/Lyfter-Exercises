def bubble_sort(list_):
    for outer_index in range(0, len(list_)):
        has_made_changes = False
        for index in range(0, len(list_) - 1 - outer_index):
            current_element = list_[index]
            next_element = list_[index + 1]
            if(current_element > next_element):
                list_[index] = next_element
                list_[index + 1] = current_element
                has_made_changes = True
        if has_made_changes == False:
            break
    
    return list_

my_list = [18, -11, 68, 6, 32, 53, -2]
my_sorted_list = bubble_sort(my_list)

print(my_sorted_list)