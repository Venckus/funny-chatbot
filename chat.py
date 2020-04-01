#!/usr/local/bin/python3
import tkinter, threading
from tkinter import scrolledtext
from tkinter import ttk

class Gui(threading.Thread):

    def __init__(self, client):
        super().__init__(daemon=False, target=self.run)
        self.client = client
        # self.run()
        self.start_window = None
        self.chat_window = None

    def run(self):
        self.start_window = StartWindow(self)
        self.chat_window = ChatWindow(self)
        self.chat_window.run()

    def show_msg(self, message):
        self.chat_window.show_msg(message)

class Window(object):
    def __init__(self, title):
        self.root = tkinter.Tk() # ttk.Tk()
        self.title = title
        self.root.title(title)
    
class StartWindow(Window):
    def __init__(self, gui):
        self.gui = gui
        self.label = None
        self.entry = None
        self.button = None
        self.start = None

        self.build_window()
        self.run()
    
    def build_window(self):
        self.label = ttk.Label(self.root, text='Enter your name', width=20)
        self.label.pack(side=ttk.LEFT, expand=ttk.YES)

        self.entry = ttk.Entry(self.root, width=20)
        self.entry.focus_set()
        self.entry.pack(side=ttk.LEFT)
        self.entry.bind('<Return>', self.get_start_event)

        self.button = ttk.Button(self.root, text='Login')
        self.button.pack(side=ttk.LEFT)
        self.button.bind('<Button-1>', self.get_start_event)

    def run(self):
        self.root.mainloop()
        self.root.destroy()
    
    def get_start_event(self, event):
        self.login = self.entry.get()
        self.root.quit()

class ChatWindow(Window):
    def __init__(self, gui):
        super().__init__("Funny Python Chat")
        self.gui = gui
        self.messages_list = None
        self.entry = None
        self.send_button = None
        self.exit_button = None
        # self.lock = threading.RLock()
        self.target = ''
        self.login = self.gui.login_window.login

        self.build_window()

    def build_window(self):
        # Size config
        self.root.geometry('750x500')
        self.root.minsize(600, 400)

        # Frames config
        main_frame = ttk.Frame(self.root)
        main_frame.grid(row=0, column=0, sticky=ttk.N + ttk.S + ttk.W + ttk.E)

        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        # List of messages
        frame00 = ttk.Frame(main_frame)
        frame00.grid(column=0, row=0, rowspan=2, sticky=ttk.N + ttk.S + ttk.W + ttk.E)

         # Message entry
        frame02 = ttk.Frame(main_frame)
        frame02.grid(column=0, row=2, columnspan=1, sticky=ttk.N + ttk.S + ttk.W + ttk.E)

        # Buttons
        frame03 = ttk.Frame(main_frame)
        frame03.grid(column=0, row=3, columnspan=2, sticky=ttk.N + ttk.S + ttk.W + ttk.E)

        main_frame.rowconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=8)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

        # ScrolledText widget for displaying messages
        self.messages_list = scrolledtext.ScrolledText(frame00, wrap='word')
        self.messages_list.insert(ttk.END, 'Welcome to Python Chat\n')
        self.messages_list.configure(state='disabled')

        # Entry widget for typing messages in
        self.entry = ttk.Text(frame02)
        self.entry.focus_set()
        self.entry.bind('<Return>', self.send_entry_event)

        # Button widget for sending messages
        self.send_button = ttk.Button(frame03, text='Send')
        self.send_button.bind('<Button-1>', self.send_entry_event)

        # Button for exiting
        self.exit_button = ttk.Button(frame03, text='Exit')
        self.exit_button.bind('<Button-1>', self.exit_event)

        # Positioning widgets in frame
        self.messages_list.pack(fill=ttk.BOTH, expand=ttk.YES)
        self.logins_list.pack(fill=ttk.BOTH, expand=ttk.YES)
        self.entry.pack(side=ttk.LEFT, fill=ttk.BOTH, expand=ttk.YES)
        self.send_button.pack(side=ttk.LEFT, fill=ttk.BOTH, expand=ttk.YES)
        self.exit_button.pack(side=ttk.LEFT, fill=ttk.BOTH, expand=ttk.YES)

        # Protocol for closing window using 'x' button
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing_event)

    def run(self):
        self.root.mainloop()
        self.root.destroy()
    
    def exit_event(self, event):
        self.root.quit()

    def on_closing_event(self):
        self.exit_event(None)
    
    def show_msg(self, message):

        with self.lock:
            self.messages_list.configure(state='normal')
            self.messages_list.insert(ttk.END, message)
            self.messages_list.configure(state='disabled')
            self.messages_list.see(ttk.END)

class Client(threading.Thread):
    def __init__(self):
        #super().__init__(daemon=True, target=self.run)
        self.lock = threading.RLock()
        self.login = ''
        self.target = ''

        self.gui = Gui(self)
        # self.start()
        self.gui.start()

# Create new client with (IP, port)
if __name__ == '__main__':
    Client()