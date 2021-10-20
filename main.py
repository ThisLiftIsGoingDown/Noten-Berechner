import wx
import wx.grid
from markCalc import MarkCalculator

class Notenskalierer (wx.Frame):

    def __init__(self, parent, title):
        super(Notenskalierer, self).__init__(parent, title = title, size = (300, 300))
        
        self.InitUI()
        
    
    def InitUI(self):
        #General Stuff
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('#696969')
        
        self.aBox = wx.BoxSizer(wx.VERTICAL)
        vbox = wx.BoxSizer(wx.VERTICAL)
        gridBox = wx.FlexGridSizer(5, 2, 10, 10)

        self.titleText = wx.StaticText(self.panel, label = "Notenskalen Berechnen")

        self.basicText = wx.TextCtrl(self.panel, -1, "", size=(175, -1))
        someTxt = wx.StaticText(self.panel, -1, "Maxmalpunktzahl:")

        self.percentageText = wx.StaticText(self.panel, -1, "Test prozent:")
        self.percentage = wx.TextCtrl(self.panel, -1, "", size=(175, -1))


        okButton = wx.Button(self.panel, -1, "OK")
        okButton.Bind(wx.EVT_BUTTON, self.OnOk)

        

        

        gridBox.AddMany([ (someTxt, 1, wx.EXPAND), (self.basicText, 1, wx.EXPAND)])
        gridBox.AddMany([ (self.percentageText, 1, wx.EXPAND), (self.percentage, 1, wx.EXPAND)])

        vbox.Add(self.titleText, 0, wx.ALIGN_CENTER)
        vbox.Add(gridBox, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)
        vbox.Add(okButton, 0, wx.ALIGN_CENTER)

        self.panel.SetSizer(vbox)
        self.UpdateSettings()

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

    def UpdateSettings(self):
        self.settings = wx.Config("Notenskalierer")
        self.percentage.SetValue("")
        if  self.settings.ReadBool('multipleScales'):
            self.percentage.Disable()
        else:
            self.percentage.Enable()

    def OnOk(self, e):
        self.marks = list()
        self.settings=wx.Config("Notenskalierer")
        tmp = self.basicText.GetValue()
        try:
            tmp = float(tmp)
        except:
            self.numberError = wx.MessageDialog(self, "Bitte geben Sie eine Zahl ein!", "Fehler", wx.OK | wx.ICON_ERROR)
            self.numberError.ShowModal()
            return
        if not self.settings.ReadBool('multipleScales'):
            tmp2 = self.percentage.GetValue()
            try:
                tmp2 = float(tmp2)
            except:
                self.numberError = wx.MessageDialog(self, "Bitte geben Sie eine Zahl ein!", "Fehler", wx.OK | wx.ICON_ERROR)
                self.numberError.ShowModal()
                return
            if tmp2 > 100:
                self.numberError = wx.MessageDialog(self, "Bitte geben Sie eine Zahl zwischen 0 und 100 ein!", "Fehler", wx.OK | wx.ICON_ERROR)
                self.numberError.ShowModal()
                return
            print(MarkCalculator.calculateMarkScalePercent(tmp, tmp2))
            self.marks.append(MarkCalculator.calculateMarkScalePercent(tmp, tmp2))
            ResultDialogue(self, 'Ergebnisse', marks=self.marks)
            
        else:
            percentages = [self.settings.ReadFloat(f'{zug}Percent') for zug in ['p', 'e', 'a']]
            for percent in percentages:
                self.marks.append(MarkCalculator.calculateMarkScalePercent(tmp, percent))
                print(MarkCalculator.calculateMarkScalePercent(tmp, percent))
        ResultDialogue(self, 'Ergebnisse', marks=self.marks)
