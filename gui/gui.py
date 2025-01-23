# Этот файл был сгенерирован с помощью Tkinter Designer от Партха Джадава
# https://github.com/ParthJadhav/Tkinter-Designer

# Импорт необходимых модулей из библиотек pathlib и tkinter
from pathlib import Path

# Явные импорты для удовлетворения требований Flake8, чтобы импортировать только нужные компоненты
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

# Установка пути вывода в директорию текущего файла
OUTPUT_PATH = Path(__file__).parent
# Определение пути к ресурсам, используемым в графическом интерфейсе
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Urban\Python\Kvantoriun\build\assets\frame0")

# Функция для преобразования относительных путей ресурсов в абсолютные пути
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Создание основного окна приложения
window = Tk()

# Установка размеров окна
window.geometry("1080x768")
# Настройка цвета фона окна
window.configure(bg="#B48F8F")

# Создание виджета канваса для рисования фигур и изображений
canvas = Canvas(
    window,
    bg="#B48F8F",  # Цвет фона канваса
    height=768,    # Высота канваса
    width=1080,    # Ширина канваса
    bd=0,          # Ширина границы
    highlightthickness=0,  # Толщина выделения для элементов в фокусе
    relief="ridge"  # Тип рельефа для границы канваса
)

# Размещение канваса в окне по координатам (0, 0)
canvas.place(x=0, y=0)

# Рисование прямоугольника на канвасе в качестве фона заголовка
canvas.create_rectangle(
    0.0,
    0.0,
    1080.0,
    134.25,
    fill="#18135E",  # Цвет заливки прямоугольника
    outline=""       # Без обводки у прямоугольника
)

# Загрузка изображения из ресурсов и создание объекта изображения на канвасе
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    540.0,
    450.25,
    image=image_image_1  # Размещение изображения в центре канваса
)

# Добавление текста на канвас, отображающего заголовок "Кванториум.22"
canvas.create_text(
    173.25,
    6.0,
    anchor="nw",  # Точка привязки для позиционирования текста
    text="Кванториум.22",
    fill="#FFFFFF",  # Цвет текста
    font=("Abel Regular", 96 * -1)  # Шрифт и размер (отрицательный размер для Tkinter)
)

# Загрузка еще одного изображения из ресурсов и создание объекта изображения на канвасе
image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    87.25,
    67.5,
    image=image_image_2  # Размещение изображения в верхнем левом углу канваса
)

# Загрузка третьего изображения из ресурсов и создание объекта изображения на канвасе
image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    539.0,
    407.25,
    image=image_image_3  # Размещение еще одного изображения на канвасе
)

# Загрузка изображения для кнопки и создание виджета Button на канвасе
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,            # Без границы вокруг кнопки
    highlightthickness=0,     # Без толщины выделения при фокусе
    command=lambda: print("button_1 clicked"),  # Команда, выполняемая при нажатии кнопки
    relief="flat"             # Плоский стиль кнопки без эффекта рельефа
)
# Размещение кнопки по заданным координатам с определенной шириной и высотой
button_1.place(
    x=306.75,
    y=634.5,
    width=465.75,
    height=78.75
)

# Запрет изменения размера окна пользователем
window.resizable(False, False)
# Запуск основного цикла событий Tkinter для отображения окна и обработки событий
window.mainloop()
