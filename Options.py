from tkinter import *
from tkinter import ttk
from tkinter import font

import json

class OptionsWindow(Toplevel):
    def __init__(self, my_text):

        #window settings
        super().__init__()
        self.geometry("600x400")

        #variables
        self.inputs = []
        self.inputs_data = []
        self.options_data = OptionData(self.inputs ,my_text )

        #title
        self.Main_Title()

        #frame 
        self.font_Frame()
        

    # display the main title
    def Main_Title(self ):
        main_title = Label(self,text="Option Menu", font=("Poppins",20)).pack()

    # display the font frame and its widgets
    def font_Frame(self):
    
        font_frame = Frame(self )
        font_frame.pack(expand=True,fill=BOTH, pady=15)

        self.Widgets(font_frame , "Font")

    #display the widgets with data from json file
    def Widgets(self ,frame,sectionName ):
        #get data from json file (keys , values , dict)
        data = self.options_data.read_Data(sectionName)

        #variables
        Keys = data[0]
        Values = data[1]

        box_options = []
        box_value = []

        int_values = []

        InputTypes = []

        #for each value in Values check if it is a list or some thing else
        #if it is a list it is a Box else it is an entry 
        for value in Values:

            if str(type(value)) == "<class 'list'>":
                InputTypes.append("box")
                box_options.append(value[0])
                box_value.append(value[1])

                int_values.append(0)

            else:
                InputTypes.append("entry")
                box_options.append([])
                box_value.append("")

                int_values.append(value)
            

        for key in range(len(Keys)):
            self.lables(frame , Keys[key], key)
            self.Inputs(frame ,InputTypes[key], key ,int_values[key] ,box_value[key] ,box_options[key])


        self.save_button(frame ,key + 1)

    #create the labels 
    def lables(self , frame, label_text, posY):

        label = Label(frame,text=label_text , font=("Poppins",14)) 
        label.grid(column=0,row=posY,pady=8 , padx=10 )

    #create the Inputs
    def Inputs(self , frame ,InputTypes ,posY , entry_value ,box_value ,box_options):

        if InputTypes == "entry":
            entry = Entry(frame , width=25 )
            entry.grid(column=1 , row= posY)

            entry.insert(0,entry_value)

            self.inputs.append(entry)
        
        if InputTypes == "box":

            box = ttk.Combobox(frame , width= 25 , values=box_options ,state="readonly")
            box.set(box_value)

            box.grid(column=1 , row= posY)

            self.inputs.append(box)
            

    def save_button(self ,frame , PosY):

        save_button = Button(frame, text="Save", font = ("Poppins",17) ,command= self.on_click)
        save_button.grid(column=0 , row=PosY)


    def on_click(self):
       self.options_data.save_Data("Font")
       self.options_data.configure("Font")
        

    def get_inputs_data(self ):
        self.inputs_data = self.inputs.get()


class OptionData():
    def __init__(self , inputs , my_Text , *args):
        self.inputs = inputs
        self.my_Text = my_Text


    def readJsonFile(self):
        with open("Setting.json","r") as f:
            jsonFileDir = json.load(f)


        return jsonFileDir

        
    def read_Data(self , section):
        #read json file as python dir
        jsonFileDirSection = self.readJsonFile()[section]

        keys = list(jsonFileDirSection.keys())
        values = list(jsonFileDirSection.values())

        return keys , values ,jsonFileDirSection
    
    
    def save_Data(self , section_key ):
        #read json file as python dir
        dic = self.readJsonFile()
        Section = dic[section_key]
        keys = list(Section.keys())


        for i in range(len(Section)):

            if str(type(self.inputs[i])) == "<class 'tkinter.Entry'>":
                if str(type(self.inputs[i])) == "<class 'int'>":

                    dic[section_key][keys[i]] = int(self.inputs[i].get())
                else:
                    dic[section_key][keys[i]] = self.inputs[i].get()

            else:
                dic[section_key][keys[i]][1] = self.inputs[i].get()


        with open("Setting.json","w") as f:
            json.dump(dic,f,indent=4)


    def configure(self , section):
        jsonFileDir = self.read_Data(section)[2]
        
        self.my_Text.config(font= (jsonFileDir["FontType"][1],jsonFileDir["FontSize"] , jsonFileDir["FontStyle"][1]))