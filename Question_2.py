"""Yes, by default, Django signals run in the same thread as the caller. Django signals are executed synchronously, meaning the signal handler is executed in the same thread that sent the signal"""
import threading
from django.dispatch import Signal, receiver
import time

# Define a custom signal
my_signal = Signal()

# Signal handler
@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
    print(f"Signal handler running in thread: {threading.current_thread().name}")
    time.sleep(2)  # Simulate some work

# Function to send the signal
def send_signal():
    print(f"Signal sender running in thread: {threading.current_thread().name}")

    # Send the signal
    my_signal.send(sender=None)
    print("Signal sent")

if __name__ == "__main__":
    # Call the function that sends the signal
    send_signal()
