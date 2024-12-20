import PySimpleGUI as sg
from playsound import playsound
from random import choice
from time import time
import os

# game constants
FIELD_SIZE = 400
CELL_COUNT = 10
CELL_SIZE = FIELD_SIZE / CELL_COUNT
DIRECTIONS = {'left': (-1,0), 'right': (1,0), 'up': (0,1), 'down': (0,-1)}
INITIAL_SNAKE_BODY = [
    (2, 2),
    (1, 2),
    (0, 2)
]

# Sounds
sounds_dir = os.path.join(os.path.dirname(__file__), "snake_sounds")
gameover_sound = os.path.join(sounds_dir, "gameover.mp3")
win_sound = os.path.join(sounds_dir, "win.mp3")
eat_sound = os.path.join(sounds_dir, "eat.mp3")
bloop_sounds = [
    os.path.join(sounds_dir, "bloop1.mp3"),
    os.path.join(sounds_dir, "bloop2.mp3"),
    os.path.join(sounds_dir, "bloop3.mp3"),
]

def pos_to_pixels(pos):
    tl = pos[0] * CELL_SIZE, pos[1] * CELL_SIZE
    br = tl[0] + CELL_SIZE, tl[1] + CELL_SIZE
    return tl, br

def get_new_apple_pos(snake_body):
    all_positions = { (x // CELL_COUNT, x % CELL_COUNT) for x in range(CELL_COUNT**2) }
    possible_positions = list(all_positions.difference(snake_body))
    if len(possible_positions):
        return choice(possible_positions)
    else:
        return None
    
# Game variable initialization
game_running = False

def initialize_game_variables():
    global game_running, snake_body, direction, next_direction, apple_pos
    
    # Snake 
    snake_body = INITIAL_SNAKE_BODY.copy()
    direction = DIRECTIONS['right']
    next_direction = None

    # Apple
    apple_pos = get_new_apple_pos(snake_body)

# Window creation
def create_window():
    sg.theme('Green')
    layout = [
        [sg.Text("Welcome to snake!", font="Franklin 38", expand_x=True, justification="center")],
        [sg.Text("Eat to grow and grow to win, good luck!", font="Franklin 20", expand_x=True, justification="center")],
        [sg.Push(), sg.Button("Start", key="-START-", size=(12, 2), font="Franklin 14", pad=(10, 10)), sg.Button("Exit", key="-EXIT-", size=(12, 2), font="Franklin 14", pad=(10, 10)), sg.Push()],
    ]

    global game_running
    game_running = False

    return sg.Window("Snake", layout=layout)

def create_game_window():
    sg.theme('Green')
    field = sg.Graph(
        canvas_size=(FIELD_SIZE,FIELD_SIZE),
        graph_bottom_left=(0, 0),
        graph_top_right=(FIELD_SIZE, FIELD_SIZE),
        background_color='#000000'
    )
    layout = [[field]]

    initialize_game_variables()

    global game_running
    game_running = True

    return sg.Window("Snake", layout=layout, return_keyboard_events=True), field
    
    
def create_gameover_window(score, win):
    sg.theme('Green')
    layout = [
        [sg.Text(
            "Congratulations!" if win else "Gameover!", 
            font="Franklin 38", 
            expand_x=True, 
            justification="center"
        )],
        [sg.Text(
            f"Your final score is {score} out of {CELL_COUNT**2}", 
            font="Franklin 20", 
            expand_x=True, 
            justification="center"
        )],
        [sg.Push(), sg.Button("Retry", key="-RETRY-", size=(12, 2), font="Franklin 14", pad=(0, 10)), sg.Push()]
    ]

    global game_running
    game_running = False

    return sg.Window("Snake", layout=layout)


# Game loop
window = create_window()
start_time = None

while True:
    event, values = window.read(timeout=10)

    # if event != sg.TIMEOUT_EVENT:
    #     print(event)

    if event == sg.WIN_CLOSED:
        break

    if game_running:
        # This is needed to get keyboard events
        window.TKroot.focus_force()

        if (event == "Left:37" or event == "a") and direction != DIRECTIONS['right']:
            playsound(choice(bloop_sounds), False)
            next_direction = DIRECTIONS['left']
        if (event == "Up:38" or event == "w") and direction != DIRECTIONS['down']:
            playsound(choice(bloop_sounds), False)
            next_direction = DIRECTIONS['up']
        if (event == "Right:39" or event == "d") and direction != DIRECTIONS['left']:
            playsound(choice(bloop_sounds), False)
            next_direction = DIRECTIONS['right']
        if (event == "Down:40" or event == "s") and direction != DIRECTIONS['up']:
            playsound(choice(bloop_sounds), False)
            next_direction = DIRECTIONS['down']

        time_since_start = time() - start_time
        if time_since_start >= 0.4:
            start_time = time()

            # Game tick
            if next_direction:
                direction = next_direction
                next_direction = None

            new_head = (snake_body[0][0] + direction[0], snake_body[0][1] + direction[1])

            # Loss condition
            if (new_head[0] >= CELL_COUNT or new_head[1] >= CELL_COUNT or
                new_head[0] < 0 or new_head[1] < 0):
                playsound(gameover_sound, False)
                window.close()
                window = create_gameover_window(len(snake_body), False)
                continue
            
            if new_head in snake_body:
                playsound(gameover_sound, False)
                window.close()
                window = create_gameover_window(len(snake_body), False)
                continue

            # Update snake
            snake_body.insert(0, new_head)
            if new_head == apple_pos:
                playsound(eat_sound, False)
                apple_pos = get_new_apple_pos(snake_body)
            else:
                snake_body.pop()

            # Win conditions
            if not apple_pos:
                playsound(win_sound)
                window.close()
                window = create_gameover_window(len(snake_body), True)
                continue

            # Clear field
            field.draw_rectangle((0, 0), (FIELD_SIZE, FIELD_SIZE), 'black')

            # Draw apple
            tl, br = pos_to_pixels(apple_pos)
            field.draw_rectangle(tl, br, 'red')

            # Draw snake
            for index, pos in enumerate(snake_body):
                tl, br = pos_to_pixels(pos)
                color = 'yellow' if index == 0 else 'green'
                field.draw_rectangle(tl, br, color)
    else:
        if event == "-RETRY-":
            window.close()
            window, field = create_game_window()
            start_time = time()
        if event == "-START-":
            window.close()
            window, field = create_game_window()
            start_time = time()
        if event == "-EXIT-":
            break

window.close()