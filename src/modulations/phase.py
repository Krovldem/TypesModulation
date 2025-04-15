import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def plot_phase_modulation():
    carrier_frequency = 25
    modulation_frequency = 8
    delta_phi = 1
    phi_0 = 0.0
    duration = 0.5
    sampling_rate = 2000

    def update(val):
        nonlocal carrier_frequency, modulation_frequency, delta_phi, phi_0
        carrier_frequency = slider_cf.val
        modulation_frequency = slider_mf.val
        delta_phi = slider_dp.val
        phi_0 = slider_p0.val

        t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
        modulating_signal = np.sin(2 * np.pi * modulation_frequency * t)
        phi = phi_0 + delta_phi * modulating_signal
        carrier_signal = np.sin(2 * np.pi * carrier_frequency * t + phi_0)
        pm_signal = np.sin(2 * np.pi * carrier_frequency * t + phi)

        line_cs.set_ydata(carrier_signal)
        line_ms.set_ydata(modulating_signal)
        line_pm.set_ydata(pm_signal)

        fig.canvas.draw_idle()

    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(10, 8))

    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    modulating_signal = np.sin(2 * np.pi * modulation_frequency * t)
    phi = phi_0 + delta_phi * modulating_signal
    carrier_signal = np.sin(2 * np.pi * carrier_frequency * t + phi_0)
    pm_signal = np.sin(2 * np.pi * carrier_frequency * t + phi)

    line_cs, = axes[0].plot(t, carrier_signal, label='Несущий сигнал')
    line_ms, = axes[1].plot(t, modulating_signal, label='Модулирующий сигнал')
    line_pm, = axes[2].plot(t, pm_signal, label='Фазомодулированный сигнал')

    axes[0].set_title('Фазовая модуляция (PM)', fontsize=14)
    for i in range(len(axes)):
        axes[i].legend(loc="upper right")
        axes[i].grid(True)

    slider_color = 'lightgoldenrodyellow'
    ax_cf = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=slider_color)
    ax_mf = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=slider_color)
    ax_dp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=slider_color)
    ax_p0 = plt.axes([0.25, 0.2, 0.65, 0.03], facecolor=slider_color)

    slider_cf = Slider(ax_cf, 'Несущая частота', valmin=10, valmax=50, valinit=carrier_frequency)
    slider_mf = Slider(ax_mf, 'Частота модуляции', valmin=1, valmax=15, valinit=modulation_frequency)
    slider_dp = Slider(ax_dp, 'Индекс фазовой модуляции', valmin=0, valmax=2, valinit=delta_phi)
    slider_p0 = Slider(ax_p0, 'Начальная фаза', valmin=-np.pi, valmax=np.pi, valinit=phi_0)

    slider_cf.on_changed(update)
    slider_mf.on_changed(update)
    slider_dp.on_changed(update)
    slider_p0.on_changed(update)

    plt.tight_layout(rect=[0, 0.25, 1, 1])
    plt.show()
