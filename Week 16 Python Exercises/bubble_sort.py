def validate_list(list_):
    try:
        if not list_:
            raise Exception("The list is empty")        

        if not isinstance(list_, list):
            raise Exception("Parameter passed is not a list")

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
    

input_L = "L"
bubble_sort(input_L)
