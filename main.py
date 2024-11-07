from scripts.capture import ScreenCapture

def main():
    capture = ScreenCapture()
    while True:
        capture.get_screen()
        capture.show_screen()

if __name__ == "__main__":
    main()
