import time as time
import tkinter as tk

clicks = []
clicks.append(time.time())
count = 0
seconds = 0
minutes = 0
hours = 0
iter = 0
log = []
iter_0 = 0

def button_click():
    global iter, count, minutes, hours, seconds
    clicks.append(time.time())
    duration_total = clicks[iter+1] - clicks[iter]
    duration_h = duration_total//60//24
    duration_m = duration_total//60%24
    duration_s = duration_total%60
    count = 0; seconds = 0; minutes = 0; hours = 0
    string_to_save = f"Activity '{activity}' registered at '{time.ctime()}'. Duration: '{duration_h} h, {duration_m} m, {duration_s:.2f} s'."
    print(string_to_save)
    log.append(string_to_save)
    logs_label.append(tk.Label(root, text=string_to_save))
    logs_label[len(log)-1].pack(pady=5)
    iter += 1

def update_counter():
    global count, minutes, seconds, hours, activity
    count += 1
    seconds = count
    if seconds/60 >= 1:
        count = 0
        seconds = 0
        minutes += 1
        if minutes/60 >= 1:
            minutes = 0
            hours += 1
    counter_label.config(text=f"Time counted: {hours} hours, {minutes} minutes, {seconds} seconds")
    root.after(1000, update_counter)  # Schedule update_counter to run again after 1000 milliseconds (1 second)
    activity = input_entry.get()

def saveLog():
    global log
    print("Day log was sucessfully saved.")
    with open("log_{}".format(time.strftime("%d_%b_%Y")), 'a') as f:
        for reg in log:
            f.write(f'{reg}\n')

# Create the main window
root = tk.Tk()
root.title("Time Counter")



# Insert Activity
input_label = tk.Label(root, text="Activity:")
input_label.pack(pady=5)
input_entry = tk.Entry(root)
input_entry.pack(pady=5)


# Create a button
button = tk.Button(root, text="Register", command=button_click)
button.pack(pady=10)

# Create a label to display the counter
counter_label = tk.Label(root, text=" ")
counter_label.pack()

# Create a Log button
button_log = tk.Button(root, text="Save log", command=saveLog)
button_log.pack(pady=10)


# LOG show
log_label = tk.Label(root, text="Log:")
log_label.pack(pady=5)

# LOG show
logs_label = []
log_r_label = tk.Label(root, text="")
log_r_label.pack(pady=5)

# Start updating the counter
update_counter()

# Start the GUI event loop
root.mainloop()