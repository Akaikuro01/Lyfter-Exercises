import FreeSimpleGUI as sg
import add_category_window
import add_revenue_expense_window
import app_logic
from datetime import datetime


def main():
    try:
        # Initialize object that handles all the logic required for the main window
        app = app_logic.AppManager()
        # Define the table headings
        headers = ["Subject", "Date", "Title", "Category", "Amount"]
        balance = app.load_balance()
        all_entries = app.load_expenses_revenue()
        all_categories = app.load_categories()
        # Now I color the rows by loading a list with the row and color each row will have in the table
        rows_colored = app.color_rows(all_entries, all_categories)
        # Define the layout
        main_window_layout = [
            [sg.Text("Start Date:"), 
            sg.Input(key="start_date", size=(20, None)),
            sg.Text("End Date:"),
            sg.Input(key="end_date", size=(20, None)),
            sg.Column([[sg.Button("Filter")], [sg.Button("Reset")]])], 
            [sg.Table(
                values=all_entries,
                headings=headers,
                auto_size_columns=True,
                display_row_numbers=False,
                justification="center",
                num_rows=5,
                key="finances_table",
                enable_events=True
            ), 
            sg.Column([
                [sg.Button("Add Category")],
                [sg.Button("Add Revenue")],
                [sg.Button("Add Expense")]
            ])
            ],
            [sg.Text(f"Balance: {balance}", key="balance_text")],
            [sg.Button("Exit"), sg.Button("Export to CSV")]
        ]

        window = sg.Window("Finances", main_window_layout, finalize=True)
        # Here I color the rows in the table.
        window["finances_table"].update(row_colors=rows_colored)

        
        while True:
            event, values = window.read()


            if event == sg.WIN_CLOSED:
                break
            elif event == "Filter":
                if(values["start_date"] != "" and values["end_date"] != ""):
                    if(app.check_date_format(values["start_date"]) and app.check_date_format(values["end_date"])):
                        start_date = datetime.strptime(values["start_date"], "%d-%m-%Y").date()
                        end_date = datetime.strptime(values["end_date"], "%d-%m-%Y").date()
                        filtered_entries = app.filter_data_dates(start_date, end_date, all_entries)
                        rows_colored = app.color_rows(filtered_entries, all_categories)
                        window["finances_table"].update(values=filtered_entries)
                        window["finances_table"].update(row_colors=rows_colored)
                    else:
                        sg.popup("Type a valid date: dd-mm-yyyy")
                else:
                    sg.popup("Type a valid date: dd-mm-yyyy")
            elif event == "Reset":
                rows_colored = app.color_rows(all_entries, all_categories)
                window["finances_table"].update(values=all_entries)
                window["finances_table"].update(row_colors=rows_colored)
            elif event == "Add Category":
                amount_entries_in_list = len(all_categories)
                all_categories = add_category_window.open_add_category_window(all_categories)
                if(amount_entries_in_list < len(all_categories)):
                    app.save_categories(all_categories)
            elif event == "Add Revenue":                
                amount_entries_in_list = len(all_entries)
                # I pass True because True = Revenue
                all_entries = add_revenue_expense_window.open_add_revenue_expense_window(all_entries, all_categories, True)
                # I check if the list hasn't grown so it doesn't go and save data that has not changed.
                if(amount_entries_in_list < len(all_entries)):
                    new_amount = app.get_new_amount(all_entries)
                    balance = app.update_balance(balance, new_amount, True)
                    app.save_expenses_revenue(headers, all_entries)
                    app.save_balance(balance)
                    rows_colored = app.color_rows(all_entries, all_categories)
                    window["finances_table"].update(values=all_entries)
                    window["balance_text"].update(f"Balance: {balance}")
                    window["finances_table"].update(row_colors=rows_colored)
            elif event == "Add Expense":
                amount_entries_in_list = len(all_entries)
                # I pass False because False = Expense
                all_entries = add_revenue_expense_window.open_add_revenue_expense_window(all_entries, all_categories, False)
                # I check if the list hasn't grown so it doesn't go and save data that has not changed.
                if(amount_entries_in_list < len(all_entries)):
                    new_amount = app.get_new_amount(all_entries)
                    balance = app.update_balance(balance, new_amount, False)
                    app.save_expenses_revenue(headers, all_entries)
                    app.save_balance(balance)
                    rows_colored = app.color_rows(all_entries, all_categories)
                    window["finances_table"].update(values=all_entries)
                    window["balance_text"].update(f"Balance: {balance}")
                    window["finances_table"].update(row_colors=rows_colored)
            elif event == "Export to CSV":
                total_revenue = app.calculate_total_revenue(all_entries)
                total_expense = app.calculate_total_expense(all_entries)
                app.manual_export_expenses_revenue(headers, all_entries, total_revenue, total_expense, balance)
                sg.popup("Data exported successfully!")
            elif event == "Exit":
                break

        window.close()
    except Exception as ex:
        print(f"Error: {ex}")

main()