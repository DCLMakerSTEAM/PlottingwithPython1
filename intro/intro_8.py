print("Hello world!")

steps_walked = [8934, 14902, 3409, 25672, 12300, 2023, 6890]

for steps in steps_walked:
    print("Steps I walked:")
    print(steps)

    if steps < 5000:
        print("You should walk more.")
    if steps > 10000:
        print("Great job! You are staying fit!")
