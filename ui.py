import tkinter as tk
from tkinter import ttk
import mysql.connector
import database


class App:
    def __init__(self, root):
        self.root = root
        self.db = database.Database()

        # Create a frame for the search and filter options
        self.search_frame = tk.Frame(self.root)
        self.search_frame.pack(side="top", fill="x")

        # Create a search entry
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(self.search_frame, textvariable=self.search_var)
        self.search_entry.pack(side="left", fill="x", expand=True)

        # Create a search button
        self.search_button = tk.Button(self.search_frame, text="Search", command=self.search)
        self.search_button.pack(side="left")
        
        # Create a frame for the results
        self.results_frame = tk.Frame(self.root)
        self.results_frame.pack(side="top", fill="both", expand=True)

        # Create a treeview to display the results
        self.tree = ttk.Treeview(self.results_frame)
        self.tree["columns"] = ("type", "sector", "resources", "individual", "email", "phone", "address", "date")
        self.tree.column("#0", width=100)
        self.tree.column("type", width=100)
        self.tree.column("sector", width=100)
        self.tree.column("resources", width=100)
        self.tree.column("individual", width=100)
        self.tree.column("email", width=100)
        self.tree.column("phone", width=100)
        self.tree.column("address", width=100)
        self.tree.column("date", width=100)
        self.tree.heading("#0", text="Name")
        self.tree.heading("type", text="Type")
        self.tree.heading("sector", text="Sector")
        self.tree.heading("resources", text="Resources")
        self.tree.heading("individual", text="Individual")
        self.tree.heading("email", text="Email")
        self.tree.heading("phone", text="Phone")
        self.tree.heading("address", text="Address")
        self.tree.heading("date", text="Date")
        self.tree.pack(side="top", fill="both", expand=True)
        
        #Search presets
        self.search_category = "name"
        self.search_term = ""
        self.filter_type=""
        self.filter_sector=""
        self.sort_category="name"
        self.order="ASC"
    
    def search(self):
        # Clear the treeview
        self.tree.delete(*self.tree.get_children())
        
        # Get the search term
        self.search_term = self.search_var.get()

        # Search, filter, and sort the database
        results = self.db.search_filter_sort(self.search_term, self.search_category, self.filter_type, 
                                             self.filter_sector, self.sort_category, self.order)

        # Add the results to the treeview
        for result in results:
            self.tree.insert("", "end", text=result[1], values=result[2:])
    

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()