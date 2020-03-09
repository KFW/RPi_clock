import time
import tkinter as tk
import datetime as dt

window_size = '800x480'
# future enhancement - put dates in separate file so don't have to keep changing code
events = [  ('Dad - BD', dt.date(2020,3,14)),
            ('Ann - BD', dt.date(2020,3,29)),
            ('I2 Sympsm', dt.date(2020,4,10)),
            ('HI Team Bldg', dt.date(2020,4,24)),
            ('XGM', dt.date(2020,5,4)),
            ('AMIA CI', dt.date(2020,5,19)),
            ('ID Attdg', dt.date(2020,5,25)),
            ('UGM', dt.date(2020,8,24)),
            ('Deutschland', dt.date(2020,9,12)),
            ('Maker Camp', dt.date(2020,10,9))
           ]

def msg_string(event_name, countdown):
    if countdown.days == 1:
        return event_name + ' is in: 1 day'
    elif countdown.days > 1000:
        return event_name + ' is in: ??? days'
    else:
        return event_name + ' is in: ' + str(countdown.days) + ' days'

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
        for index, event in enumerate(events):
            if event[1] > today:
                countdown = event[1] - today
                event_name = event[0]
                event1string = msg_string(event_name, countdown)
                if (index + 1) < len(events): # there are additional sites
                    countdown = events[index + 1][1] - today
                    event_name = events[index + 1][0]
                    event2string = msg_string(event_name, countdown)
                else:
                    event2string = "----------"
                break
        cd_line1.grid(row=2, columnspan=2)
        cd_line1.config(text = event1string)
        cd_line2.grid(row=3, columnspan=2)
        cd_line2.config(text = event2string)

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
