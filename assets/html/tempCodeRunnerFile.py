from guizero import App, Text, PushButton, error

def read_lines():
    try:
        with open("data.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            for i in lines:
                i.strip()
            result.value = ' '.join(lines)
    except FileNotFoundError:
        error("Lỗi", "Không tìm thấy file")

app = App("Đọc tất cả dòng")
PushButton(app, text="Đọc file", command=read_lines)
result = Text(app, text="")
app.display()