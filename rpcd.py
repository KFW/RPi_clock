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
        calendar.grid(row=0, column=0, sticky=tk.W)
        clock.config(text=time2)
        clock.grid(row=0, column=1, sticky=tk.E)
        countdown = bjcmg - today
        cd = str(countdown.days)
        count.config(text= cd + ' days!')
        count.grid(row=2,columnspan=2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    clock.after(200, tick)
root = tk.Tk()
root.configure(background='#7ea0d6')
root.geometry('790x470+5+5')
root.title = 'HIP Countdown Clock'
tk.Label(root, text='BJCMG goes live in:', font=('helvetica', 48, 
            'bold'), bg='#7ea0d6').grid(row=1, columnspan=2, sticky=tk.W)
calendar = tk.Label(root, font=('helvetica', 36), bg='#7ea0d6')
clock = tk.Label(root, font=('helvetica', 48, 'bold'), bg='#7ea0d6')
count = tk.Label(root, font=('helvetica', 48, 'bold'), bg='#7ea0d6')

# clock.pack(fill='both', expand=1)
tick()
root.mainloop()