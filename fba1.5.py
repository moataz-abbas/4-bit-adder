import numpy as np
import logicadder as la

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
#from kivy.properties import NumericProperty


class MainLayout(BoxLayout):
    
    true_col = (0, 0.8, 1, .8)
    false_col = (.5, .4, .4, .8)
    result=[]
    
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.orientation='vertical'
        
        self.title= MyLabel(text=
                            'Welcome to 4-bit Adder', 
                            size_hint=(1, 0.15), 
                            font_size= '{}sp'.format(25), 
                            color=[0.25,0.25,0.4,1],
                            valign='middle',
                            halign='center'
                            )
        self.title.col=(.8, 0.7, .65, 1)
        self.add_widget(self.title)
        
        
        
        self.result_lyot= BoxLayout(size_hint=(1,0.4))
        self.add_widget(self.result_lyot)
        
        for _ in range(5):
            x= MyLabel(text='0', 
            valign='middle',
            halign='center', 
            #border_width=10
            )
            x.col = self.false_col
            self.result.append(x)
        for obj in self.result:
            self.result_lyot.add_widget(obj)
        
        self.separator=MyLabel(size_hint=(1,.004))
        self.separator.col=(0,0,0,1)
        self.add_widget(self.separator)
 
        self.firstLine = BoxLayout(orientation='horizontal', size_hint=(1,0.3))
        self.add_widget(self.firstLine)
        
        self.btn0 = MyTog(disabled=True)
        self.btn1 = MyTog(text='0')
        self.btn2 = MyTog(text='0')
        self.btn3 = MyTog(text='0')
        self.btn4 = MyTog(text='0')
        
        self.firstLine.add_widget(self.btn0)
        self.firstLine.add_widget(self.btn1)
        self.firstLine.add_widget(self.btn2)
        self.firstLine.add_widget(self.btn3)
        self.firstLine.add_widget(self.btn4)
        
        self.btn1.bind(state=self.on_mytog)
        self.btn2.bind(state=self.on_mytog)
        self.btn3.bind(state=self.on_mytog)
        self.btn4.bind(state=self.on_mytog)
        
        self.secondLine = BoxLayout(orientation='horizontal', size_hint=(1,0.3))
        self.add_widget(self.secondLine)
        
        self.btnx = MyTog(disabled=True)
        self.btn5 = MyTog(text='0')
        self.btn6 = MyTog(text='0')
        self.btn7 = MyTog(text='0')
        self.btn8 = MyTog(text='0')
        
        self.secondLine.add_widget(self.btnx)
        self.secondLine.add_widget(self.btn5)
        self.secondLine.add_widget(self.btn6)
        self.secondLine.add_widget(self.btn7)
        self.secondLine.add_widget(self.btn8)
        
        self.btn5.bind(state=self.on_mytog)
        self.btn6.bind(state=self.on_mytog)
        self.btn7.bind(state=self.on_mytog)
        self.btn8.bind(state=self.on_mytog)
        
        
        
        
    def on_mytog(self, val, ins):
        a=self.btn1.text+self.btn2.text+self.btn3.text+self.btn4.text
        b=self.btn5.text+self.btn6.text+self.btn7.text+self.btn8.text
        
        a= [int(i) for i in a]
        b = [int(j) for j in b]
        print(f"a= {a}\nb= {b}")
        
        ans = la.fourBitAdder(a,b)
        print(ans)
        
        for i in range(5):
            if ans[i]:
                self.result[i].col = self.true_col
                self.result[i].text='1'
            else:
                self.result[i].col = self.false_col
                self.result[i].text='0'
            self.result[i].on_size()




class MyTog(ToggleButton):
    def on_state(self, *args):
        if (self.state=='down'):
            self.text='1'
        else:
            self.text= '0'
        
        
class MyLabel(Label):
    col=(0.5,0.5,0.5,1)
    def on_size(self, *args):
        self.text_size = self.size
        a,b,c,d = self.col
        self.canvas.before.clear()
        with self.canvas.before:
            Color(a,b,c,d)
            Rectangle(pos=self.pos, size=(self.size[0]-2,self.size[1]-2))
            


class FourBitAdderApp(App):
    def build(self):
        return MainLayout()
        	    
        
if __name__ in ('__main__'):
    FourBitAdderApp().run()