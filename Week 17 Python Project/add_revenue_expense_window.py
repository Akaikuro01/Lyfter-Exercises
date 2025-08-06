import FreeSimpleGUI as sg
import app_logic
from datetime import datetime

# For subject, it is a boolean and I use it to know whether we are adding an expense or a revene. True = Revenue, False = Expense
def open_add_revenue_expense_window(all_entries, all_categories, subject):
    try:
        #Getting only the categories to rule out the colors.
        categories_only_list = []
        for category in all_categories:
            categories_only_list.append(category[0])


        app = app_logic.AppManager()
        add_revenue_window_layout = [
            [sg.Column([
                [sg.Text("Title:")],
                [sg.Text("Category:")],
                [sg.Text("Amount:")],
                [sg.Text("Date:")],
            ]),
            sg.Column([
                [sg.Input(key="title", size=(20, None))],
                [sg.Combo(values=categories_only_list, key="category", readonly=True, size=(20, 1))],
                [sg.Input(key="amount", size=(20, None))],
                [sg.Input("Click choose date...", key="date", size=(20, None), disabled=True)],            
            ])],        
            [sg.Button("Add"), sg.CalendarButton("Choose Date", target="date", format="%d-%m-%Y")]
        ]

        
        window_name = ""
        if subject:
            window_name = "Add Revenue"
        else:
            window_name = "Add Expense"
        
        revenue_expense_window = sg.Window(window_name, add_revenue_window_layout)

        while True:
            event, values = revenue_expense_window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "Add":
                # If there is any of the values requested empty, then I request the user to fill them all up. Otherwise, nothing will happen.
                if (values["title"] == "" or values["category"] == "" or values["amount"] == "" or values["date"] == ""):
                    sg.popup("All fields are mandatory, please fill up all the requested information.")
                elif not app.check_amount_is_number(values["amount"]):
                    sg.popup("Invalid amount entered.")
                elif datetime.strptime(values["date"], "%d-%m-%Y").date() > datetime.now().date():
                    sg.popup("Cannot enter a future date.")
                    # If the amount entered is negative, I need to show them an error.
                elif float(values["amount"]) < 0:
                    sg.popup("Cannot enter negative numbers.")
                # If they enter only blank spaces, I also cannot allow them to enter the values.
                elif (values["title"].isspace() or values["category"].isspace() or values["amount"].isspace() or values["date"].isspace()):
                    sg.popup("Please enter a valid value. Input cannot be only blank spaces.")
                else:
                    #If subject is True then it is a revenue so I call revenue logic, otherwise, do the same for Expense.
                    if subject:
                        title = values["title"]
                        category = values["category"]
                        amount = float(values["amount"]) 
                        date = datetime.strptime(values["date"], "%d-%m-%Y").date()
                        revenue_entry = app.add_revenue(date, title, category, amount)
                        all_entries.append(revenue_entry)
                        sg.popup("Revenue added!")
                    else:
                        title = values["title"]
                        category = values["category"]
                        amount = float(values["amount"])
                        date = datetime.strptime(values["date"], "%d-%m-%Y").date()
                        expense_entry = app.add_expense(date, title, category, amount)
                        all_entries.append(expense_entry)
                        sg.popup("Expense added!")
                    break
        
        revenue_expense_window.close()
    except Exception as ex:
        print(f"Error: {ex}")
    return all_entries
