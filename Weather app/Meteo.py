from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.network.urlrequest import UrlRequest


  


class Meteo(App):
    def build(self):
        
        self.window = GridLayout()     #crea griglia
        self.window.cols = 1    #crea colonna
        self.window.size_hint =(0.8,0.9)   #ridimensionare finestra app
        self.window.pos_hint ={'center_x': 0.5,'center_y': 0.5}   #centrare app
        
        Window.size = (360,640)   #risoluzione app
        self.img = Image(source="world.png")  
        self.window.add_widget(self.img)
        
        
        
        
        self.label = Label(text='Search For a City',   #tabella /aggiungere testo
                                      size_hint = (1,0.5),
                                      font_size = '18sp'
                                      )   
        self.window.add_widget(self.label) #aggiungere a schermo
       
       
        self.input_testo = TextInput(        #aggiungere input
                                size_hint = (1,0.15),   #100% asse x ;  20% asse y
                                font_size = '18sp',  #modificare font
                                padding_y='10sp'   #dare padding al testo
                                )  
        self.window.add_widget(self.input_testo) #aggiungere a schermo
        
        
        
        self.btn = Button(text='Search',        #aggiungere un bottone
                                      size_hint = (1,0.1),
                                      bold = True,
                                      background_color = '#000000', #colore backg
                                      font_size = '18sp',    #grandezza testo
                                      border = (30, 30, 30, 30),                   
                                      pos_hint = {"x":0.35, "y":0.3},
                                      
                                      color = '#1E90FF'    #colore testo
                                      )
         
        self.window.add_widget(self.btn) #add to screen
        self.btn.bind(on_press=self.found_temp)    #a method get called when the button is pressed
     

        
        return self.window 
    def found_temp(self,instance):   #argomenti da associare quando si tratta di on_press
        
        def edit_label(reqeust,result):
            temp = result['main']['feels_like']
            #API
            self.label.text = f"Today in " + self.input_testo.text +  " there are "+ str(temp) + "°C"
        
        link = f'https://api.openweathermap.org/data/2.5/weather?q={self.input_testo.text}&appid=59b3200b5d95f3314706c33dfc1aaddd&units=metric'
        UrlRequest (link,edit_label)
    
   

Meteo().run()