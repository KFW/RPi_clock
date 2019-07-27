import time
import tkinter as tk
import datetime as dt

window_size = '800x480'
go_lives = [('Fall Ftr Release', dt.date(2019,10,13)),
            ('Spring Ftr Release', dt.date(2050,1,1)),
            ('HB Pilot', dt.date(2050,8,1)),     # date > 1000 days in future for now so ??? displayed
           ]

def msg_string(pod, countdown):
    if countdown.days == 1:
        return pod + ' live in: 1 day'
    elif countdown.days > 1000:
        return pod + ' live in: ??? days'
    else:
        return pod + ' live in: ' + str(countdown.days) + ' days'

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
        for index, site in enumerate(go_lives):
            if site[1] > today:
                countdown = site[1] - today
                pod = site[0]
                site1string = msg_string(pod, countdown)
                if (index + 1) < len(go_lives): # there are additional sites
                    countdown = go_lives[index + 1][1] - today
                    pod = go_lives[index + 1][0]
                    site2string = msg_string(pod, countdown)
                else:
                    site2string = "----------"
                break
        cd_line1.grid(row=2, columnspan=2)
        cd_line1.config(text = site1string)
        cd_line2.grid(row=3, columnspan=2)
        cd_line2.config(text = site2string)

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
cd_line2 = tk.Label(root, font=('helvetica', 32), bg='#7ea0d6')

# clock.pack(fill='both', expand=1)
tick()
root.mainloop()
