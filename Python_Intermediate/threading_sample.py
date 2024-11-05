import threading

def function_1():
    for i in range(30):
        print(f"Line No .{i} Function-1")
        
def function_2():
    for j in range(30):
        print(f"Line No .{j} Function-2")
        
t1 = threading.Thread(target=function_1)
t2 = threading.Thread(target=function_2)

t1.start()
t2.start()

t2.join()
t1.join()

print("****** An interrupter -1  ******")
print("****** An interrupter -2  ******")


