class Balance():
    def __init__(self, balance):
        self.balance = balance 
    
    def add_balance(self, amount):
        try:
            self.balance += amount
        except TypeError as ex:
            print(f"Error adding balance: {ex}")
        except Exception as ex:
            print(f"Unexpected error in add_balance: {ex}")
        return self.balance

    def subtract_balance(self, amount):
        try:
            self.balance -= amount
        except TypeError as ex:
            print(f"Error subtracting balance: {ex}")
        except Exception as ex:
            print(f"Unexpected error in subtract_balance: {ex}")
        return self.balance


class Revenue():
    def __init__(self, date, title, category, amount):
        self.date = date
        self.title = title
        self.category = category
        self.amount = amount
    

class Expense():
    def __init__(self, date, title, category, amount):
        self.date = date
        self.title = title
        self.category = category
        self.amount = amount


class Category():
    def __init__(self, category, color):
        self.category = category
        self.color = color

    def add_category_to_list(self, category_list):        
        try:
            new_category = []
            new_category.append(self.category)
            new_category.append(self.color)
            category_list.append(new_category)
        except AttributeError as ex:
            print(f"Error adding category: category_list is not a list. {ex}")
        except Exception as ex:
            print(f"Unexpected error in add_category_to_list: {ex}")
        return category_list


class FinancesManager(Revenue, Expense, Category, Balance):
    def add_revenue(self, new_entries=[]):
        try:
            # I pass True because it is revenue.
            return self.add_to_list(True, new_entries)
        except Exception as ex:
            print(f"Error adding revenue: {ex}")
            return new_entries

    def add_expense(self, new_entries=[]):        
        try:
            # I pass False because it is expense.
            return self.add_to_list(False, new_entries)
        except Exception as ex:
            print(f"Error adding expense: {ex}")
            return new_entries

    
    def add_to_list(self, subject, new_entries):
        #If subject is true, then it is a revenue, if it is False, then it is an expense
        try:
            if subject:
                new_entries.append("Income")
                new_entries.append(self.date)
                new_entries.append(self.title)
                new_entries.append(self.category)
                new_entries.append(self.amount)
            else:
                new_entries.append("Expense")
                new_entries.append(self.date)
                new_entries.append(self.title)
                new_entries.append(self.category)
                new_entries.append(self.amount)
        except AttributeError as ex:
            print(f"Error adding to list: new_entries is not a list. {ex}")
        except Exception as ex:
            print(f"Unexpected error in add_to_list: {ex}")
        return new_entries