import pgzrun
import random

FONT_OPTION = (255,255,255)

WIDTH = 800
HEIGHT = 600

CENTERX = 400
CENTERY = 300

CENTER = (400,300)
FINAL_LEVEL = 6
START_SPEED = 10
ITEMS = ["bag", "bottle", "chips", "battery"]

game_over = False
game_complete = False
current_level = 1
items = []
animations = []


def draw():
    global game_over, game_complete, current_level, items, animations
    screen.clear()
    screen.blit("backgroundimg", (0,0))

    if game_over:
        display_message("GAMEOVER, TRY AGAIN")
    elif game_complete:
        #argument missing for sub heading added
        display_message("YOU WON","Well done")
    else: 
        for i in items:
            i.draw()

def update():
    global game_over, game_complete, current_level, items, animations
    if len(items) == 0:
        items = make_items(current_level)

def make_items(extraitems):
    items_to_create = get_option_to_create(extraitems)
    new_items = create_item(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def get_option_to_create(numextraitems):
    items_to_create = ["paper"]
    for i in range(0, numextraitems):
        random_option = random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create

def create_item(items_to_create):
    new_items = []
    for i in items_to_create:
        items = Actor(i + "img")
        new_items.append(items)
    return new_items

       


def layout_items(items_to_layout):
    num_of_gaps = len(items_to_layout) + 1
    gap_size = WIDTH/num_of_gaps
    random.shuffle(items_to_layout)
    for i, item in enumerate(items_to_layout):
        new_x_position = (i + 1) * gap_size
        item.x = new_x_position



def animate_items(items_to_animate):
    global animations
    for i in items_to_animate:
        duration = START_SPEED - current_level
        #anchor is not a function
        i.anchor=("center", "bottom")
        ani = animate(i, duration = duration, on_finished = handle_game_over, y = HEIGHT)
        animations.append(ani)

def handle_game_over():
    global game_over
    game_over = True

def on_mouse_down(pos):
    global items, current_level

    for i in items:
        if i.collidepoint(pos):
            #image is not a function () removed
            if "paper" in i.image:
                handle_game_complete()
            else:
                handle_game_over()


def handle_game_complete():
    global items, current_level, animations, game_complete
    stop_animation(animations)
    if current_level == FINAL_LEVEL:
        game_complete = True
    else:
        current_level += 1
        items = []
        animations = []
def stop_animation(animations_to_stop):
    for i in animations_to_stop:
        #running is just a property () removed
        if i.running:
            i.stop()

def display_message(heading_text, subheading_text):
    screen.draw.text(heading_text, fontsize = 60, center = (400, 300), color = "white")
    screen.draw.text(subheading_text, fontsize = 30, center = (CENTERX, CENTERY - 30), color = "white" )

pgzrun.go()
