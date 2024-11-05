import threading
import time

no_of_pizzas = 0  # Shared resource for pizza count
ovens_semaphore = threading.Semaphore(2)  # Limit to 2 ovens
pizza_ready = threading.Condition()  # Condition for pizza serving readiness

menu = ['cipole', 'peperoni', 'wustel', 'margherita', 'genovese']  # Pizza types

def prepare_pizza(pizza_type):
    """Simulate pizza preparation"""
    print(f"Preparation of {pizza_type} is undergoing.")
    time.sleep(2)  # Simulate preparation time
    print(f"Preparation of {pizza_type} is done.")
    bake_pizza(pizza_type)  # After preparation, move to baking

def bake_pizza(pizza_type):
    """Simulate baking the pizza"""
    with ovens_semaphore:  # Limit number of pizzas baking simultaneously
        print(f"Placing {pizza_type} pizza inside the oven.")
        time.sleep(5)  # Simulate baking time
        print(f"{pizza_type} pizza is ready to serve.")
        serve_pizza(pizza_type)  # Notify that pizza is ready for serving

def serve_pizza(pizza_type):
    global no_of_pizzas
    """Serve the pizza once it's baked"""
    with pizza_ready:  # Lock to control serving process
        print(f"{pizza_type} pizza is ready to be served!")
        no_of_pizzas+=1
        pizza_ready.notify_all()  # Notify that the pizza is ready

threads = []
# Create threads for each pizza type
for item in menu:
    # Prepare and bake each pizza in a separate thread
    t = threading.Thread(target=prepare_pizza, args=(item,))
    threads.append(t)
    t.start()  # Start preparation for each pizza
    time.sleep(1)  # Slight delay for thread start-up to stagger processes

# Wait for all threads to complete
for t in threads:
    t.join()
print("---------------------------------------------------")

print(f"All pizzas {no_of_pizzas} have been prepared, baked, and served.")
