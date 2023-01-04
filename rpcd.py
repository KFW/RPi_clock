import time
import tkinter as tk
import datetime as dt

# OK it may be lazy, and sloppy, but using globals in a program 
# this short just makes life easier
events = []
event1string = "-"
event2string = "-"

window_size = '800x480'

def msg_string(event_name, countdown):
    if countdown.days == 1:
        return event_name + ' is in: 1 day'
    elif countdown.days > 1000:
        return event_name + ' is in: ??? days'
    else:
        return event_name + ' is in: ' + str(countdown.days) + ' days'

def get_event_strings():
    global events
    global event1string
    global event2string

    event1string = " "
    event2string = "-----------"
    for index, event in enumerate(events):
        if event[1] > today:
            countdown = event[1] - today
            event_name = event[0]
            event1string = msg_string(event_name, countdown)
            if (index + 1) < len(events): # there are additional events
                countdown = events[index + 1][1] - today
                event_name = events[index + 1][0]
                event2string = msg_string(event_name, countdown)
            break
    return (event1string, event2string)

# update events list; handle errors if file not present by countdown to upcoming years
def get_events():
    global events 
    
    try:
        with open('events.txt') as f:   # 'events.txt must be in same directory as program file
            for line in f:
                l = line.strip().split(",")
                event = (l[0], dt.date(int(l[1]),int(l[2]), int(l[3])))
                events.append(event)
        return events
    except:
        events = [  ('2023', dt.date(2023,1,1)),
                    ('2024', dt.date(2024,1,1)),
                    ('2025', dt.date(2025,1,1)),
                    ('2026', dt.date(2026,1,1)),
                    ('2027', dt.date(2027,1,1)),
                    ('2028', dt.date(2028,1,1)),
                    ('2029', dt.date(2029,1,1)),
                    ('2030', dt.date(2030,1,1)),
                 ]
        return events

def tick():
    global today
    global events
    
    # check date - if new date then reload events file
    if today != dt.date.today():
        today = dt.date.today()
        get_events()

    # get the current local time from the PC
    time_now = time.strftime('%H:%M')
    today = dt.date.today()
    cal_day.config(text=today.strftime("%A"))
    cal_day.grid(row=0, column=0, sticky=tk.W)
    cal_date.config(text=today.strftime("%x"))
    cal_date.grid(row=0, column=1, sticky=tk.E)
    clock.config(text=time_now)
    clock.grid(row=1, columnspan=2)
    # for index, event in enumerate(events):
    #     if event[1] > today:
    #         countdown = event[1] - today
    #         event_name = event[0]
    #         event1string = msg_string(event_name, countdown)
    #         if (index + 1) < len(events): # there are additional events
    #             countdown = events[index + 1][1] - today
    #             event_name = events[index + 1][0]
    #             event2string = msg_string(event_name, countdown)
    #         else:
    #             event2string = "----------"
    #         break
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
cd_line2 = tk.Label(root, font=('helvetica', 24), bg='#7ea0d6')


# initialize
today = dt.date.today()
get_events()
get_event_strings()

# Not actually sure at this point why it keeps looping like it does
# I don't recall where I saw the example code
tick()
root.mainloop()
