import FreeSimpleGUI as sg
import Logic

def add_category(category_list, category, color):
    try:
        new_category = Logic.Category(category, color)
        category_list = new_category.add_category_to_list(category_list)
    except Exception as ex:
        print(f"Error: {ex}")
    return category_list

def open_add_category_window(all_categories):
    try:
        add_category_window_layout = [
            [sg.Text("New Category name:"), sg.Input(key="category", size=(20, None))],
            [sg.ColorChooserButton("Choose a color for your category", key="color"), sg.Input(key="color_input", size=(10, None))],
            [sg.Button("Add")]
        ]
        category_window = sg.Window("Add a category", add_category_window_layout)

        while True:
            event, values = category_window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "Add":
                if (values["category"] == "" or values["color_input"] == ""):
                    sg.popup("Please type a category and a color to add.")
                elif (values["category"].isspace() or values["color_input"].isspace()):
                    sg.popup("Please enter a valid value. Input cannot be only blank spaces.")
                else:
                    category = values["category"]
                    color = values["color_input"]
                    all_categories = add_category(all_categories, category, color)
                    sg.popup("Category added!")
                    break
            elif event == "color":
                chosen_color = values["color"]
                category_window["color_input"].update(chosen_color)
            elif event == "Back":
                category_window.close()
        
        category_window.close()
    except Exception as ex:
        print(f"Error: {ex}")
    return all_categories