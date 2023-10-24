import tkinter, customtkinter  # импортируем библиотеки tkinter и customtkinter
from tkinter import filedialog as fileD  # импортируем filedialog из tkinter и переименуем его в fileD
import os  # импортируем библиотеку os
from pygame import mixer  # импортируем mixer из pygame
from PIL import Image  # импортируем Image из PIL

flPause = False  # устанавливаем флаг паузы в False

mixer.init()  # инициализируем mixer

volume = tkinter.DoubleVar  # создаем переменную volume типа DoubleVar из tkinter

customtkinter.set_appearance_mode("System")  # устанавливаем режим внешнего вида окна (system, light, dark)
customtkinter.set_default_color_theme("green")  # устанавливаем цветовую тему окна (blue, dark-blue, green)

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), ".")  # создаем путь к папке с изображениями

app = customtkinter.CTk()  # создаем окно CTk, как и обычное окно Tk
app.geometry("505x350")  # устанавливаем размеры окна
app.title('MusicPlayer')  # устанавливаем заголовок окна

# создаем иконки для кнопок
PlayIcon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "play.png")))
StopIcon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "stop.png")))
LoadIcon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "load.png")))
ClearIcon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "clear.png")))
PauseIcon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "pause.png")))

# функция для изменения режима внешнего вида окна
def change_appearance_mode_event(new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)

# функция для начала воспроизведения музыки
def start():
    try:
        global selected
        selected = PlayList.get(tkinter.ACTIVE)
        mixer.music.load(selected)
        mixer.music.play()
    except:
        print('oops..')

# функция для паузы/возобновления воспроизведения музыки
def pause():
    global flPause
    flPause = not flPause
    if flPause:
        mixer.music.pause()
    else:
        mixer.music.unpause()

# функция для остановки воспроизведения музыки
def stop():
    mixer.music.stop()

# функция для загрузки музыкальных файлов
def Loading():
    global name
    name = fileD.askopenfilename()
    PlayList.insert(tkinter.END,name)

# функция для очистки плейлиста
def Clear():
    PlayList.delete(0,tkinter.END)

# функция для изменения громкости
def sliderChangeVolume(value):
    mixer.music.set_volume(value)
    print("Значение слайдера:", value)

# создаем кнопки для управления воспроизведением музыки
startB = customtkinter.CTkButton(master=app,text='Play',image=PlayIcon, command=start,width=24,height=24)
startB.place(x=5, y=245-35, anchor=tkinter.W)

pauseB = customtkinter.CTkButton(master=app,image=PauseIcon,text='Pause', command=pause,width=24,height=24)
pauseB.place(x=5, y=280-35, anchor=tkinter.W)

stopB = customtkinter.CTkButton(master=app,image=StopIcon,text='Stop', command=stop,width=24,height=24)
stopB.place(x=5, y=280, anchor=tkinter.W)

clearB = customtkinter.CTkButton(master=app,text='Clear playlist',image=ClearIcon ,command=Clear,width=24,
                                 height=24)
clearB.place(x=335,y=310,anchor=tkinter.CENTER)

LoadB = customtkinter.CTkButton(master=app,text='Add to playlist',image=LoadIcon,command=Loading,width=24,
                                height=24)
LoadB.place(x=210,y=310,anchor=tkinter.CENTER)

# создаем выпадающее меню для изменения режима внешнего вида окна
appearance_mode_OptionMenu = customtkinter.CTkOptionMenu(master=app, values=["Light", "Dark", "System"],
                                                          command=change_appearance_mode_event,width=8)
appearance_mode_OptionMenu.place(x=5,y=311,anchor=tkinter.W)

# создаем контейнер для отображения обложки альбома
Container = customtkinter.CTkFrame(master=app, width=140,height=140,corner_radius=10,fg_color='#404040')
Container.place(x=5,y=5)

# создаем слайдер для изменения громкости
volume = tkinter.DoubleVar()
VolumeSlider = customtkinter.CTkSlider(app, from_=0, to=1,height=400, orientation='vertical', command=sliderChangeVolume, variable=volume)
VolumeSlider.pack(side='right')

# создаем холст для отображения обложки альбома
Album = tkinter.Canvas(Container, width=130,height=130,highlightthickness=0,bg='#404040')
Album.place(x=5,y=5)

# создаем список для отображения плейлиста
PlayList = tkinter.Listbox(width=57,height=18,bg='#3b3b3b',fg='white')
PlayList.place(x=250-50-50,y=1)

app.mainloop()  # запускаем главный цикл приложения
