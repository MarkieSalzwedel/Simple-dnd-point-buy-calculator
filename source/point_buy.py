import tkinter as tk
from tkinter import font
import math

all_a_plus_buttons = []
all_a_num_values = []
all_b_num_values = []
all_point_cost_values = []
all_total_values = []
all_mod_values = []

def point_buy_table(root, label_txt, index, col_s, total_points_label, point_cost_rows):
    
    if(index == 6):
        a_reset = tk.Button(root,text="RESET", width=10, command=lambda:a_reset_click(all_a_num_values, all_b_num_values, total_points_label, all_point_cost_values, point_cost_rows, all_total_values, all_mod_values))
        a_reset.grid(row=index+1, column=col_s, padx=10, pady=10)

        b_reset = tk.Button(root,text="RESET", width=10, command=lambda:b_reset_click(all_a_num_values, all_b_num_values, all_total_values, all_mod_values))
        b_reset.grid(row=index+1, column=col_s+2, padx=10, pady=10)
    else:
        # ATTRIBUTE label
        label_A = tk.Label(root, text=label_txt, anchor="w", bg="black", fg="white")
        label_A.grid(row=index+1, column=0, padx=10, pady=10, sticky="w")

        # "+" Label
        label_plus = tk.Label(root, text="+", bg="black", fg="white")
        label_plus.grid(row=index+1, column=col_s + 1, padx=10, pady=10)

        # "=" Label
        label_minus = tk.Label(root, text="=", bg="black", fg="white")
        label_minus.grid(row=index+1, column=col_s + 3, padx=10, pady=10)

        # Total
        label_total = tk.Label(root, text="8", bg='black', fg="white", width=3)
        label_total.grid(row=index+1, column=col_s + 4, padx=10, pady=10)

        # MOD
        label_mod = tk.Label(root, bg='white', fg="black", text="-1", width=3)
        label_mod.grid(row=index+1, column=col_s + 5, padx=10, pady=10)

        # Point cost
        label_pc = tk.Label(root, text="0", bg="black", fg="white")
        label_pc.grid(row=index+1, column=col_s + 6, padx=10, pady=10)

        # Append to lists
        all_point_cost_values.append(label_pc)
        all_total_values.append(label_total)
        all_mod_values.append(label_mod)

        # ---------------- ATTRIBUTE BUTTON 

        A_frame = tk.Frame(root)

        a_num = tk.Label(A_frame, text="8", bg="white",width=3)
        a_minus = tk.Button(A_frame,text="-",command=lambda:a_click(a_num, b_num, False, label_total, label_mod, index, point_cost_rows,total_points_label, label_pc), bg="white")
        a_plus = tk.Button(A_frame, text="+",command=lambda:a_click(a_num, b_num, True, label_total, label_mod, index, point_cost_rows,total_points_label, label_pc), bg="white")
        
        a_minus.pack(side="left")
        a_num.pack(side="left")
        a_plus.pack(side="left")

        A_frame.grid(row=index+1, column=col_s, padx=10, pady=10)

        # Append to list
        all_a_num_values.append(a_num)
        all_a_plus_buttons.append(a_plus)

        # ---------------- BONUS BUTTON

        B_frame = tk.Frame(root)

        b_num = tk.Label(B_frame, text="0", width=3)
        b_minus = tk.Button(B_frame,text="-",command=lambda:b_click(a_num, b_num, False, label_total, label_mod))
        b_plus = tk.Button(B_frame, text="+",command=lambda:b_click(a_num, b_num, True, label_total, label_mod))
        
        b_minus.pack(side="left")
        b_num.pack(side="left")
        b_plus.pack(side="left")

        B_frame.grid(row=index+1, column=col_s+2, padx=10, pady=10)

        # Append to list
        all_b_num_values.append(b_num)

        label_total.config(text=str(int(a_num.cget("text")) + int(b_num.cget("text"))))

def a_click(a_num, b_num, x, label_total, label_mod, index, point_cost_rows, total_points_label, label_pc):
    # Get the num in ATTRIBUTE label
    num = int(a_num.cget("text"))
    
    # If True, then add
    if(x):
        num = min(num+1, 20)
    # Else, subtract
    else:
        num = max(num-1, 1)

    a_num.config(text=str(num))

    # Calculate point cost
    point_cost = num - 8
    point_cost_rows[index] = point_cost
    total_point_cost = sum(point_cost_rows)
    point_value = max(27 - total_point_cost, 0)

    label_pc.config(text=point_cost)
    total_points_label.config(text=f"{point_value}/27")

    # Update total label
    update_label_total(a_num, b_num, label_total, label_mod)

    # Disable ALL "+" if point_value is 0
    update_all_a_plus_buttons(point_value)

