import numpy as np
import matplotlib.pyplot as plt

def plot_psk_modulation():
    bits = [1, 0, 1, 1, 0]
    carrier_freq = 10
    bit_duration = 0.5
    sampling_rate = 1000

    t_total = np.linspace(0, len(bits)*bit_duration, len(bits)*int(bit_duration*sampling_rate))

    carrier = np.sin(2*np.pi*carrier_freq*t_total)

    modulating_signal = np.repeat(bits, int(bit_duration * sampling_rate))

    psk_signal = []
    for bit in bits:
        phase = np.pi if bit == 1 else 0
        segment = np.sin(2*np.pi*carrier_freq*t_total[:int(bit_duration*sampling_rate)] + phase)
        psk_signal.extend(segment)

    fig, axs = plt.subplots(3, 1, figsize=(10, 8))

    axs[0].plot(t_total, carrier, label='Несущий сигнал', color='blue')
    axs[0].set_title('Фазовая манипуляция (PSK)', fontsize=14)
    axs[0].set_xlabel('Время')
    axs[0].set_ylabel('Амплитуда')

    axs[1].step(np.linspace(0, len(bits)*bit_duration, len(modulating_signal)), modulating_signal, where='post', label='Модулирующий сигнал', color='green')
    axs[1].set_xlabel('Время')
    axs[1].set_ylabel('Амплитуда')

    axs[2].plot(t_total, psk_signal, label='PSK-сигнал', color='red')
    axs[2].set_xlabel('Время')
    axs[2].set_ylabel('Амплитуда')

    plt.tight_layout()
    plt.show()