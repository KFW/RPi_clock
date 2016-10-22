import time
import tkinter as tk
import datetime as dt

bjcmg = dt.date(2017,6,1)

def tick(time1=''):
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        today = dt.date.today()
        calendar.config(text=today.strftime("%a, %x"))
        calendar.grid(row=0, column=0)
        clock.config(text=time2)
        clock.grid(row=0, column=1)
        countdown = bjcmg - today
        cd = str(countdown.days)
        count.config(text='BJCMG goes live in ' + cd + ' days!')
        count.grid(row=1)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    clock.after(200, tick)
root = tk.Tk()
root.configure(background='#7ea0d6')
calendar = tk.Label(root, font=('helvetica', 75, 'bold'), bg='#7ea0d6')
clock = tk.Label(root, font=('helvetica', 75, 'bold'), bg='#7ea0d6')
count = tk.Label(root, font=('helvetica', 75, 'bold'), bg='#7ea0d6')

# clock.pack(fill='both', expand=1)
tick()
root.mainloop()