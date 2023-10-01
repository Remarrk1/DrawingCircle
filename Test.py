import unittest
import tkinter as tk
from tkinter import Canvas
class TestCircleProgram(unittest.TestCase):

    def setUp(self):
        # Создание окна и холста
        self.root = tk.Tk()
        self.canvas = Canvas(self.root, width=400, height=400)
        self.canvas.pack()

    def tearDown(self):
        # Завершение теста, закрытие окна
        self.root.destroy()

    def test_initial_circle_position(self):
        # Проверка начального положения круга
        circle = self.canvas.create_oval(185, 185, 215, 215, fill="black")
        coords = self.canvas.coords(circle)
        self.assertEqual(coords, [185.0, 185.0, 215.0, 215.0])

    def test_move_left(self):
        # Проверка перемещения круга влево
        circle = self.canvas.create_oval(185, 185, 215, 215, fill="black")
        self.canvas.move(circle, -10, 0)
        coords = self.canvas.coords(circle)
        self.assertEqual(coords, [175.0, 185.0, 205.0, 215.0])

    def test_move_right(self):
        # Проверка перемещения круга вправо
        circle = self.canvas.create_oval(185, 185, 215, 215, fill="black")
        self.canvas.move(circle, 10, 0)
        coords = self.canvas.coords(circle)
        self.assertEqual(coords, [195.0, 185.0, 225.0, 215.0])


if __name__ == '__main__':
    unittest.main()


















