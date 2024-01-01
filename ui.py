import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import database


class App:
    def __init__(self, root):
        self.root = root
        self.db = database.Database()
        
        # Set the initial size of the window
        root.geometry("800x600")

        # Create a frame for the search and filter options
        self.search_frame = tk.Frame(self.root)
        self.search_frame.pack(side="top", fill="x")

        # Create a search entry
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(self.search_frame, textvariable=self.search_var, bg='white', fg='black', font=('Times New Roman', 16))
        self.search_entry.pack(side="left", fill="x", expand=True)

        # Create a search button
        self.search_button = tk.Button(self.search_frame, text="Search", command=self.update, bg='white', fg='black', font=('Times New Roman', 12))
        self.search_button.pack(side="left")

        # Bind the search function to the Enter key
        self.search_entry.bind("<Return>", lambda event: self.update())

        # Create a frame for the results
        self.results_frame = tk.Frame(self.root)
        self.results_frame.pack(side="top", fill="both", expand=True)

        # Create a treeview to display the results
        self.tree = ttk.Treeview(self.results_frame)
        self.columns = ("name", "type", "sector", "resources", "individual", "email", "phone", "address", "date", "id")
        self.tree["columns"] = self.columns[1:]
        self.tree.column("#0", width=100)
        self.tree.column("type", width=100)
        self.tree.column("sector", width=100)
        self.tree.column("resources", width=100)
        self.tree.column("individual", width=100)
        self.tree.column("email", width=100)
        self.tree.column("phone", width=100)
        self.tree.column("address", width=100)
        self.tree.column("date", width=100)

        # id column is a placeholder and will not be shown to the user
        self.tree.column("id", width=0, stretch=tk.NO)

        self.tree.heading("#0", text="Name")
        self.tree.heading("type", text="Type")
        self.tree.heading("sector", text="Sector")
        self.tree.heading("resources", text="Resources")
        self.tree.heading("individual", text="Individual")
        self.tree.heading("email", text="Email")
        self.tree.heading("phone", text="Phone")
        self.tree.heading("address", text="Address")
        self.tree.heading("date", text="Date")

        # Create a context menu
        self.context_menu = tk.Menu(self.root, tearoff=0)
        self.context_menu.add_command(label="Edit", command=self.edit_selected_cell)
        self.context_menu.add_command(label="Delete", command=self.delete_selected_cell)

        # Mouse event listener
        self.tree.bind("<ButtonRelease-1>", self.column_header_clicked)
        self.tree.bind("<Double-ButtonRelease-1>", self.double_click_event)
        self.tree.bind("<Button-3>", self.show_context_menu)
        self.tree.pack(side="left", fill="both", expand=True)

        # Create a vertical scrollbar
        y_scrollbar = ttk.Scrollbar(self.results_frame, orient="vertical", command=self.tree.yview)
        y_scrollbar.pack(side="right", fill="y")

        # Configure the treeview to use the vertical scrollbar
        self.tree.configure(yscrollcommand=y_scrollbar.set)

        # Search presets
        self.search_category = "name"
        self.search_term = ""
        self.filter_type = ""
        self.filter_sector = ""
        self.sort_category = "name"
        self.order = "ASC"

        # Initialize tree content
        self.update()

    def update(self):
        # Clear the treeview
        self.tree.delete(*self.tree.get_children())

        # Get the search term
        self.search_term = self.search_var.get()

        # Search, filter, and sort the database
        results = self.db.search_filter_sort(
            self.search_term, self.search_category, self.filter_type, self.filter_sector, self.sort_category, self.order
        )

        # Add the results to the treeview
        for result in results:
            self.tree.insert("", "end", text=result[1], values=result[2:] + (result[0],))

    # Change sort_category based on column
    def column_header_clicked(self, event):
        region = self.tree.identify_region(event.x, event.y)
        if region == "heading":
            column_id = int(self.tree.identify_column(event.x).split("#")[-1])
            if self.sort_category != self.columns[column_id]:
                self.sort_category = self.columns[column_id]
                self.order = "ASC"
            elif self.order == "ASC":
                self.order = "DESC"
            else:
                self.order = "ASC"
            self.update()

    def double_click_event(self, event):
        return

    def show_context_menu(self, event):
        region = self.tree.identify("region", event.x, event.y)
        if "cell" in region:
            region = self.tree.identify("row", event.x, event.y)
            # Deselect all other rows
            self.tree.selection_remove(self.tree.get_children())
            # Select the clicked row
            self.tree.selection_add(region)
            # Display the context menu at the right-clicked location
            self.context_menu.post(event.x_root, event.y_root)

    def edit_selected_cell(self):
        selected_items = self.tree.selection()
        if selected_items:
            if self.confirm_action("Edit", "Are you sure you want to edit this row?"):
                return
            # Need to implement a way for the user to edit

    def delete_selected_cell(self):
        selected_items = self.tree.selection()
        if selected_items:
            if self.confirm_action("Edit", "Are you sure you want to delete this row?"):
                selected_item_values = self.tree.item(selected_items, 'values')
                self.db.delete(selected_item_values[-1])
                self.update()

    def confirm_action(self, action, message):
        result = messagebox.askyesno(f"Confirm {action}", message)
        return result


def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