def a_reset_click(all_a_num_values, all_b_num_values, total_points_label, all_point_cost_values, point_cost_rows, all_total_values, all_mod_values):
    for i, num in enumerate(all_a_num_values):
        # Reset label
        num.config(text="8")
        # Reset points
        all_point_cost_values[i].config(text="0")
        point_cost_rows[i] = 0
        # Reset total labels
        sum = int(all_a_num_values[i].cget("text")) + int(all_b_num_values[i].cget("text"))
        all_total_values[i].config(text=str(sum))
        # Reset mod labels
        calc_mod(all_total_values[i], all_mod_values[i])

    # Reset total
    total_points_label.config(text="27/27")

    # Re-enable all "+" buttons
    update_all_a_plus_buttons(27)

def b_click(a_num, b_num, x, label_total, label_mod):
    # Get the num in BONUS label
    num = int(b_num.cget("text"))

    # If True, then add
    if(x):
        num = min(num+1, 5)
    # Else, subtract
    else:
        num = max(num-1, 0)

    b_num.config(text=str(num))

    # Update total label
    update_label_total(a_num, b_num, label_total, label_mod)

def b_reset_click(all_a_num_values, all_b_num_values, all_total_values, all_mod_values):
    for i, num in enumerate(all_b_num_values):
        num.config(text="0")

        # Reset total labels
        sum = int(all_a_num_values[i].cget("text")) + int(all_b_num_values[i].cget("text"))
        all_total_values[i].config(text=str(sum))
        # Reset mod labels
        calc_mod(all_total_values[i], all_mod_values[i])

def update_all_a_plus_buttons(point_value):
    for button in all_a_plus_buttons:
        button.config(state='normal' if point_value > 0 else 'disabled')

def update_label_total(a_num, b_num, label_total, label_mod):
    a_val = int(a_num.cget("text")) if a_num else 0
    b_val = int(b_num.cget("text")) if b_num else 0
    
    total = a_val + b_val
    label_total.config(text=str(total))
    calc_mod(label_total, label_mod)

def calc_mod(label_total, label_mod):
    # Get total value
    total = int(label_total.cget("text"))
    temp_val = (total - 10) / 2
    # Round down the value
    mod_val = math.floor(temp_val)

    # positive mod value gets "+"
    if (mod_val >= 0):
        label_mod.configure(text="+" + str(mod_val))
    else:
        label_mod.configure(text=str(mod_val))

def grid_header(root, label_txt, col):
    # Define a bold font
    bold_font = font.Font(family="Helvetica", size=9, weight="bold")

    # Create label
    label = tk.Label(root, text=label_txt, font=bold_font, bg="black", fg="white")
    label.grid(row=0, column=col, padx=10, pady=10)

def main():
    # Create main window
    root = tk.Tk()
    root.title("D&D Point Buy!")
    root.geometry("710x365")
    root.configure(bg="black")

    root.resizable(False, False)

    # Set up grid headers
    grid_header_list = ["ATTRIBUTE", "ABILITY SCORE", " ", "BONUS", " ", "TOTAL", "MODIFIER", "POINT COST"]
    # Set up rows
    attributes_list = ["Strength (STR)", "Dexterity (DEX)", "Constitution (CON)", "Intelligence (INT)", "Wisdom (WIS)", "Charisma (CHA)", " "]

    # Label for total points
    bold_font = font.Font(family="Helvetica", size=9, weight="bold")

    total_points_label = tk.Label(root, text="27/27", font=bold_font, bg="black", fg="white")
    total_points_label.grid(row=0, column=8, padx=10, pady=10)

    # Track point cost for each attribute
    point_cost_rows = [0] * (len(attributes_list)-1)

    # ---------------- BUILD GRID

    # Headers
    for i in range(len(grid_header_list)):
        grid_header(root, grid_header_list[i], i)

    # Rows
    for i in range(len(attributes_list)):
        point_buy_table(root, attributes_list[i], i, 1, total_points_label, point_cost_rows)
    
    root.mainloop()

if __name__ == "__main__":
    main()