class ResultDialogue(wx.Dialog):
     def __init__(self, parent, title, marks):
            super(ResultDialogue, self).__init__(parent, title = title, size = (350, 200))
            self.parent = parent
            self.marks = marks
            self.InitUI()
     def InitUI(self):

        self.settings = wx.Config("Notenskalierer")

        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('ffffff')
        sz = wx.BoxSizer(wx.VERTICAL)

        self.markGrid = wx.grid.Grid(self)
        self.markGrid.CreateGrid(11,1)
        self.markGrid.SetRowSize(0, 20)
        self.markGrid.SetColSize(0, 100)
        self.markGrid.DeleteCols(0, 1)
        for column, markL in enumerate(self.marks):
            mar = 1.0
            self.markGrid.AppendCols(1)
            for row, mark in enumerate(markL):
                self.markGrid.SetRowLabelValue( row, f'{mar}')
                self.markGrid.SetCellValue( row, column, f'{int(mark)}')
                mar+=.5

        if not self.settings.ReadBool('multipleScales'):
            self.markGrid.SetColLabelValue(0, "Notenskala")
        else:
            zuege = ['P-Zug', 'E-Zug', 'A-Zug']
            for zug in zuege:
                self.markGrid.SetColLabelValue(zuege.index(zug), f'{zug}')

        
        sz.Add(self.markGrid, 1, wx.EXPAND | wx.ALL, 10)
        self.SetSizerAndFit(sz)
        self.Show(True)
class SettingsDialogue(wx.Dialog):
        def __init__(self, parent, title):
            super(SettingsDialogue, self).__init__(parent, title = title, size = (350, 200))
            self.parent = parent
            self.readSettings()
            self.InitUI()

        def readSettings(self):
            self.settings = wx.Config('Notenskalierer')

        def InitUI(self):
            self.SetTitle("Einstellungen")
            self.Centre()
            self.panel = wx.Panel(self)
            self.panel.SetBackgroundColour('#696969')

            boxSizerSettings = wx.BoxSizer(wx.VERTICAL)
            zugGrid = wx.GridSizer(4, 2, 20, 20)
            buttonGrid = wx.GridSizer(1, 2, 20, 20)

            self.multipleScale = wx.CheckBox(self.panel, -1, "Notenskalen für 3 verschiedene Leistungszüge")
            self.multipleScale.SetValue(self.settings.ReadBool('multipleScales'))
            self.multipleScale.Bind(wx.EVT_CHECKBOX, self.OnMultipleScale)

            self.filler = wx.StaticText(self.panel, -1, "")

            self.pzug = wx.StaticText(self.panel, -1, "P-Zug Prozent")
            self.azug = wx.StaticText(self.panel, -1, "A-Zug Prozent")
            self.ezug = wx.StaticText(self.panel, -1, "E-Zug Prozent")
            self.pProzent = wx.TextCtrl(self.panel, -1, f"{self.settings.ReadFloat('pProzent')}", size=(175, -1))
            self.eProzent = wx.TextCtrl(self.panel, -1, f"{self.settings.ReadFloat('eProzent')}", size=(175, -1))
            self.aProzent = wx.TextCtrl(self.panel, -1, f"{self.settings.ReadFloat('aProzent')}", size=(175, -1))

            self.okButton = wx.Button(self.panel, -1, "OK")
            self.cancelButton = wx.Button(self.panel, -1, "Abbrechen")

            self.okButton.Bind(wx.EVT_BUTTON, self.OnOk)
            self.cancelButton.Bind(wx.EVT_BUTTON, self.OnCancel)

            buttonGrid.AddMany([(self.okButton, 1, wx.EXPAND), (self.cancelButton, 1, wx.EXPAND)])
            zugGrid.AddMany([ (self.pzug, 1, wx.EXPAND), (self.pProzent, 1, wx.EXPAND), (self.azug, 1, wx.EXPAND), (self.aProzent, 1, wx.EXPAND), (self.ezug, 1, wx.EXPAND), (self.eProzent, 1, wx.EXPAND)])
            zugGrid.AddMany([(self.filler, 1, wx.EXPAND),(buttonGrid, 1, wx.EXPAND) ])
            boxSizerSettings.Add(self.multipleScale, 0, wx.ALIGN_CENTER)
            boxSizerSettings.Add(zugGrid, wx.ID_ANY, wx.EXPAND | wx.ALL, 10)
            self.panel.SetSizer(boxSizerSettings)
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
        
        def Save(self):
            self.settings.WriteBool('multipleScales', self.multipleScale.GetValue())
            self.settings.WriteFloat('pProzent', float(self.pProzent.GetValue()))
            self.settings.WriteFloat('eProzent', float(self.eProzent.GetValue()))
            self.settings.WriteFloat('aProzent', float(self.aProzent.GetValue()) )
            self.settings.Flush()
            self.parent.UpdateSettings()

        def OnOk(self, e):
            self.Save()
            self.Close() 

        def OnCancel(self, e):
            self.Close()       


def main():
    app = wx.App()
    Notenskalierer(None, "Notenskalierer")
    app.MainLoop()

if __name__ == '__main__':
    main()

