# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor is tested to run in recent versions of
# Chrome, Firefox, Safari, and Edge.

import simplegui

frame_width = int(input("what do you wnat the width to be: "))
frame_height = int(input("what do you wnat the width to be: "))

show_face1 = True
show_face2 = True
show_face3 = True
show_face4 = True
frame = None

def draw_face(canvas, cx, cy, size, expression):
    # Draw the circle (face)
    canvas.draw_circle((cx, cy), size, 1, "Yellow", "Yellow")  # Face color

    # Draw the eyes
    eye_size = size / 8
    eye_y_offset = size / 4
    left_eye_x = cx - size / 3
    right_eye_x = cx + size / 3

    # Draw eyes
    canvas.draw_circle((left_eye_x, cy - eye_y_offset), eye_size, 1, "Black", "Black")
    canvas.draw_circle((right_eye_x, cy - eye_y_offset), eye_size, 1, "Black", "Black")

    # Draw mouth based on expression
    mouth_width = size / 2
    mouth_height = size / 6
    if expression == "happy":
        canvas.draw_line((cx - mouth_width / 2, cy + mouth_height), 
                         (cx + mouth_width / 2, cy + mouth_height), 2, "Black")  # Happy mouth
    elif expression == "sad":
        canvas.draw_line((cx - mouth_width / 2, cy - mouth_height), 
                         (cx + mouth_width / 2, cy - mouth_height), 2, "Black")  # Sad mouth
    elif expression == "neutral":
        canvas.draw_line((cx - mouth_width / 2, cy + mouth_height / 2), 
                         (cx + mouth_width / 2, cy + mouth_height / 2), 2, "Black")  # Neutral mouth




def draw(canvas):
    quadrant_width = frame_width / 2
    quadrant_height = frame_height / 2
    
    # Only draw if show_faces is True
    if show_face1:
        # Top-left face (happy)
        draw_face(canvas, quadrant_width / 2, quadrant_height / 2, 50, "happy")
    
    if show_face2:
        # Top-right face (neutral)
        draw_face(canvas, 3 * quadrant_width / 2, quadrant_height / 2, 50, "neutral")
    
    if show_face3:
        # Bottom-left face (sad)
        draw_face(canvas, quadrant_width / 2, 3 * quadrant_height / 2, 50, "sad")
    
    if show_face4:
        # Bottom-right face (happy)
        draw_face(canvas, 3 * quadrant_width / 2, 3 * quadrant_height / 2, 50, "happy")

def toggle_face1():
    global show_face1
    show_face1 = not show_face1
def toggle_face2():
    global show_face1
    show_face2 = not show_face2
def toggle_face3():
    global show_face3
    show_face3 = not show_face3
def toggle_face4():
    global show_face4
    show_face4 = not show_face4
    
def create_frame():
    global frame
    frame = simplegui.create_frame("Shape Drawing Guide wih toggles", frame_width, frame_height)
    frame.set_draw_handler(draw)
    
    frame.add_button("Jannatul", toggle_face1, 150)
    #frame.add_button("Jerelyn", toggle_emoji1, 150)
    #frame.add_button("Vashti", toggle_triangle, 150)
    #frame.add_button("britany", toggle_triangle, 150)
    frame.start()
    
    
create_frame()
