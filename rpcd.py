import time
import tkinter as tk
import datetime as dt

window_size = '800x480'
bjcmg = dt.date(2017,6,1)
boone = dt.date(2017,8,5)

def tick(time1=''):
    # get the current local time from the PC
    time2 = time.strftime('%H:%M')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        today = dt.date.today()
        calendar.config(text=today.strftime("%a, %x"))
        calendar.grid(row=0, column=0, sticky=tk.W)
        clock.config(text=time2)
        clock.grid(row=0, column=1, sticky=tk.E)
        countdown1 = bjcmg - today
        countdown2 = boone - today
        cd1 = str(countdown1.days)
        cd2 = str(countdown2.days)
        count1.config(text= cd1 + ' days')
        count1.grid(row=2,columnspan=2)
        count2.config(text= cd2 + ' days')
        count2.grid(row=4,columnspan=2)        
    # calls itself every 200 milliseconds
    # to update the time display as needed
    clock.after(200, tick)
root = tk.Tk()
root.configure(background='#7ea0d6')
root.geometry(window_size)
root.columnconfigure(1, weight=1)
root.title('HIP Countdown Clock')
tk.Label(root, text='BJCMG goes live in:', font=('helvetica', 48, 
            'bold'), bg='#7ea0d6').grid(row=1, columnspan=2)
tk.Label(root, text='Boone goes live in:', font=('helvetica', 48, 
            'bold'), bg='#7ea0d6').grid(row=3, columnspan=2)
calendar = tk.Label(root, font=('helvetica', 48), bg='#7ea0d6')
clock = tk.Label(root, font=('helvetica', 80, 'bold'), bg='#7ea0d6', fg='blue4')
count1 = tk.Label(root, font=('helvetica', 64, 'bold'), bg='#7ea0d6')
count2 = tk.Label(root, font=('helvetica', 64, 'bold'), bg='#7ea0d6')

# clock.pack(fill='both', expand=1)
tick()
root.mainloop()