import tkinter as tk
from tkinter import filedialog, Text
import os

# holds the application

root = tk.Tk()

apps =[]
# if the file path is in save.txt, open the file and read the information which
# is stored as tempApps and then printed
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()] # removes extra space

# function that opens file explorer and shows only executables and .exe
def addApp():
    # Widget gives access to everything attached to the frame
    # This also keeps the labels from repeating on every selection by destroying
    # and updating the old labels
    for widget in frame.winfo_children():
        widget.destroy()

    filename= filedialog.askopenfilename(initialdir="/",
    title="Select File", filetypes = (("executables","*.exe"), ("all files", "*.*")))
    #add apps filename to apps list
    apps.append(filename)
    print(filename)
    #loop that creates a label for selected apps
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

# Function that loops over the apps in applist and opens the file
def runApps():
    for app in apps:
        os.startfile(app)
# Canvas edits the window
canvas = tk.Canvas(root, height=700, width=700, bg="lightslategray")
canvas.pack() # attaches the canvas to the app root

# create a frame within the window
frame = tk.Frame(root, bg="paleturquoise")
# relx=0.1, rely=0.1 centers the frame in the window
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# Create a buttons that is attached to the root
#Command = addApp creates the click event for the button
openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()# attaches the button to the app root
#Command = runApp creates the click event for the button
runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()# attaches the button to the app root

for app in apps:
    label =tk.Label(frame, text=app)
    label.pack()
root.mainloop()

#creates a file to save the list of apps to when the application closes
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app +',')