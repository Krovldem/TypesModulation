from matplotlib import pyplot as plt
from ..signal_generator import *

def plot_phase_modulation():
    carrier_frequency = 100
    modulation_frequency = 10
    sensitivity = 1
    carrier_signal = generate_carrier_signal(carrier_frequency)
    modulating_signal = generate_modulating_signal(frequency=modulation_frequency)
    pm_signal = np.sin(2 * np.pi * carrier_frequency * np.arange(len(modulating_signal))/len(modulating_signal) +
                      sensitivity * modulating_signal)
    time_axis = np.linspace(0, len(carrier_signal)/len(carrier_signal), len(carrier_signal))
    plt.figure(figsize=(10, 8))
    plt.subplot(3, 1, 1)
    plt.plot(time_axis, carrier_signal, label='Carrier Signal')
    plt.title('Phase Modulation')
    plt.legend()
    plt.subplot(3, 1, 2)
    plt.plot(time_axis, modulating_signal, label='Modulating Signal')
    plt.legend()
    plt.subplot(3, 1, 3)
    plt.plot(time_axis, pm_signal, label='PM Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()