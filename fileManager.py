from tkinter import *
from tkinter import filedialog

class FileSettings():
    def __init__(self , parent , mainField) :
        self.parent = parent
        self.my_Text = mainField[0]
        self.path_Label = mainField[1]
        self.file_path = ""

        parent.bind_all('<Key>', self.check_for_edit)

        self.Open_command(False)


    def New_command(self):
        self.my_Text.delete(1.0,END)
        self.parent.title("Undefined - TextEditor")
        self.file_path = ""
        self.path_Label.config(text = "Undifind",)
        self.removeStar()
        self.saving_filePath()

    def Open_command(self , isFileDialog):
        document_path = "C:\nUsers\noutma\nOneDrive\nImages\nDocuments"

        if isFileDialog:
            self.file_path = filedialog.askopenfilename(initialdir=document_path , title="Select File" , 
                                               filetypes=(("All files","*"),("text file",".*txt"),))
        else:
            self.file_path = self.getFilePathFromFile()

        print(self.file_path)
        try :

        
            self.file_name = self.FindFileName(self.file_path)
    
            self.parent.title(f"{self.file_name} - TextEditor")
            self.path_Label.config(text = self.file_path)

        

            #opening the file and read the content
            with open(self.file_path , "r") as file:
                content = file.read()

            self.my_Text.delete("1.0",END)
            self.my_Text.insert("1.0",content)
        except :
            print("file not found")
        
        self.removeStar()
        self.saving_filePath()
        

    def Save_command(self):
        #getting the content then writing the file
        try :

            with open(self.file_path,"w") as file:
                my_text_Content = self.my_Text.get(1.0 ,END)
                file.write(my_text_Content)

        except:
            self.SaveAs_command()

        self.removeStar()
        self.saving_filePath()


    def SaveAs_command(self):
        fileFirstLine_b = self.my_Text.get(1.0,2.0)
        fileFirstLine = fileFirstLine_b[0:fileFirstLine_b.find("\n")]
        print(fileFirstLine)

        try:
            save_file = filedialog.asksaveasfilename (filetypes=[("all files","*"),("text file","*.txt")] ,defaultextension=".txt",title="TextEditor",initialfile=f"{fileFirstLine}.txt" )
        
        
            with open(save_file,"w") as file:
                my_text_Content = self.my_Text.get(1.0 ,END)
                file.write(my_text_Content)

            file_name = self.FindFileName(save_file)
            self.parent.title(f"{file_name} - TextEditor")
            self.file_path = save_file
            self.path_Label.config(text = self.file_path)
            self.removeStar()
            self.saving_filePath()

        except :
            pass


    def Exit_command(self):
        self.parent.quit()

    def check_for_edit(self , event):

        if  self.parent.title()[0] != "*":
            self.parent.title(f"*{self.parent.title()}")
        
    def removeStar(self):
            self.parent.title(self.parent.title().replace("*",""))

    def saving_filePath(self):
        with open("file_path.txt", "w") as f:
            f.write(self.file_path)

    def getFilePathFromFile(self):
        with open("file_path.txt", "r") as f:
            content = f.read()
            
        return content
        


    def FindFileName(self,file_path):
        letter_pos = 0
        indexes = []

        for letter in file_path:

            if letter == "/":
                indexes.append(letter_pos)

            letter_pos += 1

        return file_path [max(indexes) + 1 :] 