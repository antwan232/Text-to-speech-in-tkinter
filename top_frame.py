from starter import *

# Top Frame
title_frame = tk.Frame(root, bg='white', width=900, height=100, padx=10, pady=10)
title_frame.grid(row=0, column=0, sticky='ew')
# title_frame.place(x=0,y=0)

# Title img
title_photo = Image.open('img/title_img.jpg').resize((70,70))
title_img = ImageTk.PhotoImage(title_photo)
logo_label = ttk.Label(title_frame, image=title_img)
logo_label.grid(row=0, column=0)
# logo_label.place(x=20,y=10)

# Title label
title_label = ttk.Label(
  title_frame, 
  text='TEXT TO SPEECH', 
  background='white',
  font='arial 20 bold', 
  foreground='black'
)
title_label.grid(row=0, column=1)
# title_label.place(x=100, y=30)