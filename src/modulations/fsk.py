import numpy as np
import matplotlib.pyplot as plt

def plot_fsk_modulation():
    bits = [1, 0, 1, 1, 0]
    freq0 = 5
    freq1 = 15
    bit_duration = 0.5
    sampling_rate = 1000

    t_total = np.linspace(0, len(bits)*bit_duration, len(bits)*int(bit_duration*sampling_rate))

    modulating_signal = np.repeat(bits, int(bit_duration * sampling_rate))

    carrier_freq0 = np.sin(2*np.pi*freq0*t_total)
    carrier_freq1 = np.sin(2*np.pi*freq1*t_total)

    fsk_signal = []
    for bit in bits:
        freq = freq1 if bit == 1 else freq0
        segment = np.sin(2*np.pi*freq*t_total[:int(bit_duration*sampling_rate)])
        fsk_signal.extend(segment)

    fig, axs = plt.subplots(3, 1, figsize=(10, 8))

    axs[0].plot(t_total, carrier_freq0, label='Несущий сигнал (F0)', color='b')
    axs[0].plot(t_total, carrier_freq1, label='Несущий сигнал (F1)', color='g')
    axs[0].set_title('Несущие сигналы')
    axs[0].set_xlabel('Время')
    axs[0].set_ylabel('Амплитуда')
    axs[0].legend()

    axs[1].step(np.linspace(0, len(bits)*bit_duration, len(modulating_signal)), modulating_signal, where='post', label='Модулирующий сигнал', color='orange')
    axs[1].set_title('Модулирующий сигнал')
    axs[1].set_xlabel('Время')
    axs[1].set_ylabel('Амплитуда')
    axs[1].legend()

    axs[2].plot(t_total, fsk_signal, label='FSK-сигнал', color='purple')
    axs[2].set_title('Частотная манипуляция (FSK)')
    axs[2].set_xlabel('Время')
    axs[2].set_ylabel('Амплитуда')
    axs[2].legend()

    plt.tight_layout()
    plt.show()