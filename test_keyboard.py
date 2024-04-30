import keyboard

TEST = 1

if TEST == 1:
    while True:
        # Wait for the next event.
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            print(event.name)  # to check key name

if TEST == 2:
    while True:
        # Wait for the next event.
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "ctrl":
                print("Clicked")
                break  # to check key name
