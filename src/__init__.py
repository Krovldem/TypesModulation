from .modulations.amplitude import plot_amplitude_modulation
from .modulations.frequency import plot_frequency_modulation
from .modulations.phase import plot_phase_modulation

def main():
    print("Demonstration of different types of modulation:")
    plot_amplitude_modulation()
    plot_frequency_modulation()
    plot_phase_modulation()

if __name__ == "__main__":
    main()