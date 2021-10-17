
import tkinter
import pyperclip




def getPercent():
    global pPercent
    global ePercent
    global aPercent
    global maxPkt
    pPercent = float(prP.get())
    ePercent = float(prE.get())
    aPercent = float(prA.get())
    maxPkt = float(maxP.get())

    wait = tkinter.Tk()
    def cont():
        wait.destroy()
    wait.title("Notenskalierer")
    tkinter.Label(wait, text="Bitte warten...").grid(row=0)
    percent.destroy()
    seeBttn = tkinter.Button(wait, text="Notenskala Anzeigen",command=cont )
    seeBttn.grid(row=1)
    wait.mainloop()
    print(f"A:{aPercent} E:{ePercent} P:{pPercent}")

percent = tkinter.Tk()
percent.title("Notenskalierer")
tkinter.Label(percent, text="Prozent im P-zug für eine 4").grid(row=0)
tkinter.Label(percent, text="Prozent im E-zug für eine 4").grid(row=1)
tkinter.Label(percent, text="Prozent im A-zug für eine 4").grid(row=2)
tkinter.Label(percent, text="Maximale Punktzahl").grid(row=3)

prP = tkinter.Entry(percent)
prE = tkinter.Entry(percent)
prA = tkinter.Entry(percent)
maxP = tkinter.Entry(percent)

prP.grid(row=0, column=1)
prE.grid(row=1, column=1)
prA.grid(row=2, column=1)
maxP.grid(row=3, column=1)


startBttn = tkinter.Button(text="Berechnen", command=getPercent)
startBttn.grid(row=4, column=0)

percent.mainloop()

gPktP = (maxPkt/100)*pPercent
gPktE = (maxPkt/100)*ePercent
gPktA = (maxPkt/100)*aPercent

UpStep = gPktP/7
UeStep = gPktE/7
UaStep = gPktA/7

GpStep = (maxPkt-gPktP)/4
GeStep = (maxPkt-gPktE)/4
GaStep = (maxPkt-gPktA)/4

markStr = ""
tmpMark = 1
tmpPkt = 0
tmpPktW = 0
markStr += "P-zug:\n"
for i in range(0,7):
    markStr += f"{tmpMark}: {tmpPktW}/{maxPkt}\n"
    tmpMark += .5
    tmpPkt += UpStep
    tmpPktW = round(tmpPkt, 1)
for j in range(0,4):
    markStr += f"{tmpMark}: {tmpPktW}/{maxPkt}\n"
    tmpMark += .5
    tmpPkt += GpStep
    tmpPktW = round(tmpPkt, 1)

tmpMark = 1
tmpPkt = 0
tmpPktW = 0
markStr += "\nE-zug:\n"

for i in range(0,7):
    markStr += f"{tmpMark}: {tmpPktW}/{maxPkt}\n"
    tmpMark += .5
    tmpPkt += UeStep
    tmpPktW = round(tmpPkt, 1)
for j in range(0,4):
    markStr += f"{tmpMark}: {tmpPktW}/{maxPkt}\n"
    tmpMark += .5
    tmpPkt += GeStep
    tmpPktW = round(tmpPkt, 1)

tmpMark = 1
tmpPkt = 0
tmpPktW = 0
markStr += "\A-zug:\n"

for i in range(0,7):
    markStr += f"{tmpMark}: {tmpPktW}/{maxPkt}\n"
    tmpMark += .5
    tmpPkt += UaStep
    tmpPktW = round(tmpPkt, 1)
for j in range(0,4):
    markStr += f"{tmpMark}: {tmpPktW}/{maxPkt}\n"
    tmpMark += .5
    tmpPkt += GaStep
    tmpPktW = round(tmpPkt, 1)

print(markStr)

def copy():
    pyperclip.copy(markStr)
    tkinter.Label(notenskala, text="Kopiert!").grid(row=3)
    notenskala.mainloop()

notenskala = tkinter.Tk()
notenskala.title("Notenskalierer")
tkinter.Label(notenskala, text="Ihnre Notenskalen:").grid(row = 0)
skalen = tkinter.Label(notenskala, text=markStr).grid(row=1)
copyBttn = tkinter.Button(notenskala, text="Kopieren", command=copy)
copyBttn.grid(row= 2)
notenskala.mainloop()


