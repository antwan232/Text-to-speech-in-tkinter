from starter import *

engine = pyttsx3.init()

def speak():
  text = text_area.get(1.0, END)
  gender = gender_combobox.get()
  speed = speed_compobox.get()
  voices = engine.getProperty('voices')

  def setVoice():
    if(gender == 'Male'):
      engine.setProperty('voice', voices[0].id)
      engine.say(text)
      engine.runAndWait()
    else:
      engine.setProperty('voice', voices[1].id)
      engine.say(text)
      engine.runAndWait()
  
  if text:
    if speed == 'Fast':
      engine.setProperty('rate', 250)
      setVoice()
    elif speed == 'Normal':
      engine.setProperty('rate', 150)
      setVoice()
    else:
      engine.setProperty('rate', 60)
      setVoice()


def downlaod():
  text = text_area.get(1.0, END)
  gender = gender_combobox.get()
  speed = speed_compobox.get()
  voices = engine.getProperty('voices')

  def setVoice():
    if(gender == 'Male'):
      engine.setProperty('voice', voices[0].id)
      path = filedialog.askdirectory()
      os.chdir(path)
      engine.save_to_file(text, 'text.mp3')
      engine.runAndWait()
    else:
      engine.setProperty('voice', voices[1].id)
      path = filedialog.askdirectory()
      os.chdir(path)
      engine.save_to_file(text, 'text.mp3')
      engine.runAndWait()
  
  if text:
    if speed == 'Fast':
      engine.setProperty('rate', 250)
      setVoice()
    elif speed == 'Normal':
      engine.setProperty('rate', 150)
      setVoice()
    else:
      engine.setProperty('rate', 60)
      setVoice()

text_area = tk.Text(
  root, 
  font='Robote 20', 
  bg='white', 
  relief='groove', 
  wrap='word'
)
text_area.place(x=10, y=150, width=500, height=250)

gender_label = ttk.Label(
  root, 
  text='VOICE',
  font='arial 15 bold',
  background='#305065',
  foreground='white'
)
gender_label.place(x=580,y=160)

speed_label = ttk.Label(
  root, 
  text='SPEED',
  font='arial 15 bold',
  background='#305065',
  foreground='white'
)
speed_label.place(x=760,y=160)

gender_combobox = ttk.Combobox(
  root, 
  values=['Male', 'Female'],
  font='arial 14',
  state='r',
  width=10
)
gender_combobox.set('Male')
gender_combobox.place(x=550, y=200)

speed_compobox = ttk.Combobox(
  root,
  values=['Fast', 'Normal', 'Slow'],
  font='arial 14',
  state='r',
  width=10
)
speed_compobox.set('Normal')
speed_compobox.place(x=730, y=200)

speak_photo = Image.open('img/speak.jpg').resize((50,50))
speak_img = ImageTk.PhotoImage(speak_photo)

speak_btn = tk.Button(
  root, 
  text=' SPEAK', 
  compound='left',
  image=speak_img,
  width=150,
  font='arial 14 bold',
  command=speak
)
speak_btn.place(x=550, y=280)

downlaod_photo = Image.open('img/./download.png').resize((60,50))
downlaod_img = ImageTk.PhotoImage(downlaod_photo)


downlaod_btn = tk.Button(
  root, 
  text=' SAVE', 
  compound='left',
  image=downlaod_img,
  width=150,
  font='arial 14 bold',
  command=downlaod
)
downlaod_btn.place(x=730, y=280)
