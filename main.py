from app import run_flask_server
import threading
import sys

#main 
if __name__ == "__main__":
     # Start the Flask server in a separate thread
    server_thread = threading.Thread(target=run_flask_server)
    server_thread.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        sys.exit(0)
