'''
This project is not mine. I have taken the code from the youtube channel "Alina Chudnova", link of the project is : https://youtu.be/uUWG5cm2Los?si=Df0bHbolhXCZVNzR
'''

#The Pomodoro Timer is a popular method of time-keeping during work, and provide a break from work at regular intervals, which can be argued to make a person more productive and efficient. Here after every 25 minutes of work, there is a short break of 5 minutes, and after every 4 such work times, there is a longer break of 15 minutes. 

import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import ttk, Style

# Set default time for work and break intervals
WORK_TIME = 25 * 60
SHORT_BREAK_TIME = 5 * 60
LONG_BREAK_TIME = 15 * 60

class PomodoroTimer:
    '''
    This class creates the Pomodoro Timer, with the required GUI with Tkinter.
    '''
    def __init__(self):
        '''
        This function initiates the Tkinter GUI for the timer app.
        '''
        self.root = tk.Tk()
        self.root.geometry("300x200")
        self.root.title("Pomodoro Timer")
        self.style = Style(theme="lumen")
        self.style.theme_use()

        self.timer_label = tk.Label(self.root, text="", font=("TkDefaultFont", 40))
        self.timer_label.pack(pady=20)

        self.start_button = ttk.Button(self.root, text="Start", command=self.start_timer)
        self.start_button.pack(pady=5)

        self.stop_button = ttk.Button(self.root, text="Stop", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        self.work_time, self.break_time = WORK_TIME, SHORT_BREAK_TIME
        self.is_work_time, self.pomodoros_completed, self.is_running = True, 0, False

        self.root.mainloop()
    
    def start_timer(self):
        '''
        This function initiates when a user presses the START button on the app.
        '''
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.is_running = True
        self.update_timer()

    def stop_timer(self):
        '''
        This function initiates when a user presses the STOP button on the app.
        '''
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.is_running = False
    
    def update_timer(self):
        '''
        This function initiates when a user presses the START button on the app. Here, it updates the time for each leg of the timer, and prints the messages on an alert box.
        '''
        if self.is_running:
            if self.is_work_time:
                self.work_time -= 1
                if self.work_time == 0:
                    self.is_work_time = False
                    self.pomodoros_completed += 1
                    self.break_time = LONG_BREAK_TIME if self.pomodoros_completed % 4 == 0 else SHORT_BREAK_TIME
                    messagebox.showinfo("Great Job!" if self.pomodoros_completed % 4 == 0
                                        else "Good job!", "Take a long break and rest your mind."
                                        if self.pomodoros_completed % 4 == 0
                                        else "Take a short break and strech your legs!")
            else:
                self.break_time -= 1
                if self.break_time == 0:
                    self.is_work_time, self.work_time = True, WORK_TIME
                    messagebox.showinfo("Work Time", "Get back to work!")
            minutes, seconds = divmod(self.work_time if self.is_work_time else self.break_time, 60)
            self.timer_label.config(text="{:02d}:{:02d}".format(minutes, seconds))
            self.root.after(1000, self.update_timer)

PomodoroTimer()
