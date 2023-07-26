from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from random import randint


class RandomNumberGenerator(BoxLayout):
    def __init__(self, **kwargs):
        super(RandomNumberGenerator, self).__init__(**kwargs)

        self.orientation = "vertical"

        self.random_number_label = Label(text="Tap the button to generate a random number")
        self.add_widget(self.random_number_label)

        self.generate_button = Button(text="Generate", size_hint=(1, 0.5))
        self.generate_button.bind(on_press=self.generate_random_number)
        self.add_widget(self.generate_button)

    def generate_random_number(self, instance):
        random_number = randint(1, 100)
        self.random_number_label.text = f"Random Number: {random_number}"


class RandomNumberApp(App):
    def build(self):
        return RandomNumberGenerator()


if __name__ == '__main__':
    RandomNumberApp().run()
