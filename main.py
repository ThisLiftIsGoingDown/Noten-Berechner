import wx

class Notenskalierer (wx.Frame):

    def __init__(self, parent, title):
        super(Notenskalierer, self).__init__(parent, title = title, size = (300, 200))
        self.InitUI()

    
    def InitUI(self):
        #General Stuff
        panel = wx.Panel(self)
        panel.SetBackgroundColour('#696969')

        vbox = wx.BoxSizer(wx.VERTICAL)

        basicText = wx.TextCtrl(panel, -1, "Tomp", size=(175, -1))

        middlePanel = wx.Panel(panel)
        middlePanel.SetBackgroundColour('#11ef87')

        vbox.Add(middlePanel, wx.ID_ANY, wx.EXPAND | wx.ALL, 10)
        vbox.Add(basicText, wx.ID_ANY, wx.EXPAND | wx.ALL, 10)
        panel.SetSizer(vbox)


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