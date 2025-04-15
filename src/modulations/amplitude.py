from matplotlib import pyplot as plt
from ..signal_generator import *

def plot_amplitude_modulation():
    carrier_frequency = 100
    modulation_frequency = 10
    carrier_signal = generate_carrier_signal(carrier_frequency)
    modulating_signal = generate_modulating_signal(frequency=modulation_frequency)
    am_signal = (1 + modulating_signal) * carrier_signal
    time_axis = np.linspace(0, len(carrier_signal)/len(carrier_signal), len(carrier_signal))
    plt.figure(figsize=(10, 8))
    plt.subplot(3, 1, 1)
    plt.plot(time_axis, carrier_signal, label='Carrier Signal')
    plt.title('Amplitude Modulation')
    plt.legend()
    plt.subplot(3, 1, 2)
    plt.plot(time_axis, modulating_signal, label='Modulating Signal')
    plt.legend()
    plt.subplot(3, 1, 3)
    plt.plot(time_axis, am_signal, label='AM Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()