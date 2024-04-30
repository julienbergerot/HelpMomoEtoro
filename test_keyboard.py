import keyboard

TEST = 1

if TEST == 1:
    while True:
        # Wait for the next event.
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            print(event.name)  # to check key name

if TEST == 2:
    while True:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed("v"):  # if key 'q' is pressed
                print("You Pressed V Key!")
                break  # finishing the loop
        except:
            print("Error")
            break
