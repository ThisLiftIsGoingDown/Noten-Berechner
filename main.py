import wx

class Notenskalierer (wx.Frame):

    def __init__(self, parent, title):
        super(Notenskalierer, self).__init__(parent, title = title, size = (300, 150))
        self.InitUI()

    
    def InitUI(self):
        #General Stuff
        panel = wx.Panel(self)
        panel.SetBackgroundColour('#696969')

        vbox = wx.BoxSizer(wx.VERTICAL)
        gridBox = wx.FlexGridSizer(4, 2, 10, 10)

        self.titleText = wx.StaticText(panel, label = "Notenskalen Berechnen")

        self.basicText = wx.TextCtrl(panel, -1, "", size=(175, -1))
        someTxt = wx.StaticText(panel, -1, "Maximalpunktzahl:")

        okButton = wx.Button(panel, -1, "OK")
        okButton.Bind(wx.EVT_BUTTON, self.OnOk)

        

        gridBox.AddMany([ (someTxt, 1, wx.EXPAND), (self.basicText, 1, wx.EXPAND),])

        vbox.Add(self.titleText, 0, wx.ALIGN_CENTER)
        vbox.Add(gridBox, wx.ID_ANY, wx.EXPAND | wx.ALL, 10)
        vbox.Add(okButton, 0, wx.ALIGN_CENTER)
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

    def OnOk(self, e):
        tmp = self.basicText.GetValue()
        try:
            tmp = float(tmp)
        except:
            self.numberError = wx.MessageDialog(self, "Bitte geben sie eine Zahl ein!", "Fehler", wx.OK | wx.ICON_ERROR)
            self.numberError.ShowModal()

class SettingsDialogue(wx.Dialog):
        def __init__(self, parent, title):
            super(SettingsDialogue, self).__init__(parent, title = title, size = (300, 200))
            self.InitUI()
    
        def InitUI(self):
            self.SetTitle("Einstellungen")
            self.Centre()
            panel = wx.Panel(self)
            panel.SetBackgroundColour('#696969')

            boxSizerSettings = wx.BoxSizer(wx.VERTICAL)
            zugGrid = wx.GridSizer(4, 2, 20, 20)

            self.multipleScale = wx.CheckBox(panel, -1, "Notenskalen für 3 verschiedene Leistungszüge")

            self.pzug = wx.StaticText(panel, -1, "P zug prozent")
            self.azug = wx.StaticText(panel, -1, "A zug prozent")
            self.ezug = wx.StaticText(panel, -1, "E zug prozent")
            self.pProzent = wx.TextCtrl(panel, -1, "", size=(175, -1))
            self.eProzent = wx.TextCtrl(panel, -1, "", size=(175, -1))
            self.aProzent = wx.TextCtrl(panel, -1, "", size=(175, -1))

            self.multipleScale.Bind(wx.EVT_CHECKBOX, self.OnMultipleScale)

            
            zugGrid.AddMany([ (self.pzug, 1, wx.EXPAND), (self.pProzent, 1, wx.EXPAND), (self.azug, 1, wx.EXPAND), (self.aProzent, 1, wx.EXPAND), (self.ezug, 1, wx.EXPAND), (self.eProzent, 1, wx.EXPAND)])
            boxSizerSettings.Add(self.multipleScale, 0, wx.ALIGN_CENTER)
            boxSizerSettings.Add(zugGrid, wx.ID_ANY, wx.EXPAND | wx.ALL, 10)
            panel.SetSizer(boxSizerSettings)
            self.Show(True)

        def OnMultipleScale(self, e):
            if self.multipleScale.GetValue():
                self.pProzent.Enable()
                self.eProzent.Enable()
                self.aProzent.Enable()
            else:
                self.pProzent.Disable()
                self.eProzent.Disable()
                self.aProzent.Disable()            


def main():
    app = wx.App()
    Notenskalierer(None, "Notenskalierer")
    app.MainLoop()

if __name__ == '__main__':
    main()

