import csv

class AutoSave():
    def save_revenue_expenses(self, path, headers, all_entries_list):
        try:
            with open(path, 'w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                writer.writerows(all_entries_list)
        except FileNotFoundError:
            print(f"Error: File {path} not found.")
        except PermissionError:
            print(f"Error: No permission to read {path}.")
        except UnicodeDecodeError:
            print(f"Error: Encoding issue while reading {path}.")
        except csv.Error as e:
            print(f"CSV parsing error: {e}")
        except Exception as ex:
            print(f"Unexpected error: {ex}")
    
    def save_balance(self, path, balance):
        try:
            with open(path, 'w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Balance"]) #Only one header as I am just saving balance on this sheet.
                writer.writerow([balance]) #Same here, I only have one value which is the total balance.
        except FileNotFoundError:
            print(f"Error: File {path} not found.")
        except PermissionError:
            print(f"Error: No permission to read {path}.")
        except UnicodeDecodeError:
            print(f"Error: Encoding issue while reading {path}.")
        except csv.Error as e:
            print(f"CSV parsing error: {e}")
        except Exception as ex:
            print(f"Unexpected error: {ex}")
    
    def save_categories(self, path, categories_list):
        try:
            with open(path, 'w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Category", "Color"])
                writer.writerows(categories_list)
        except FileNotFoundError:
            print(f"Error: File {path} not found.")
        except PermissionError:
            print(f"Error: No permission to read {path}.")
        except UnicodeDecodeError:
            print(f"Error: Encoding issue while reading {path}.")
        except csv.Error as e:
            print(f"CSV parsing error: {e}")
        except Exception as ex:
            print(f"Unexpected error: {ex}")


class AutoLoad():
    def load_revenue_expenses(self, path):
        list_all_elements_with_headers = []
        try:
            with open(path, mode="r", encoding='utf-8', newline="") as file:
                reader = csv.reader(file)
                next(reader, None) # Skip the headers
                list_all_elements_with_headers = list(reader)
        except FileNotFoundError:
            print(f"Error: File {path} not found.")
        except PermissionError:
            print(f"Error: No permission to read {path}.")
        except UnicodeDecodeError:
            print(f"Error: Encoding issue while reading {path}.")
        except csv.Error as e:
            print(f"CSV parsing error: {e}")
        except Exception as ex:
            print(f"Unexpected error: {ex}")        
        return list_all_elements_with_headers
    
    def load_balance(self, path):
        try:
            with open(path, mode="r", encoding='utf-8', newline="") as file:
                balance = list(csv.reader(file))[1][0] #here I am only taking the first value as I know this only saves one header with one row
        except FileNotFoundError:
            print(f"Error: File {path} not found.")
        except PermissionError:
            print(f"Error: No permission to read {path}.")
        except UnicodeDecodeError:
            print(f"Error: Encoding issue while reading {path}.")
        except csv.Error as e:
            print(f"CSV parsing error: {e}")
        except Exception as ex:
            print(f"Unexpected error: {ex}")        
        return float(balance)
    
    def load_categories(self, path):
        categories_list_of_lists = []
        try:
            with open(path, mode="r", encoding='utf-8', newline="") as file:
                    reader = csv.reader(file)
                    next(reader, None) # Skip the headers
                    categories_list_of_lists = list(reader)                    
        except FileNotFoundError:
            print(f"Error: File {path} not found.")
        except PermissionError:
            print(f"Error: No permission to read {path}.")
        except UnicodeDecodeError:
            print(f"Error: Encoding issue while reading {path}.")
        except csv.Error as e:
            print(f"CSV parsing error: {e}")
        except Exception as ex:
            print(f"Unexpected error: {ex}")
        return categories_list_of_lists
    
class ManualLoad():
    def manual_export_csv(self, path, headers, all_entries_list, total_revenue, total_expense, balance):
        try:
            with open(path, 'w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                writer.writerows(all_entries_list)
                writer.writerow([])
                writer.writerow(["Grand Totals:"])
                writer.writerow([f"Revenue: ₡{total_revenue}"])
                writer.writerow([f"Expenses: ₡{total_expense}"])
                writer.writerow([f"Net Balance: ₡{balance}"])
        except FileNotFoundError:
            print(f"Error: File {path} not found.")
        except PermissionError:
            print(f"Error: No permission to read {path}.")
        except UnicodeDecodeError:
            print(f"Error: Encoding issue while reading {path}.")
        except csv.Error as e:
            print(f"CSV parsing error: {e}")
        except Exception as ex:
            print(f"Unexpected error: {ex}")