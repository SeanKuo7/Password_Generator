import sys
import time
import threading


class LoadingAnimation:
    loadingComplete = False

    def __init__(self) -> None:
        pass

    def animateLoading(self):
        animationChars = ["-", "\\", "|", "/"]
        idx = 0
        while not self.loadingComplete:
            sys.stdout.write("\r" + "Loading " + animationChars[idx])
            sys.stdout.flush()
            idx = (idx + 1) % len(animationChars)
            time.sleep(0.1)

    def start(self):
        self.loadingComplete = False

        # Start the loading animation in a separate thread
        loadingThread = threading.Thread(target=self.animateLoading)
        loadingThread.start()

    def stop(self):
        # Stop the loading animation by setting loadingComplete to True
        self.loadingComplete = True
        sys.stdout.write("\r" + "Loading complete\n")
        sys.stdout.flush()


def main():
    animation = LoadingAnimation()
    animation.start()

    # Simulate some time-consuming operation
    print("pseudo job that take 3 seconds")
    time.sleep(3)

    animation.stop()


if __name__ == "__main__":
    main()
