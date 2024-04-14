import tkinter as tk
import threading

items = {
    'cake': 500,
    'pizza': 300,
    'ice-cream': 100,
    'momo': 100,
    'burger': 200,
    'french-fries': 80,
    'cold-drinks': 70,
    'coffee': 120,
    'milk-shake': 400,
    'chowmein': 100,
    'thukpa': 100,
    'fried-rice': 100
}

# Function to search for items and update the listbox
def search_item(item):
    search_results = [key for key in items.keys() if key.startswith(item)]
    update_listbox(search_results)

# Function to update the listbox with search results
def update_listbox(results):
    listbox.delete(0, tk.END)
    for result in results:
        listbox.insert(tk.END, result)

# Function to continuously update the search results
def live_search():
    search_item(search_entry.get())
    root.after(500, live_search)  # Update every 500 milliseconds

# Create the main window
root = tk.Tk()
root.title("Live Search")

# Create a search entry widget
search_entry = tk.Entry(root)
search_entry.pack(pady=10, padx=10)
search_entry.focus()

# Create a listbox to display search results
listbox = tk.Listbox(root)
listbox.pack(padx=10, pady=5)

# Start live search in a separate thread
thread = threading.Thread(target=live_search)
thread.daemon = True  # Daemonize the thread to stop it when the main program exits
thread.start()

# Run the Tkinter event loop
root.mainloop()
