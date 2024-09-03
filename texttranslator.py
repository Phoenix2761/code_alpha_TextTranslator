#Importing the GoogleTranslator frmo the deep_translator library
from deep_translator import GoogleTranslator

from tkinter import *

class ConversionWindow:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x500")
        
        self.label = Label(self.root, text="TextTranslator", font=('Times New Roman', 18))
        self.label.pack(pady=5)
        
        self.frame = Frame(self.root)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)
        
        # Creating the textbox where the user will type the text to be translated 
        self.inputtext = Text(self.frame, font=('Times New Roman', 18), height=5, width=15)
        # Placing the input textbox in the grid layout of self.frame at row 0 and column 0
        self.inputtext.grid(row=0, column=0)

        # Creating the textbox where the translated text will be displayed for the user
        self.outputtext = Text(self.frame, font=('Times New Roman', 18), height=5, width=15)
        # Placing the output textbox in the grid layout of self.frame at row 0 column 2
        self.outputtext.grid(row=0, column=2)

        # Creating an entry where the users types the language to be translated to
        self.language = Entry(self.frame, font=('Times New Roman', 18), width=30)
        # self.language.bind("<KeyPress>", self.altrun)
        # Placing the entry in the grid layout of self.frame at row 1 and letting it the span 3 columns 
        # starting from column 0
        self.language.grid(row=1, column=0, columnspan=3, sticky=E+W, pady=10)

        # Creating a button that upon clicking passes the function translate(self)-'created subsequently in the code'
        self.translatebutton = Button(self.frame, text="Translate", font=("Times New Roman", 16), command=self.translate)
        self.translatebutton.grid(row=2, column=1, pady=1)

        self.frame.pack()
        self.root.mainloop()
    
    # Creating the function that translates the text stored in the inputtext variable which was obtained from the 
    # inputtext variable's textbox, to the language specified by the user in the language variable's entry using 
    # GoogleTranslator via deep_translator API and displaying the translated text to the user via the outputtext variable's textbox.
    def translate(self):
        # Reading the value of the inputtext textbox and storing it in the userinput variable
        userinput = self.inputtext.get('1.0', END)
        # Reading the value of the language entry and storing it in the translate_To variable
        translate_to = self.language.get()
        
        # Obtaining the dictioanry of available languages and their respective abbreviations from the
        # the GoogleTranslatpr API and storing the dictionary in a variable named language_dict
        language_dict = GoogleTranslator().get_supported_languages(as_dict=True)

        # Removing any whitesapce on the left and right of teh language to be converted and converting the text 
        # to be converted to lowercase so that is can match the keys in the dictionary
        translate_to = translate_to.strip()
        translate_to = translate_to.lower()

        # Using the value of the translate_to variable which is the language that the value of the userinput 
        # variable is to be converted to, to obtain key with the same name in the language_dict dictionary. 
        # The value of the key is the abbreviated name of the language and this abbreviated name is saved 
        # to the variable translate_to_abbrev(Line 72) but if the value of the translate_to variable(the language 
        # to be translated to) is not in the language_dict dictionary, the content of the self.language entry
        # will be cleared and the user will be prompted with a 'Language not availabe' message in the 
        # self.language entry(Lines 69-71).
        if (translate_to in language_dict) == False:
            self.language.delete(0, END)
            self.language.insert(END, 'Language not available')
        translate_to_abbrev = language_dict.get(translate_to)

        # The translate_to_abbrev variable, which contains the abbreviation of language the user wants the value 
        # of self.userinput to be converted to and the value of the self.userinput are both passed to the 
        # GoogleTranslator() function as the target value and the argument for the translate method respectively 
        # hence converting the users text to the specified language.
        self.translated = GoogleTranslator(source="auto", target=translate_to_abbrev).translate(userinput)

        # Displaying the translated text to the user by, inserting the translated text which is the vlaue of 
        # the self.translated variable into the self.outputtext textbox.
        self.outputtext.insert('1.0', self.translated)
       

ConversionWindow()