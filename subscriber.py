import zmq
import sys 

context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect("tcp://localhost:5555")

# If empty string is used, all messages are received (useful for testing)
subscription = "SILVER" 
socket.setsockopt_string(zmq.SUBSCRIBE, subscription)

print(f"SUBSCRIBER: Listening... (Filter: {subscription})")

while True:
    try:
        message = socket.recv_string()
        print(f"Received from network: {message}")
        print("-----------------")
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"Unexpected error: {e}")