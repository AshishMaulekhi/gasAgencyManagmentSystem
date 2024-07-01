import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error

# Database connection
def connect_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='gas_management',
            user='root',
            password='Lavanu#1'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        messagebox.showerror("Database Connection Error", str(e))
        return None

# CRUD operations
def create_record(gas_type, quantity, price_per_unit, date):
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO gas_records (gas_type, quantity, price_per_unit, date) VALUES (%s, %s, %s, %s)",
                       (gas_type, quantity, price_per_unit, date))
        connection.commit()
        cursor.close()
        connection.close()

def read_records():
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM gas_records")
        records = cursor.fetchall()
        cursor.close()
        connection.close()
        return records

def update_record(record_id, gas_type, quantity, price_per_unit, date):
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE gas_records SET gas_type=%s, quantity=%s, price_per_unit=%s, date=%s WHERE id=%s",
                       (gas_type, quantity, price_per_unit, date, record_id))
        connection.commit()
        cursor.close()
        connection.close()

def delete_record(record_id):
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM gas_records WHERE id=%s", (record_id,))
        connection.commit()
        cursor.close()
        connection.close()

# Tkinter UI
class GasManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gas Management System")

        # Form labels and entries
        self.label_gas_type = tk.Label(root, text="Gas Type")
        self.label_gas_type.grid(row=0, column=0, padx=10, pady=10)
        self.entry_gas_type = tk.Entry(root)
        self.entry_gas_type.grid(row=0, column=1, padx=10, pady=10)

        self.label_quantity = tk.Label(root, text="Quantity")
        self.label_quantity.grid(row=1, column=0, padx=10, pady=10)
        self.entry_quantity = tk.Entry(root)
        self.entry_quantity.grid(row=1, column=1, padx=10, pady=10)

        self.label_price_per_unit = tk.Label(root, text="Price Per Unit")
        self.label_price_per_unit.grid(row=2, column=0, padx=10, pady=10)
        self.entry_price_per_unit = tk.Entry(root)
        self.entry_price_per_unit.grid(row=2, column=1, padx=10, pady=10)

        self.label_date = tk.Label(root, text="Date (YYYY-MM-DD)")
        self.label_date.grid(row=3, column=0, padx=10, pady=10)
        self.entry_date = tk.Entry(root)
        self.entry_date.grid(row=3, column=1, padx=10, pady=10)

        # Buttons
        self.button_add = tk.Button(root, text="Add Record", command=self.add_record)
        self.button_add.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.button_update = tk.Button(root, text="Update Record", command=self.update_record)
        self.button_update.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.button_delete = tk.Button(root, text="Delete Record", command=self.delete_record)
        self.button_delete.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        self.button_view = tk.Button(root, text="View Records", command=self.view_records)
        self.button_view.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        # Treeview for displaying records
        self.tree = ttk.Treeview(root, columns=("ID", "Gas Type", "Quantity", "Price Per Unit", "Date"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Gas Type", text="Gas Type")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Price Per Unit", text="Price Per Unit")
        self.tree.heading("Date", text="Date")
        self.tree.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

        self.tree.bind("<Double-1>", self.on_tree_select)

    def add_record(self):
        gas_type = self.entry_gas_type.get()
        quantity = self.entry_quantity.get()
        price_per_unit = self.entry_price_per_unit.get()
        date = self.entry_date.get()
        if gas_type and quantity and price_per_unit and date:
            create_record(gas_type, quantity, price_per_unit, date)
            messagebox.showinfo("Success", "Record added successfully")
            self.view_records()
        else:
            messagebox.showerror("Input Error", "All fields are required")

    def view_records(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        records = read_records()
        for record in records:
            self.tree.insert("", "end", values=record)

    def on_tree_select(self, event):
        selected_item = self.tree.selection()[0]
        record = self.tree.item(selected_item, "values")
        self.entry_gas_type.delete(0, tk.END)
        self.entry_gas_type.insert(0, record[1])
        self.entry_quantity.delete(0, tk.END)
        self.entry_quantity.insert(0, record[2])
        self.entry_price_per_unit.delete(0, tk.END)
        self.entry_price_per_unit.insert(0, record[3])
        self.entry_date.delete(0, tk.END)
        self.entry_date.insert(0, record[4])
        self.selected_record_id = record[0]

    def update_record(self):
        gas_type = self.entry_gas_type.get()
        quantity = self.entry_quantity.get()
        price_per_unit = self.entry_price_per_unit.get()
        date = self.entry_date.get()
        if gas_type and quantity and price_per_unit and date:
            update_record(self.selected_record_id, gas_type, quantity, price_per_unit, date)
            messagebox.showinfo("Success", "Record updated successfully")
            self.view_records()
        else:
            messagebox.showerror("Input Error", "All fields are required")

    def delete_record(self):
        selected_item = self.tree.selection()[0]
        record = self.tree.item(selected_item, "values")
        if messagebox.askyesno("Delete Confirmation", f"Are you sure you want to delete the record with ID {record[0]}?"):
            delete_record(record[0])
            messagebox.showinfo("Success", "Record deleted successfully")
            self.view_records()

if __name__ == "__main__":
    root = tk.Tk()
    app = GasManagementApp(root)
    root.mainloop()
