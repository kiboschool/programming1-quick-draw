import random, time

# TODO 1: Print a welcome message. Include "press Enter to start".
print("Are you the fastest draw in the west?")
print("Find out!")
print("When the screen says DRAW, press enter.")
print()
print("Press Enter to start")

# TODO 2: use input() to wait for the user to press Enter
input()
print("Wait for it...")

# TODO 3: wait a random number of seconds
wait = random.randint(1,3) + random.random()
time.sleep(wait)

# TODO 4: Time how long it takes for the user to press Enter
# Get the current time with time.time()
start = time.time()
print("DRAW!")
input()
# Use time.time() again to get the time after the user pressed Enter with 
stop = time.time()
# Subtract the stop time from the start time to get the elapsed time
elapsed = stop - start

# Print how long it took
print("You took " + str(elapsed) + " seconds")

# Print different results, based on how long it took
if elapsed < 0.1:
  print("You pressed Enter too soon, didn't you?")
elif elapsed < 0.3:
  print("You're the fastest draw in the west, congratulations!")
else:
  print("Too slow! Try again next time.")