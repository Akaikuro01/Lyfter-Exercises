def validate_list(list_):
    try:
        if not list_:
            raise Exception("The list is empty")        
        
        for item in list_:
            if not isinstance(item, (int, float)):
                raise Exception("The list contains non numeric values")
        return True
    except Exception as ex:
        print(ex)
        return False




def bubble_sort(list_):
    if not validate_list(list_):
        return
    else:
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

#Scenario 1
my_list = [18, -11, 68, 6, 32, 53, "-2"]
my_sorted_list = bubble_sort(my_list)

print(my_sorted_list)
print("-----------------------------")

#Scenario 2
my_list = []
my_sorted_list = bubble_sort(my_list)

print(my_sorted_list)
print("-----------------------------")

#Scenario 3
my_list = None
my_sorted_list = bubble_sort(my_list)

print(my_sorted_list)
print("-----------------------------")

#Scenario 4
my_list = [18, -11, 68, 6, 32, 53, -2]
my_sorted_list = bubble_sort(my_list)

print(my_sorted_list)
print("-----------------------------")