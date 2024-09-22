import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

# Define parameters
f1 = 10  # Frequency of first sine wave in Hz
f2 = 25  # Frequency of second sine wave in Hz
a = 2 * np.pi * f1  # Angular frequency of first sine wave
b = 2 * np.pi * f2  # Angular frequency of second sine wave

# Time parameters
T = 1  # Total time in seconds
sampling_rates = [100, 200, 400]  # Different sampling rates

# Prepare a plot
plt.figure(figsize=(12, 8))

# Loop through different sampling rates
for i, fs in enumerate(sampling_rates):
    t = np.linspace(0, T, int(T * fs), endpoint=False)  # Time vector
    F_t = np.sin(a * t) + np.sin(b * t)  # F(t) = sin(at) + sin(bt)

    # Perform FFT
    N = len(F_t)  # Number of sample points
    fft_result = fft(F_t)
    fft_freq = np.fft.fftfreq(N, 1 / fs)[: N // 2]  # Frequency bins (only positive)
    fft_magnitude = 2.0 / N * np.abs(fft_result[: N // 2])  # FFT magnitude

    # Plot FFT results
    plt.subplot(3, 1, i + 1)
    plt.plot(fft_freq, fft_magnitude)
    plt.title(f"Sampling Rate = {fs} Hz")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.grid()

# Display plots
plt.tight_layout()
plt.show()
