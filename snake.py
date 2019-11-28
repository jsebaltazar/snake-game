import curses
import random as r


'''
    A simple terminal-based snake game implemented using python
    Uses curses library to control text-mode terminal displays

'''


class Game:
    def __init__(self):
        scr = curses.initscr()
        curses.curs_set(False)
        height, width = scr.getmaxyx()
        window = curses.newwin(height, width, 0, 0)
        self.window = window
        self.window.keypad(True)
        self.height, self.width = height, width
        
    
    def set_speed(self, speed=100):
        self.window.timeout(speed)


    def create_snake(self):
        x = self.height/4
        y = self.width/2
        return [[y,x],[y,x-1],[y,x-2]]


    def create_food(self):
        food = [self.height/2, self.width/2]
        return food

    def spawn_char(self, h,w, c):
        print(int(h),int(w))
        self.window.addch(int(h),int(w),c)

g = Game()
g.set_speed(95)
snake = g.create_snake()
food = g.create_food()
g.spawn_char(food[0], food[1], "$")
print(g.height, g.width,g.window)
key = curses.KEY_RIGHT

while True:
    nxt_key = g.window.getch()
    
    if(nxt_key == -1):
        key = key
    else:
        key = nxt_key


    if( snake[0][0] in [0,g.height] or snake[0][1] in [0,g.width] or snake[0] in snake[1:]):
        curses.endwin()
        quit()

    head = [snake[0][0], snake[0][1]]

    if( key == curses.KEY_UP ):
        head[0] -= 1
   
    if( key == curses.KEY_RIGHT ):
        head[1] += 1

    if( key == curses.KEY_DOWN ):
        head[0] += 1
    
    if( key == curses.KEY_LEFT ):
        head[1] -= 1


    snake.insert(0, head)


    if(snake[0] == food):
        food = None
        while food is None:
            fd = [r.randint(1, g.height - 1), r.randint(1,g.width-1)]
            food = fd if fd not in snake else None
        g.spawn_char(food[0], food[1], "$")
    else:
        tail = snake.pop()
        g.spawn_char(int(tail[0]), int(tail[1]), '\ ')
    g.spawn_char(int(snake[0][0]), int(snake[0][1]), curses.ACS_BOARD)
