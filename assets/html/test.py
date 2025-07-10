from guizero import App, PushButton, Text

def get_file():
    file_name.value = app.select_file(folder="C:\\Users\\NGOC THAI\\Documents\\Zalo Received Files")

app = App()
PushButton(app, command=get_file, text="Get file")
file_name = Text(app)
app.display()