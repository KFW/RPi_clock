import time
import tkinter as tk
import datetime as dt

message1string = 'Clinical Informatics'
message2string = 'Froedtert & MCW'

window_size = '800x480'

def tick():

    # get the current local time from the PC
    time_now = time.strftime('%H:%M')
    today = dt.date.today()
    cal_day.config(text=today.strftime("%A"))
    cal_day.grid(row=0, column=0, sticky=tk.W)
    cal_date.config(text=today.strftime("%x"))
    cal_date.grid(row=0, column=1, sticky=tk.E)
    clock.config(text=time_now)
    clock.grid(row=1, columnspan=2)

    cd_line1.grid(row=2, columnspan=2)
    cd_line1.config(text = message1string)
    cd_line2.grid(row=3, columnspan=2)
    cd_line2.config(text = message2string)

    # calls itself every 200 milliseconds
    # to update the time display as needed
    clock.after(200, tick)

root = tk.Tk()
root.configure(background='#7ea0d6')
root.geometry(window_size)
root.columnconfigure(1, weight=1)
root.title('KFW Clock')
cal_day = tk.Label(root, font=('helvetica', 48), bg='#7ea0d6')
cal_date = tk.Label(root, font=('helvetica', 48), bg='#7ea0d6')
clock = tk.Label(root, font=('helvetica', 128, 'bold'), bg='#7ea0d6', fg='blue4')
cd_line1 = tk.Label(root, font=('helvetica', 32), bg='#7ea0d6')
cd_line2 = tk.Label(root, font=('helvetica', 24), bg='#7ea0d6')

# Not actually sure at this point why it keeps looping like it does
# I don't recall where I saw the example code
tick()
root.mainloop()
