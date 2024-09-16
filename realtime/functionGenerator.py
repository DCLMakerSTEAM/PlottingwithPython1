import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters for the waveform
sampling_rate = 1000  # Hz
frequency = 5  # Hz
duration = 1  # seconds
num_samples = sampling_rate * duration

# Generate initial data
t = np.linspace(0, duration, num_samples, endpoint=False)
y = np.sin(2 * np.pi * frequency * t)

# Set up the figure and axis
fig, ax = plt.subplots()
line, = ax.plot(t, y)
ax.set_xlim(0, duration)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel('Time [s]')
ax.set_ylabel('Amplitude')
ax.set_title('Real-Time Waveform')

def update(frame):
    # Update the waveform data
    global t, y
    y = np.sin(2 * np.pi * frequency * (t + frame / sampling_rate))
    line.set_ydata(y)
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 2*sampling_rate, 1),
                              interval=1000 / sampling_rate, blit=True)

plt.show()
