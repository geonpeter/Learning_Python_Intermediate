import threading
import time

my_event = threading.Event()

def blinkLight():
    while True:
        my_event.wait()
        #print("Waiting for the trigger")
        print("Light ON")
        time.sleep(3)
        print("Light OFF")
        time.sleep(3)
    
def movingRobot():
    while True:
        my_event.wait()
        print("Robot is moving ...")
        time.sleep(3)
    
light_thread = threading.Thread(target=blinkLight)
robot_thread = threading.Thread(target=movingRobot)

light_thread.start()
robot_thread.start()
        
my_event.set()