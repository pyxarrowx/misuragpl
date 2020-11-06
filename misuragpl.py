import kivy 
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import smtplib
import ssl

class MyGridLayout(GridLayout):
    
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        
        #Call grid layout constructopr
        super(MyGridLayout, self).__init__(**kwargs)
        
        #set colunms
        self.cols = 2

        #add widget Pressione PVF
        self.add_widget(Label(text="ID Impianto:"))
        #add input box Pressione PVF
        self.pvf = TextInput(multiline=False)
        self.add_widget(self.pvf)

        #add widget Pressione P1
        self.add_widget(Label(text="Pressione P1:"))
        #add input box Pressione P1
        self.p1 = TextInput(multiline=False)
        self.add_widget(self.p1)

        #add widget Pressione P2
        self.add_widget(Label(text="Pressione P2:"))
        #add input box Pressione P2
        self.p2 = TextInput(multiline=False)
        self.add_widget(self.p2)

        #add widget Volume Bombola
        self.add_widget(Label(text="Volome Bombola:"))
        #add input box Volume Bombola
        self.vb = TextInput(multiline=False)
        self.add_widget(self.vb)

        #add widget Volume Display
        self.add_widget(Label(text="Volome Display:"))
        #add input box Volume Display
        self.vm = TextInput(multiline=False)
        self.add_widget(self.vm)

        #create submit button
        self.submit = Button(text="Calcola", font_size=32)
        #bind the button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

        #create clear button
        self.clear = Button(text="Chiudi App", font_size=32)
        #bind clear button
        #self.clear.bind(on_press=self.clearfields)
        self.clear.bind(on_press=self.clkfunc)
        self.add_widget(self.clear)

    def clkfunc(self , obj):
        App.get_running_app().stop()
        Window.close()

    def clearfields(self, instance):
        #svuotamento delle caselle di testo
        self.p1.text = ""
        self.p2.text = ""
        self.vm.text = ""
        self.vb.text = ""

    def press(self, instance):
        #name = self.name.text vecchia variabile testo
        p1 = self.p1.text
        p2 = self.p2.text
        vm = self.vm.text
        vb = self.vb.text
        em = 18.76 * (float(p1)*5 - float(p2))
        vr = float(vb) - em
        ea = vr - float(vm)
        ee = ea / 20


        #print(f'Hello {name} {surname}, il tuo colore preferito è {color}')
        #stampa su schermo dei risultati
        self.add_widget(Label(text=f'Errore Misura = {round(em,2)}'))
        self.add_widget(Label(text=f'Volume Reale = {round(vr,2)}'))
        self.add_widget(Label(text=f'Errore Assoluto = {round(ea,2)}'))
        self.add_widget(Label(text=f'Errore Per Mille = {round(em)}'))


class Gmail(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.server = 'smtp.libero.it'
        self.port = 587
        session = smtplib.SMTP(self.server, self.port)        
        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(self.email, self.password)
        self.session = session
        #create button invia mail
        #self.smail = Button(text="Submit", font_size=32)
        #bind the button email
        #self.smail.bind(on_press=self.send_message)
        #self.add_widget(self.smail)

    def send_message(self, subject, body):
        ''' This must be removed '''
        headers = [
            "From: " + self.email,
            "Subject: " + subject,
            "To: " + self.email,
            "MIME-Version: 1.0",
           "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        self.session.sendmail(
            self.email,
            self.email,
            headers + "\r\n\r\n" + body)

    __version__ = 'some_version'
    

class MisuraGPLApp(App):
        #gm = Gmail('misuragpl@libero.it', 'mSrl-2020')
        #gm.send_message('Impianto: {pvf}', 'Misura del {}')
        def build(self):
            return MyGridLayout()

if __name__ == '__main__':
    MisuraGPLApp().run()

