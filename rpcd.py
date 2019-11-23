import time
import tkinter as tk
import datetime as dt

window_size = '800x480'
# future enhancement - put dates in separate file so don't have to keep changing code
events = [('Thanksgiving', dt.date(2019,11,28)),
            ('Christmas', dt.date(2019,12,25)),
            ('New Years', dt.date(2020,01,01)),
            ('MLK', dt.date(2020,01,20)),
            ('Holland', dt.date(2020,02,01)),
            ('G - BD', dt.date(2020,02,28)),
            ('Dad - BD', dt.date(2020,03,14))
           ]

def msg_string(event, countdown):
    if countdown.days == 1:
        return event + ' is in: 1 day'
    elif countdown.days > 1000:
        return event + ' is in: ??? days'
    else:
        return event + ' is in: ' + str(countdown.days) + ' days'

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
        for index, site in enumerate(events):
            if site[1] > today:
                countdown = site[1] - today
                pod = site[0]
                site1string = msg_string(event, countdown)
                if (index + 1) < len(events): # there are additional sites
                    countdown = events[index + 1][1] - today
                    event = events[index + 1][0]
                    site2string = msg_string(event, countdown)
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
