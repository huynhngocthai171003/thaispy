from guizero import App, TextBox, PushButton

def write_lines():
    lines = textbox.value.split("\n")
    with open("file.txt", "w", encoding="utf-8") as f:
        f.writelines(line.upper() + "\n" for line in lines)

app = App("Ghi nhiều dòng")
textbox = TextBox(app, multiline=True, width=40, height=5)
PushButton(app, text="Ghi danh sách dòng", command=write_lines)
app.display()