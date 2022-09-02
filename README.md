# Quick Draw: Instructions  

How fast is your reaction time?

In this project, you will program a Quick Draw game which will measure reaction time, and print a different message based on how fast the reaction was.

[Here's a video of playing the game](https://www.loom.com/share/604d7be55d1f43aa97919cb3862c6191).

# Rules

Here's how the game should work.

1. First, it should welcome the user by printing out a message. 

2. Then, it should wait for the user to read the instructions and press Enter.

3. Next, it should wait a *random number of seconds* before showing:

```
DRAW!
```

4. When it prints out `DRAW!`, it should store the current time in a variable.

5. After the user presses Enter, the program should get the current time again.

6. The *elapsed time* (the time it took for the user to press Enter) can be found by subtracting the start time from the end time.

7. Print out the elapsed time, to tell the user how fast they were.

8. Show a final message based on the elapsed time:

- If the elapsed time was more than `0.3` seconds, the message should be:

```
Too slow! Try again next time.
```

- If the elapsed time was less than `0.1` seconds, the user probably cheated and pressed Enter before the `DRAW!` was shown. The message should be

```
You pressed Enter too soon, didn't you?
```

- If the elapsed time was less than `0.3` seconds but more than `0.1` seconds, then they are the fastest draw in the West! The message should be:

```
You're the fastest draw in the west, congratulations!
```

## Rubric

There aren't any test cases for this assignment. Instead, you'll have to check that it works for yourself.

Compare your program's output to the [video](https://www.loom.com/share/604d7be55d1f43aa97919cb3862c6191). Does your program work the same?

- [ ] The program runs without errors
- [ ] The program prints out instructions for the user
- [ ] The program times how long it takes for the user to press Enter
- [ ] The program shows a different message depending on how fast the user pressed Enter

If you checked off all these boxes, your program is probably right! If it doesn't meet these criteria, keep trying, and rememeber that you can ask for help.

## Hints and Tips

* If you use the `input()` function without any text, it will wait until the user presses Enter
* `time.time()` gives the current time.
* `time.sleep(seconds)` will sleep for the given number of seconds
* `random.randint(low, high)` will give a random number between the low and high inputs. `random.random()` will give a random number between `0` and `1`.
