# import the library
from appJar import gui

# handle button events
def press(button):
    if button == "Cancel":
        app.stop()
    else:
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        print("User:", usr, "Pass:", pwd)
        app.hideSubWindow("Login Window")
        app.show()

# create a GUI variable called app
app = gui("Main Window")

#subwindow login
app.startSubWindow("Login Window","400x200")
app.setBg("orange")
app.setFont(18)
app.addLabel("title", "XD")
app.setLabelBg("title", "blue")
app.setLabelFg("title", "orange")
app.addLabelEntry("Username")
app.addLabelSecretEntry("Password")
app.addButtons(["Submit", "Cancel"], press)
app.setFocus("Username")
app.stopSubWindow()

# start the GUI
app.go(startWindow="Login Window")
