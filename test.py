import FreeSimpleGUI as sg

data = [
    ["2025-08-01", "Salary", "1500"],
    ["2025-08-02", "Groceries", "-80"],
    ["2025-08-03", "Car Repair", "-200"]
]
headings = ["Date", "Category", "Amount"]

layout = [
    [sg.Table(values=data,
              headings=headings,
              key="-TABLE-",
              auto_size_columns=True,
              justification="center",
              enable_events=True,
              num_rows=5)],
    [sg.Button("Color Rows"), sg.Button("Exit")]
]

window = sg.Window("Row Color Example", layout)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
    elif event == "Color Rows":
        row_colors = []
        for idx, row in enumerate(data):
            amount = float(row[2])
            if amount < 0:
                row_colors.append((idx, "white", "red"))   # (row_index, text_color, background_color)
            else:
                row_colors.append((idx, "white", "green"))
        
        window["-TABLE-"].update(row_colors=row_colors)

window.close()
