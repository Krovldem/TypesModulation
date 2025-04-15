import tkinter as tk
from .modulations.amplitude import plot_amplitude_modulation
from .modulations.frequency import plot_frequency_modulation
from .modulations.phase import plot_phase_modulation
from .modulations.ask import plot_ask_modulation
from .modulations.fsk import plot_fsk_modulation
from .modulations.psk import plot_psk_modulation

def create_gui():
    root = tk.Tk()
    root.title("Виды модуляции")
    root.geometry("300x250")

    # Надпись вверху окна
    tk.Label(root, text="Выберите вид модуляции:", font=("Helvetica", 14)).pack(pady=10)

    # Кнопки для выбора видов модуляции
    tk.Button(root, text="Амплитудная модуляция (AM)", command=plot_amplitude_modulation).pack(fill="both", expand=True)
    tk.Button(root, text="Частотная модуляция (FM)", command=plot_frequency_modulation).pack(fill="both", expand=True)
    tk.Button(root, text="Фазовая модуляция (PM)", command=plot_phase_modulation).pack(fill="both", expand=True)
    tk.Button(root, text="Дискретная амплитудная манипуляция (ASK)", command=plot_ask_modulation).pack(fill="both", expand=True)
    tk.Button(root, text="Дискретная частотная манипуляция (FSK)", command=plot_fsk_modulation).pack(fill="both", expand=True)
    tk.Button(root, text="Дискретная фазовая манипуляция (PSK)", command=plot_psk_modulation).pack(fill="both", expand=True)
    tk.Button(root, text="Показать все виды модуляции", command=lambda: all_modulations()).pack(fill="both", expand=True)
    tk.Button(root, text="Выход", command=root.destroy).pack(fill="both", expand=True)

    # Метод для одновременного вывода всех видов модуляции
    def all_modulations():
        print("Demonstration of different types of modulation:")
        plot_amplitude_modulation()
        plot_frequency_modulation()
        plot_phase_modulation()
        plot_ask_modulation()
        plot_fsk_modulation()
        plot_psk_modulation()

    root.mainloop()

def main():
    create_gui()

if __name__ == "__main__":
    main()