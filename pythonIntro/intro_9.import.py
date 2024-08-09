# We can make use of code that others have written. We do that
# by importing a 'module'. Here we are importing the 'statistics'
# module, so we can use its functions.
import statistics

steps_walked = [8934, 14902, 3409, 25672, 12300, 2023, 6890]

for steps in steps_walked:
    print("Steps I walked:")
    print(steps)

    # Python has a way to compare values and make decisions based
    # on the result of that comparison. Here we can suggest more
    # walking if the person did not have many steps.
    if steps < 5000:
        print("You should walk more.")

    # Here we congratulate the person if they walked a lot.
    if steps > 10000:
        print("Great job! You are staying fit!")

# Use the 'mean' function from the 'statistics' module to
# calculate the average. No need for us to do it! :)
average = statistics.mean(steps_walked)
print("Average steps walked:", average)
