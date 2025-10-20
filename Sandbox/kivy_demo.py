"""
CP1404 Practical 05 - Kivy Layout Demo
Estimated time: 10 min
Actual time: ?
"""

from kivy.app import App
from kivy.lang import Builder


class KivyDemoApp(App):
    """Simple Kivy app to demonstrate layout with extra label."""

    def build(self):
        self.title = "Kivy Layout Demo"
        self.root = Builder.load_file('kivy_layout.kv')
        return self.root

    def press_button(self):
        """Handle button press."""
        print("Button pressed!")

    def handle_enter(self, text):
        """Handle Enter key press in TextInput."""
        print(f"You entered: {text}")


if __name__ == '__main__':
    KivyDemoApp().run()
