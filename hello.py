import kivy 
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        #Call grid layout constructopr
        super(MyGridLayout, self).__init__(**kwargs)

        #set colunms
        self.cols = 2

        #add widget
        self.add_widget(Label(text="Nome:"))
        #add input box
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Cognome:"))
        #add input box
        self.surname = TextInput(multiline=False)
        self.add_widget(self.surname)

        self.add_widget(Label(text="Colore preferito:"))
        #add input box
        self.color = TextInput(multiline=False)
        self.add_widget(self.color)

        #create submit button
        self.submit = Button(text="Submit", font_size=32)
        #bind the butto
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)
    
    def press(self, instance):
        name = self.name.text
        surname = self.surname.text
        color = self.color.text

        #print(f'Hello {name} {surname}, il tuo colore preferito è {color}')
        #print to the crscreen
        self.add_widget(Label(text=f'Hello {name} {surname}, il tuo colore preferito è {color}'))

        #CLEAR INPUT BOXERS
        #self.name.text = ""
        #self.color.text = ""
        #self.surname.text = ""

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()

