steps_walked = [8934, 14902, 3409, 25672, 12300, 2023, 6890]

# Python can loop through each of the values in the list.
# Here we start at the value in the zeroth position and
# loop through each subsequent value, stopping BEFORE we
# get to the 7th value.
for day in range(0, 7):
    print("Steps I walked:")
    print(steps_walked[day])

# This seems fragile. What if we add a value to the list?
# We'll need to remember to change the 7 to an 8. Or if we
# remove a value from the list. We'll need to remember to
# change the 7 to a 6.

# Surely there must be an easier way to loop...