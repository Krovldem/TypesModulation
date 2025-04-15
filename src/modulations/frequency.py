import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
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

    fig, axs = plt.subplots(3, 1, figsize=(10, 8))

    line_carrier, = axs[0].plot(t, carrier_signal, label='Carrier Signal')
    line_modulating, = axs[1].plot(t, modulating_signal, label='Modulating Signal')
    line_fm, = axs[2].plot(t, fm_signal, label='FM Signal')

    axs[0].set_title('Frequency Modulation')
    for ax in axs:
        ax.grid(True)
        ax.legend()

    slider_color = 'lightgoldenrodyellow'

    ax_cf = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=slider_color)
    slider_cf = Slider(ax_cf, 'Carrier Freq.', valmin=10, valmax=50, valinit=carrier_frequency)

    ax_mf = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=slider_color)
    slider_mf = Slider(ax_mf, 'Modulation Freq.', valmin=1, valmax=15, valinit=modulation_frequency)

    ax_md = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=slider_color)
    slider_md = Slider(ax_md, 'Max Deviation', valmin=1, valmax=50, valinit=max_deviation)

    def update(val):
        nonlocal carrier_frequency, modulation_frequency, max_deviation
        carrier_frequency = slider_cf.val
        modulation_frequency = slider_mf.val
        max_deviation = slider_md.val

        t_new = np.linspace(0, duration, sampling_rate)
        carrier_signal_new = np.sin(2 * np.pi * carrier_frequency * t_new)
        modulating_signal_new = np.sin(2 * np.pi * modulation_frequency * t_new)
        accumulated_phase_new = np.cumsum(max_deviation * modulating_signal_new) / sampling_rate
        fm_signal_new = np.sin(2 * np.pi * carrier_frequency * t_new + accumulated_phase_new)

        line_carrier.set_data(t_new, carrier_signal_new)
        line_modulating.set_data(t_new, modulating_signal_new)
        line_fm.set_data(t_new, fm_signal_new)

        fig.canvas.draw_idle()

    slider_cf.on_changed(update)
    slider_mf.on_changed(update)
    slider_md.on_changed(update)

    plt.tight_layout(rect=[0, 0.25, 1, 1])
    plt.show()
