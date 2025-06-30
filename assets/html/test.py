from guizero import App, Picture, Box
from PIL import Image
app = App()
box = Box(app, layout = "grid")
image = Image.open("assets/images/nhà.png")  # Resize ảnh
image2 = Image.open("assets/images/vòng-quay.png")  # Resize ảnh
image3 = Image.open("assets/images/cối.png")  # Resize ảnh
image4 = Image.open("assets/images/suối.png")  # Resize ảnh
max_size = (300, 300) 
max_size1 = (400, 400) 
image.thumbnail(max_size)
image2.thumbnail(max_size)
image3.thumbnail(max_size)
image4.thumbnail(max_size1)
image.save("processed_image.jpg")
image2.save("processed_image2.jpg")
image3.save("processed_image3.jpg")
image4.save("processed_image4.jpg")
print("Kích thước gốc:", image.size)
box1 = Box(box, grid=[0,0], width=200, height=100)
picture1 = Picture(box1, image="processed_image.jpg")
box1.bg = "yellow"
box2 = Box(box, grid=[1,0], width=200, height=100)
picture2 = Picture(box2, image="processed_image2.jpg")
box2.bg = "red"
box3 = Box(box,  grid=[2,0,1,2], width=200, height=200)
picture3 = Picture(box3, image="processed_image3.jpg")
box3.bg = "green"
box4 = Box(box,   grid=[0,1,2,1], width=400, height=100)
picture4 = Picture(box4, image="processed_image4.jpg")
box3.bg = "black"

# picture1 = Picture(box, image="assets/images/nhà.png", grid=[0,0])
# picture2 = Picture(box, image="assets/images/vòng-quay.png", grid=[1,0])
# picture3 = Picture(box, image="assets/images/cối.png", grid=[2,0,1,2])
# picture4 = Picture(box, image="assets/images/suối.png", grid=[0,1,2,1])
app.display()