from random import randrange as rnd, choice
import tkinter as tk
import math
import time

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.c = 80
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME

        if self.r != 0:
            self.vy -= 2
            self.x += self.vx
            self.y -= self.vy
            if self.x + self.r >= 800 or self.x - self.r <= 0:
                self.vx *= -1
                if self.x + self.r >= 800:
                    self.x = 800 - self.r
                else:
                    self.x = 0 + self.r
            if self.y + self.r >= 550:
                self.vy *= -2 / 3
                self.vx *= 5 / 6
                self.y = 550 - self.r
            canv.coords(self.id, self.x - self.r,
                        self.y - self.r,
                        self.x + self.r,
                        self.y + self.r, )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x - obj.x) * (self.x - obj.x) + (self.y - obj.y) * (self.y - obj.y) < (obj.r + self.r) * (
                obj.r + self.r):

            return True
        else:
            return False

    def kill(self):
        canv.coords(self.id, -100, -100, -100, -100)
        self.vx = 0
        self.vy = 0
        self.r = 0


class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class target():
    def __init__(self):
        self.points = 0
        self.live = 1
        self.id = canv.create_oval(0, 0, 0, 0)
        # self.id_points = canv.create_text(30, 30, text=self.points, font='28')
        self.new_target()

        self.t = 0

    def new_target(self):
        """ Инициализация новой цели. """
        color = self.color = 'red'
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(10, 30)
        self.x0 = rnd(400, 600)
        self.y0 = rnd(100, 300)
        self.a = rnd(100, 170)
        self.b = rnd(100, 170)
        t = rnd(1, 4)
        if t == 1:
            self.k1 = 1
            self.k2 = 1
        if t == 2:
            self.k1 = -1
            self.k2 = 1
        if t == 3:
            self.k1 = 1
            self.k2 = -1
        if t == 4:
            self.k1 = -1
            self.k2 = -1
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.y0 = -1000
        self.x0 = -1000
        self.r = 0
        self.points += points
        #canv.itemconfig(self.id_points, text=self.points)

    def move1(self):
        m = 60
        self.x = self.x0 + self.k1 * self.a * math.sin(self.t)
        self.y = self.y0 + self.k2 * self.b * math.cos(self.t)
        if self.x + self.r >= 800 or self.x - self.r <= 0:
            self.a *= -1
            if self.x + self.r >= 800:
                self.x = 800 - self.r
            else:
                self.x = 0 + self.r
        if self.y + self.r >= 550 or self.y - self.r < 0:
            self.b *= -1
            if self.y + self.r >= 550:
                self.y0 = self.y
                self.y = 550 - self.r
            else:
                self.y0 = self.y
                self.y = 0 + self.r

        canv.coords(self.id, self.x - self.r,
                    self.y - self.r,
                    self.x + self.r,
                    self.y + self.r, )
        self.t += math.pi / m


t1 = target()
t2 = target()
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []
points = 0
id_points = canv.create_text(30, 30, text=points, font='28')


def new_game(event=''):
    global t1, t2, screen1, balls, bullet, points
    canv.itemconfig(screen1, text='')
    t1.new_target()
    t2.new_target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<Motion>', g1.targetting)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    z = 0.03
    t1.live = 1
    lop = 1
    t2.live = 1
    # canv.itemconfig(t2.id_points, text=' ')
    while lop:  # or balls:
        t1.move1()
        t2.move1()
        for b in balls:
            b.move()
            if b.c > 0:
                b.c -= 1
                if b.c == 0:
                    b.kill()
            # for t in targets:
            if b.hittest(t1) and t1.live == 1:
                t1.live = 0
                t1.hit()
                points += 1
                canv.itemconfig(id_points, text=points)
            if b.hittest(t2) and t2.live == 1:
                t2.live = 0
                t2.hit()
                points += 1
                canv.itemconfig(id_points, text=points)
                # canv.itemconfig(t1.id_points, text=t1.points+1)
            if t1.live == 0 and t2.live == 0:
                root.after(3000, new_game)
                t1.live = 2
                t2.live = 2
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
        #canv.itemconfig(t2.id_points, text=' ')
        canv.update()
        # canv.itemconfig(t1.id_points, text=bullet)
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()


new_game()
root.mainloop()
