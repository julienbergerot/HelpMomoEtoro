import keyboard


def wait_key():
    while True:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed("v"):  # if key 'q' is pressed
                # print("You Pressed V Key!")
                print("V")
                break  # finishing the loop
        except:
            print("error")
            break


wait_key()
