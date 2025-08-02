def bubble_sort(list_):
    total_iterations = 0
    changes_made = 0
    for outer_index in range(0, len(list_)):        
        has_made_changes = False
        for index in range(0, len(list_) - 1 - outer_index):
            total_iterations += 1
            current_element = list_[index]
            next_element = list_[index + 1]
            if(current_element > next_element):
                list_[index] = next_element
                list_[index + 1] = current_element
                has_made_changes = True
                changes_made += 1
        if has_made_changes == False:
            break
    
    print(f"Lista ordenada: {list_}")
    print(f"Iteraciones: {total_iterations}")
    print(f"Intercambios: {changes_made}")
    return list_



my_list = [18, -11, 68, 6, 32, 53, -2]
my_sorted_list = bubble_sort(my_list)