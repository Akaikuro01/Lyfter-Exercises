import Logic
import Data_handling
from datetime import datetime

class AppManager():
    def update_balance(self, current_balance, amount, subject):
        try:
            new_balance = Logic.Balance(current_balance)
            if subject:
                new_balance.add_balance(amount)
            else:
                new_balance.subtract_balance(amount)
        except Exception as ex:
            print(f"Error: {ex}")
        return new_balance.balance

    def get_new_amount(self, list_entries):
        new_amount = 0
        try:
            last_element_all_entries = (len(list_entries) - 1)
            last_element_amount = (len(list_entries[last_element_all_entries]) - 1)
            new_amount = float(list_entries[last_element_all_entries][last_element_amount])
        except Exception as ex:
            print(f"Error: {ex}")    
        return new_amount

    def load_expenses_revenue(self):
        all_entries = []
        try:
            load = Data_handling.AutoLoad()
            all_entries = load.load_revenue_expenses("revenue_expenses.csv")
        except Exception as ex:
            print(f"Error: {ex}")
        return all_entries

    def load_categories(self):
        all_categories = []
        try:
            load = Data_handling.AutoLoad()
            all_categories = load.load_categories("categories.csv")
        except Exception as ex:
            print(f"Error: {ex}")
        return all_categories

    def load_balance(self):
        try:
            load = Data_handling.AutoLoad()
            balance = load.load_balance("balance.csv")
        except Exception as ex:
            print(f"Error: {ex}")
        return balance

    def save_expenses_revenue(self, headers, all_entries):
        try:
            save = Data_handling.AutoSave()
            save.save_revenue_expenses("revenue_expenses.csv", headers, all_entries)
            print("Changes saved!")
        except Exception as ex:
            print(f"Error: {ex}")

    def save_balance(self, balance):
        try:
            save = Data_handling.AutoSave()
            save.save_balance("balance.csv", balance)
            print("Balance saved!")
        except Exception as ex:
            print(f"Error: {ex}")

    def save_categories(self, all_categories):
        try:
            save = Data_handling.AutoSave()
            save.save_categories("categories.csv", all_categories)
            print("Categories saved!")
        except Exception as ex:
            print(f"Error: {ex}")
    
    def filter_data_dates(self, start_date, end_date, all_entries):
        filtered_entries = []
        try:
            for element in all_entries:  
                date = datetime.strptime(element[1], "%d-%m-%Y").date()            
                if (start_date <= date <= end_date):
                    filtered_entries.append(element)
        except Exception as ex:
            print(f"Error: {ex}")
        return filtered_entries
    
    def check_date_format(self, date):
        try:
            datetime.strptime(date, "%d-%m-%Y")
            return True
        except ValueError as ex:
            return False
    
    def add_revenue(self, date, title, category, amount):
        try:
            new_revenue = Logic.FinancesManager(date, title, category, amount)
            revenue_entries = new_revenue.add_revenue()
        except Exception as ex:
            print(f"Error: {ex}")
        return revenue_entries


    def add_expense(self, date, title, category, amount):
        try:
            new_expense = Logic.FinancesManager(date, title, category, amount)
            expense_entries = new_expense.add_expense()
        except Exception as ex:
            print(f"Error: {ex}")
        return expense_entries

    def check_amount_is_number(self, amount):
        try:
            float(amount)
            return True
        except ValueError as ex:
            return False
        
    def color_rows(self, all_entries, all_categories):
        rows_colored = []
        try:
            for index, element in enumerate(all_entries):
                for category in all_categories:
                    if element[3] == category[0]:
                        rows_colored.append((index, "white", category[1]))
                        break
        except IndexError as e:
            print(f"Index error while coloring rows: {e}")
        except TypeError as e:
            print(f"Type error: expected lists of lists for entries and categories: {e}")
        except AttributeError as e:
            print(f"Attribute error: data not structured correctly: {e}")
        except Exception as ex:
            print(f"Unexpected error: {ex}")
        return rows_colored
    
    def calculate_total_revenue(self, all_entries):
        try:
            total_revenue = 0
            for entry in all_entries:
                if entry[0] == "Income":
                    total_revenue += float(entry[4])
        except Exception as ex:
            print(ex)
        return total_revenue
    
    def calculate_total_expense(self, all_entries):
        try:
            total_expense = 0
            for entry in all_entries:
                if entry[0] == "Expense":
                    total_expense += float(entry[4])
        except Exception as ex:
            print(ex)
        return total_expense
        
    def manual_export_expenses_revenue(self, headers, all_entries, total_revenue, total_expense, balance):
        try:
            export = Data_handling.ManualLoad()
            export.manual_export_csv("revenue_expenses_report.csv", headers, all_entries, total_revenue, total_expense, balance)
            print("Data exported!")
        except Exception as ex:
            print(f"Error: {ex}")
