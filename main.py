#!/usr/local/bin/python3
import kivy
import datetime
# my package
import nlp
# kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
# to use buttons:
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView


class ConnectPage(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        prev_username = 'Anonymous'
        self.cols = 2

        self.add_widget(Label(text='Username:'))
        self.username = TextInput(text=prev_username, multiline=False)
        self.add_widget(self.username)

        # add our button.
        self.join = Button(text="Join")
        self.join.bind(on_press=self.join_button)
        self.add_widget(Label())  # just take up the spot.
        self.add_widget(self.join)

    def join_button(self, instance):
        username = self.username.text
        # Create chat page and activate it
        chat_app.create_chat_page()
        chat_app.screen_manager.current = 'Chat'


class ScrollableLabel(ScrollView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = GridLayout(cols=1, size_hint_y=None)
        self.add_widget(self.layout)

        self.chat_history = Label(size_hint_y=None, markup=True)
        self.scroll_to_point = Label()

        # We add them to our layout
        self.layout.add_widget(self.chat_history)
        self.layout.add_widget(self.scroll_to_point)

    # Methos called externally to add new message to the chat history
    def update_chat_history(self, message):

        # First add new line and message itself
        self.chat_history.text += '\n' + message

        self.layout.height = self.chat_history.texture_size[1] + 14
        self.chat_history.height = self.chat_history.texture_size[1]
        self.chat_history.text_size = (self.chat_history.width * 0.98, None)

        self.scroll_to(self.scroll_to_point)


class ChatPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # !!! instantantiate nlp class here
        self.nlp = nlp.NLP()

        # We are going to use 1 column and 2 rows
        self.cols = 1
        self.rows = 2

        self.history = ScrollableLabel(
            height=Window.size[1]*0.9, size_hint_y=None)
        self.add_widget(self.history)

        self.new_message = TextInput(width=Window.size[0]*0.8,
                                     size_hint_x=None, multiline=False)
        self.send = Button(text="Send")
        self.send.bind(on_press=self.send_message)

        bottom_line = GridLayout(cols=2)
        bottom_line.add_widget(self.new_message)
        bottom_line.add_widget(self.send)
        self.add_widget(bottom_line)

        # To be able to send message on Enter key, we want to listen to keypresses
        Window.bind(on_key_down=self.on_key_down)
        # to create and call a function that takes no parameters
        Clock.schedule_once(self.focus_text_input, 1)
    # Gets called on key press
    def on_key_down(self, instance, keyboard, keycode, text, modifiers):

        # But we want to take an action only when Enter key is being pressed, and send a message
        if keycode == 40:
            self.send_message(None)
    # Gets called when either Send button or Enter key is being pressed
    # (kivy passes button object here as well, but we don;t care about it)

    def send_message(self, _):
        # Get message text and clear message input field
        message = self.new_message.text
        self.new_message.text = ''

        # If there is any message - add it to chat history and send to the server
        if message:
            # Our messages - use red color for the name
            self.history.update_chat_history(
                f'[color=999]{datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")}[/color] '
                f'[color=dd2020]{chat_app.connect_page.username.text}'
                f'[/color] > {message}')
            # socket_client.send(message)
            # !!!! implement message handling service here
            # self.incoming_message('me',message)
            response = self.nlp.process(
                chat_app.connect_page.username.text, message)
            self.incoming_message('Funny bot', response)

        # As mentioned above, we have to shedule for refocusing to input field
        Clock.schedule_once(self.focus_text_input, 0.1)

    # Sets focus to text input field
    def focus_text_input(self, _):
        self.new_message.focus = True

    # Passed to sockets client, get's called on new message
    def incoming_message(self, username, message):
        # Update chat history with username and message, green color for username
        self.history.update_chat_history(
            f'[color=999]{datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")}[/color] '
            f'[color=20dd20]{username}[/color] > {message}')


class EpicApp(App):

    def build(self):

        self.screen_manager = ScreenManager()

        self.connect_page = ConnectPage()
        screen = Screen(name='Connect')
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

    def create_chat_page(self):
        self.chat_page = ChatPage()
        screen = Screen(name='Chat')
        screen.add_widget(self.chat_page)
        self.screen_manager.add_widget(screen)


def show_error(message):
    chat_app.info_page.update_info(message)
    chat_app.screen_manager.current = 'Info'
    Clock.schedule_once(sys.exit, 10)


# GUI module taken from:
# https://pythonprogramming.net/finishing-chat-application-kivy-application-python-tutorial/?completed=/chat-application-kivy-application-python-tutorial/
if __name__ == "__main__":
    chat_app = EpicApp()
    chat_app.run()
