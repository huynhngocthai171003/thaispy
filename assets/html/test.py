from guizero import App, TextBox

def xu_ly(event_data=None):
    print("Sự kiện xảy ra tại:", event_data.widget)

app = App()
widget = TextBox(app)
widget.when_double_clicked = xu_ly
app.display()
    