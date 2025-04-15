import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from ..signal_generator import *


def plot_amplitude_modulation():
    fig, axs = plt.subplots(nrows=3, ncols=1, figsize=(10, 8))
    carrier_frequency = 100
    modulation_frequency = 10
    depth_modulation = 0.5
    duration = 0.5
    sampling_rate = 1000

    def update(val):
        nonlocal carrier_frequency, modulation_frequency, depth_modulation

        carrier_frequency = slider_cf.val
        modulation_frequency = slider_mf.val
        depth_modulation = slider_dm.val

        t = np.linspace(0, duration, int(sampling_rate * duration))
        carrier_signal = generate_carrier_signal(carrier_frequency, duration, sampling_rate)
        modulating_signal = generate_modulating_signal(1, modulation_frequency, duration, sampling_rate)
        am_signal = (1 + depth_modulation * modulating_signal) * carrier_signal

        line_cs.set_ydata(carrier_signal)
        line_ms.set_ydata(modulating_signal)
        line_as.set_ydata(am_signal)

        fig.canvas.draw_idle()

    axcf = plt.axes([0.25, 0.05, 0.65, 0.03])
    slider_cf = Slider(axcf, 'Несущая частота', valmin=50, valmax=200, valinit=carrier_frequency)

    axmf = plt.axes([0.25, 0.1, 0.65, 0.03])
    slider_mf = Slider(axmf, 'Частота модуляции', valmin=1, valmax=20, valinit=modulation_frequency)

    axdm = plt.axes([0.25, 0.15, 0.65, 0.03])
    slider_dm = Slider(axdm, 'Коэффициент модуляции', valmin=0, valmax=1, valinit=depth_modulation)

    axs[0].set_title('Амплитудная модуляция (AM)', fontsize=14)
    axs[0].set_xlabel('Время')
    axs[0].set_ylabel('Амплитуда')
    axs[1].set_xlabel('Время')
    axs[1].set_ylabel('Амплитуда')
    axs[2].set_xlabel('Время')
    axs[2].set_ylabel('Амплитуда')

    t = np.linspace(0, duration, int(sampling_rate * duration))
    carrier_signal = generate_carrier_signal(carrier_frequency, duration, sampling_rate)
    modulating_signal = generate_modulating_signal(1, modulation_frequency, duration, sampling_rate)
    am_signal = (1 + depth_modulation * modulating_signal) * carrier_signal

    line_cs, = axs[0].plot(t, carrier_signal, label='Несущий сигнал')
    line_ms, = axs[1].plot(t, modulating_signal, label='Модулирующий сигнал')
    line_as, = axs[2].plot(t, am_signal, label='AM-сигнал')

    slider_cf.on_changed(update)
    slider_mf.on_changed(update)
    slider_dm.on_changed(update)

    plt.tight_layout(rect=[0, 0.2, 1, 1])
    plt.show()

