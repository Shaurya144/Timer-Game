import time

print("Hi! Get ready to play the estimateing game wait ten seconds and press enter")
time.sleep(0.5)
Pressed = input("Press enter(The time starts when you press enter) ")
starttime = time.time()
enter = input("press enter: ")
endTime = time.time()


timeTaken = endTime - starttime
print("That toook ", round(timeTaken, 2), " seconds")
