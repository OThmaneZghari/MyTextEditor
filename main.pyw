from tkinter import *

from Options import OptionsWindow
from Options import OptionData

from fileManager import FileSettings
from keyBiding import Biding


class App(Tk):
    def __init__(self , title , size):
        #Some Constants
        Screen_Coor = (1680,1050)

        #main loop
        super().__init__()
        self.title(title)
        
        self.geometry(f"{size[0]}x{size[1]}+{int(Screen_Coor[0] / 16)}+{int(Screen_Coor[1] /16)}")
        self.minsize(size[0] , size[1])
        self.title("Undefined - TextEditor")

        # widgets
        mainField = MainField(self ).textFieldUtilities()

        #menu
        self.menu = SelectMenu(self,mainField)

        #key biding
        self.keyBiding = Biding(self , mainField)

        optionData = OptionData(my_Text= mainField[0] , inputs=None)
        optionData.configure("Font")

        # run
        self.mainloop()

class MainField(Frame):
    def __init__(self,parent  ):
        super().__init__(parent)

        self.my_Text = Text(self,undo = True,bd = 5 ,wrap=NONE)
        self.my_Text.pack(expand=True,fill = BOTH)


        #scroll Bars
        #vertical scroll bar
        vertical_scrollbar = Scrollbar(self.my_Text  , orient="vertical" , command=self.my_Text.yview)
        self.my_Text.configure(yscrollcommand=vertical_scrollbar.set)
        vertical_scrollbar.place(relx = 1,rely= 0 , relheight=1 , anchor="ne")

        #horizontal scroll bar
        horizontal_scrollbar = Scrollbar(self.my_Text , orient="horizontal" , command=self.my_Text.xview)
        self.my_Text.configure(xscrollcommand= horizontal_scrollbar.set)
        horizontal_scrollbar.place(relx = 0,rely= 1 , relwidth=1 , anchor="sw")
        #control
        self.my_Text.bind("<Control MouseWheel>", lambda event : self.my_Text.xview_scroll(-int(event.delta /60),"units"))

        self.PathLabel = Label(self  ,text= "Undifined",font=("Arial" , 14) )
        self.PathLabel.pack(side= RIGHT , expand=True , fill=BOTH)

        
        self.pack(expand=True,fill = BOTH)

    def textFieldUtilities(self):
        return self.my_Text ,self.PathLabel

class SelectMenu(Menu):
    def __init__(self,parent,mainField ):
        super().__init__(parent)

        self.parent = parent
        self.mainField = mainField

        self.filesettings = FileSettings(parent , self.mainField)

        #create Menu
        parent.config(menu = self)

        #add file Menu
        self.file_menu = Menu(self,tearoff=False)
        self.add_cascade(label="File",menu =self.file_menu)

        self.file_menu.add_command(label = "New                       Ctrl+N", command=self.filesettings.New_command    )
        self.file_menu.add_command(label = "Open                      Ctrl+O", command=lambda :self.filesettings.Open_command (True)  )
        self.file_menu.add_command(label = "Save                      Ctrl+S", command=self.filesettings.Save_command   )
        self.file_menu.add_command(label = "Save As             Ctrl+Shift+S", command=self.filesettings.SaveAs_command )
        self.file_menu.add_separator()
        self.file_menu.add_command(label = "Exit",command=self.filesettings.Exit_command   )

        #add edit Menu
        edit_menu = Menu(self,tearoff=False)
        self.add_cascade(label="Edit",menu=edit_menu)

        edit_menu.add_command(label="Cut")
        edit_menu.add_command(label="Copy")
        edit_menu.add_command(label="Undo")
        edit_menu.add_command(label="Redo")

        #add option Menu
        option_menu = Menu(self,tearoff=False)
        self.add_cascade(label="Options" , menu=option_menu)

        option_menu.add_command(label="Options",command=self.Open_Options)


    def Open_Options(self):
        self.option_menu = OptionsWindow(self.mainField[0])
        
if __name__ == "__main__":
    App("Class App", (1200,800)) 