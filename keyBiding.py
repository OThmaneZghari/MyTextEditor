from fileManager import FileSettings

class Biding():
    def __init__(self , parent , mainField) :
        self.parent = parent
        self.fileSetting = FileSettings(parent , mainField)
        self.key_biding()


    def key_biding(self):
        self.parent.bind_all('<Control-n>', self.New)
        self.parent.bind_all('<Control-o>', self.Open)
        self.parent.bind_all('<Control-s>', self.Save)
        self.parent.bind_all('<Control-Alt-s>', self.SaveAs)

    def New(self , event):
        self.fileSetting.New_command()
    def Open(self , event):
        self.fileSetting.Open_command(True)
    def Save(self , event):
        self.fileSetting.Save_command()
    def SaveAs(self , event):
        self.fileSetting.SaveAs_command()