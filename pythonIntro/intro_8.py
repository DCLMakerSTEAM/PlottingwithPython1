steps_walked = [8934, 14902, 3409, 25672, 12300, 2023, 6890]

for steps in steps_walked:
    print("Steps I walked:")
    print(steps)

    # Python has a way to compare values and make decisions based
    # on the result of that comparison. Here we can suggest more
    # walking if the person did not have that many steps.
    if steps < 5000:
        print("You should walk more.")

    # Here we congratulate the person if they walked a lot.
    if steps > 10000:
        print("Great job! You are staying fit!")
