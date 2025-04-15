import numpy as np
import matplotlib.pyplot as plt

def plot_ask_modulation():
    bits = [1, 0, 1, 1, 0]
    carrier_freq = 10
    bit_duration = 0.5
    sampling_rate = 1000

    t_total = np.linspace(0, len(bits)*bit_duration, len(bits)*int(bit_duration*sampling_rate))

    carrier = np.sin(2*np.pi*carrier_freq*t_total)

    modulating_signal = np.repeat(bits, int(bit_duration * sampling_rate))

    ask_signal = []
    for bit in bits:
        segment = carrier[int(bit_duration*sampling_rate)*bits.index(bit):int((bit_duration*sampling_rate)*(bits.index(bit)+1))]
        if bit == 1:
            ask_signal.extend(segment)
        else:
            ask_signal.extend(np.zeros_like(segment))

    fig, axs = plt.subplots(3, 1, figsize=(10, 8))

    axs[0].plot(t_total, carrier, color='blue')
    axs[0].set_title('Несущий сигнал')
    axs[0].set_xlabel('Время')
    axs[0].set_ylabel('Амплитуда')

    axs[1].step(np.linspace(0, len(bits)*bit_duration, len(modulating_signal)), modulating_signal, color='green')
    axs[1].set_title('Модулирующий сигнал')
    axs[1].set_xlabel('Время')
    axs[1].set_ylabel('Амплитуда')

    axs[2].plot(t_total, ask_signal, color='red')
    axs[2].set_title('Амплитудная манипуляция (ASK)')
    axs[2].set_xlabel('Время')
    axs[2].set_ylabel('Амплитуда')

    plt.tight_layout()
    plt.show()