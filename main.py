import kivy
kivy.require('1.9.0')

import quotes
import random
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.label import Label


Builder.load_file('builder.kv')



class MyLayout(Widget):
    def generateQuote(self):
        quote = random.choice(quotes.slicedQuotes) # chosen quote from list of quotes in quotes.py
        altQuote = "" # new quote that contains newlines
        i = 0 # counter

        for char in quote: # iterates through quote string
            altQuote+=char # rebuilds quote into altQuote variable
            if char == " ": # Waits to find a space in quote
                i+=1 # adds 1 t counter

                if i % 6 == 0: # when there are at least 10 spaces....
                    altQuote+="\n" # add a new line

        colonIndex = altQuote.index(":") + 2 # find the index of the space after the colon but before the quote
        altQuote = altQuote[colonIndex:] # slice the quote so the quote #, colon, and space afterwards is removed
        self.ids.quote_view.text = altQuote # display the newly altered quote to the label on the user's screen

                    


class AspiringQuotesApp(App):
    def build(self):
        Window.clearcolor = (.1,0,.1,1)
        return MyLayout()

if __name__ == "__main__":
    AspiringQuotesApp().run()