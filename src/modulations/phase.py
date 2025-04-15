import numpy as np
import matplotlib.pyplot as plt

def plot_phase_modulation():
    carrier_frequency = 25  # Гц
    modulation_frequency = 8 # Гц
    delta_phi = 1
    phi_0 = 0.0
    duration = 0.5
    sampling_rate = 2000

    samples = int(duration * sampling_rate)
    t = np.linspace(0, duration, samples, endpoint=False)

    modulating_signal = np.sin(2 * np.pi * modulation_frequency * t)

    phi = phi_0 + delta_phi * modulating_signal

    carrier_signal = np.sin(2 * np.pi * carrier_frequency * t + phi_0)

    pm_signal = np.sin(2 * np.pi * carrier_frequency * t + phi)

    plt.figure(figsize=(10, 8))
    plt.subplot(3, 1, 1)
    plt.plot(t, carrier_signal, label='Несущий сигнал')
    plt.title('Фазовая модуляция')
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(t, modulating_signal, label='Модулирующий сигнал (x(t))')
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(t, pm_signal, label='Фазомодулированный сигнал (PM)')
    plt.xlabel('Время, с')
    plt.ylabel('Амплитуда')
    plt.legend()

    plt.tight_layout()
    plt.show()
