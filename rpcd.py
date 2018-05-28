import time
import tkinter as tk
import datetime as dt

window_size = '800x480'
go_lives = [('Academic', dt.date(2018,6,2)),
            ('Mem Med Grp', dt.date(2050,2,2)),     # date > 1000 days in future for now so ??? displayed
            ('Memorial', dt.date(2050,8,1)),
           ]


def tick(time1=''):
    # get the current local time from the PC
    time2 = time.strftime('%H:%M')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        today = dt.date.today()
        cal_day.config(text=today.strftime("%A"))
        cal_day.grid(row=0, column=0, sticky=tk.W)
        cal_date.config(text=today.strftime("%x"))
        cal_date.grid(row=0, column=1, sticky=tk.E)
        clock.config(text=time2)
        clock.grid(row=1, columnspan=2)
        for site in go_lives:
            if site[1] > today:
                countdown = site[1] - today
                pod = site[0]
                break
        cd_line.grid(row=2, columnspan=2)
        if countdown.days == 1:
            cd_line.config(text=  pod + ' goes live in: 1 day')
        elif countdown.days > 1000:
            cd_line.config(text= pod + ' goes live in: ??? days')
        else:
            cd_line.config(text= pod + ' goes live in: ' + str(countdown.days) + ' days')

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
cd_line = tk.Label(root, font=('helvetica', 32), bg='#7ea0d6')


# clock.pack(fill='both', expand=1)
tick()
root.mainloop()
