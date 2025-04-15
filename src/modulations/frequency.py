import numpy as np
import matplotlib.pyplot as plt
from ..signal_generator import *


def plot_frequency_modulation():
    carrier_frequency = 20
    modulation_frequency = 5
    max_deviation = 20
    duration = 0.5
    sampling_rate = 1000

    t = np.linspace(0, duration, sampling_rate)

    carrier_signal = np.sin(2 * np.pi * carrier_frequency * t)

    modulating_signal = np.sin(2 * np.pi * modulation_frequency * t)

    accumulated_phase = np.cumsum(max_deviation * modulating_signal) / sampling_rate

    fm_signal = np.sin(2 * np.pi * carrier_frequency * t + accumulated_phase)

    time_axis = np.linspace(0, duration, len(carrier_signal))

    plt.figure(figsize=(10, 8))
    plt.subplot(3, 1, 1)
    plt.plot(time_axis, carrier_signal, label='Carrier Signal')
    plt.title('Frequency Modulation')
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(time_axis, modulating_signal, label='Modulating Signal')
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(time_axis, fm_signal, label='FM Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()