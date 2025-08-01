from guizero import App, Slider, PushButton, Picture, Text

def resize_image():
    size = size_slider.value
    image.width = size
    image.height = size
    size_label.value = f"Kích thước: {size} x {size}"

def reset_size():
    size_slider.value = 150
    resize_image()

app = App("Điều chỉnh ảnh", width=300, height=350)

Text(app, "Điều chỉnh kích thước ảnh:")
size_slider = Slider(app, start=50, end=300, command=resize_image)
size_slider.value = 150

image = Picture(app, image="hacker.png", width=150, height=150)

size_label = Text(app, text="Kích thước: 150 x 150")
PushButton(app, text="Đặt lại", command=reset_size)

app.display()



