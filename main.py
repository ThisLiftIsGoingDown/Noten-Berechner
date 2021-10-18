import wx

class Notenskalierer (wx.Frame):

    def __init__(self, parent, title):
        super(Notenskalierer, self).__init__(parent, title = title, size = (300, 200))
        self.InitUI()

    
    def InitUI(self):
        # Menubar
        menu = wx.MenuBar()
        fileMenu = wx.Menu()
        fileSettings = fileMenu.Append(wx.ID_ANY, '&Einstellungen', 'Einstellungen')
        fileQuit = fileMenu.Append(wx.ID_EXIT, '&Beenden', 'Beenden')        
        menu.Append(fileMenu, '&Datei')
        self.SetMenuBar(menu)
        #Menubar Bindings
        self.Bind(wx.EVT_MENU, self.OnQuit, fileQuit)
        self.Bind(wx.EVT_MENU, self.OnSettings, fileSettings)
        self.SetTitle("Notenskalierer")
        
        self.Centre()
        self.Show(True)

    def OnQuit(self, e):
        self.Close()
    
    def OnSettings(self, e):
        SettingsDialogue(self,"Einstellungen")

class SettingsDialogue(wx.Dialog):
        def __init__(self, parent, title):
            super(SettingsDialogue, self).__init__(parent, title = title, size = (300, 200))
            self.InitUI()
    
        def InitUI(self):
            self.SetTitle("Einstellungen")
            self.Centre()
            self.Show(True)

def main():
    app = wx.App()
    Notenskalierer(None, "Notenskalierer")
    app.MainLoop()

if __name__ == '__main__':
    main()