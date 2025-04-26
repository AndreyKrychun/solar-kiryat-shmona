import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Параметры установки
kWp = 10  # Пиковая мощность солнечной установки
efficiency = 0.85  # Эффективность установки

# Временной диапазон
date_range = pd.date_range(
    start="2024-07-01", end="2024-07-31 23:00", freq="h")

# Списки для хранения данных
irradiance = []
temperature = []
power_output = []

for timestamp in date_range:
    hour = timestamp.hour

    # Температура — днём выше, ночью ниже
    if 6 <= hour <= 18:
        temp = np.random.normal(30, 3)  # днём жарко
    else:
        temp = np.random.normal(22, 2)  # ночью прохладнее

    # Радиация — по синусоиде
    if 6 <= hour <= 18:
        rad = 1000 * np.sin(np.pi * (hour - 6) / 12) + np.random.normal(0, 50)
        rad = max(0, min(rad, 1000))  # ограничим значения
    else:
        rad = 0  # ночью солнца нет

    # P = kWp * (рад/1000) * efficiency
    power = kWp * (rad / 1000) * efficiency

    temperature.append(round(temp, 1))
    irradiance.append(round(rad, 1))
    power_output.append(round(power, 2))

data = pd.DataFrame({
    'timestamp': date_range,
    'temperature_C': temperature,
    'irradiance_W_m2': irradiance,
    'power_output_kW': power_output
})

data.to_csv('kiriyat_shmona_solar_july2024.csv', index=False)

plt.figure(figsize=(12, 5))
plt.plot(data['timestamp'], data['power_output_kW'], label='Power Output (kW)')
plt.xlabel("Дата")
plt.ylabel("Выработка энергии (кВт)")
plt.title("Синтетическая солнечная генерация — Кирьят Шмона, Июль 2024")
plt.legend()
plt.tight_layout()
plt.grid()
plt.show()
