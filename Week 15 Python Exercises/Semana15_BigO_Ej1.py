def bubble_sort(list_):
    for outer_index in range(0, len(list_)): #O(n)
        has_made_changes = False #O(1)
        for index in range(0, len(list_) - 1 - outer_index): #O(n^2)
            current_element = list_[index] #O(1)
            next_element = list_[index + 1] #O(1)
            if(current_element > next_element): #O(1)
                list_[index] = next_element #O(1)
                list_[index + 1] = current_element #O(1)
                has_made_changes = True #O(1)
        if has_made_changes == False: #O(1)
            break #O(1)
    
    return list_ #O(1)

my_list = [18, -11, 68, 6, 32, 53, -2] #O(1)
my_sorted_list = bubble_sort(my_list) #O(n^2)

print(my_sorted_list) #O(1)