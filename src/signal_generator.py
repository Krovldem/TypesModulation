import numpy as np

def generate_carrier_signal(frequency=100, duration=1, sampling_rate=1000):
    t = np.linspace(0, duration, int(sampling_rate * duration))
    return np.sin(2 * np.pi * frequency * t)

def generate_modulating_signal(amplitude=1, frequency=10, duration=1, sampling_rate=1000):
    t = np.linspace(0, duration, int(sampling_rate * duration))
    return amplitude * np.sin(2 * np.pi * frequency * t)