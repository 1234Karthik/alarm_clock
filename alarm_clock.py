from tkinter import Button, Entry, Label, OptionMenu, StringVar, Tk, messagebox
from datetime import datetime
from threading import Thread
from win10toast import ToastNotifier
from packages import mytime
from time import sleep


def on_closing():
    reply = messagebox.askquestion("Alarm", "If the alarm is still running, the program will run in the background and won't notify when the alarm is done. \nDo you want to close the program?")
    if reply == "yes":
        messagebox.showwarning("Alarm", "Please end the program in task manager if you set an alarm")
        window.destroy()


def SetAlarm():
    bufferTime = datetime.now()

    if int(hour_enter.get()) < 24 and int(min_enter.get()) < 60:
        try:
            set_alarm.grid_forget()

            sleep(mytime.time_to_second(mytime.time_difference_hour(int(hour_enter.get())), mytime.time_difference_min(int(min_enter.get()))))

            if option.get() == "Pop Up":
                messagebox.showinfo("Alarm", f"{alarm_name_enter.get()}")
                            
            if option.get() == "Notification":
                notification = ToastNotifier()
                notification._show_toast("Alarm", alarm_name_enter.get(), "", 10)
        
        except ValueError:
            messagebox.showerror("Error", "Error running code! \nReason: Enter Charecter/String instead of Number")

    else:
        messagebox.showerror("Alarm Clock", "Hour cannot be greater than 23 and minutes cannot be greater than 59")

        
window = Tk()
window.title("Alarm Clock")
window.iconbitmap("E:\\ImQWERTY\\VSC\\pictures\\clock.ico")

hour_label = Label(window, text = 'Time(Hours)    ')
hour_label.grid(row=0, column=0)

hour_enter = Entry(window)
hour_enter.grid(row=1, column=0)

min_label = Label(window, text = 'Time(Minutes)    ')
min_label.grid(row=0, column=1)

min_enter = Entry(window)
min_enter.grid(row=1, column=1)

alarm_name = Label(window, text = "Alarm Name    ")
alarm_name.grid(row=0, column=2)

alarm_name_enter = Entry(window)
alarm_name_enter.grid(row=1, column=2)

func = Thread(target = SetAlarm)

set_alarm = Button(window, text = "Start", command = func.start)
set_alarm.grid(row=2, column=1)


alarm_name = Label(window, text = "Alarm Type")
alarm_name.grid(row=0, column=3)

option = StringVar()
option.set("Pop Up")

alarm_notification_type = OptionMenu(window, option, "Pop Up", "Notification")
alarm_notification_type.grid(row = 1, column = 3)


window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()