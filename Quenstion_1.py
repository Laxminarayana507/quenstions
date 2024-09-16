
"""By default, Django signals are executed synchronously. This means that when a signal is sent, the signal handler is executed immediately, blocking further code execution until the handler completes."""

import time
from django.dispatch import Signal, receiver

# Define a custom signal
my_signal = Signal()

# Signal handler
@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
    print("Signal handler started")
    time.sleep(3)  # Simulate a delay to check for blocking
    print("Signal handler finished")

# Function to send the signal
def send_signal():
    print("Sending signal")
    start_time = time.time()
    
    # Send the signal
    my_signal.send(sender=None)
    
    end_time = time.time()
    print(f"Signal processing finished in {end_time - start_time:.2f} seconds")

# Call the send_signal function
send_signal()
