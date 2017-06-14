import time
import tkinter as tk
import datetime as dt

window_size = '800x480'
go_lives = [('BJCMG', dt.date(2017,6,1)),
            ('Boone', dt.date(2017,8,5)),
            ('Pod 1', dt.date(2017,12,2)), 
            ('Pod 2', dt.date(2018,2,3)),
            ('Academic', dt.date(2018,6,2)),
            ('Memorial', dt.date(2018,10,1))                      
           ]

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
        for i in range(len(go_lives)): # using regular iteration would be hard 
                                # since I need next item as well
                                # this will break after academic go-live,
                                # but will do for now
            if go_lives[i][1] > today:
                countdown1 = go_lives[i][1] - today
                h1 = go_lives[i][0]
                countdown2 = go_lives[i+1][1] - today
                h2 = go_lives[i+1][0]
                break
        cd1 = str(countdown1.days)
        cd2 = str(countdown2.days)
        hosp1.config(text= h1 + ' goes live in:')
        hosp1.grid(row=1, columnspan=2)
        count1.config(text= cd1 + ' days')
        count1.grid(row=2,columnspan=2)
        hosp2.config(text= h2 + ' goes live in:')
        hosp2.grid(row=3, columnspan=2)
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
calendar = tk.Label(root, font=('helvetica', 32), bg='#7ea0d6')
clock = tk.Label(root, font=('helvetica', 80, 'bold'), bg='#7ea0d6', fg='blue4')
hosp1 = tk.Label(root, font=('helvetica', 24, 'bold'), bg='#7ea0d6')
count1 = tk.Label(root, font=('helvetica', 48, 'bold'), bg='#7ea0d6')
hosp2 = tk.Label(root, font=('helvetica', 24, 'bold'), bg='#7ea0d6')
count2 = tk.Label(root, font=('helvetica', 48, 'bold'), bg='#7ea0d6')

# clock.pack(fill='both', expand=1)
tick()
root.mainloop()
