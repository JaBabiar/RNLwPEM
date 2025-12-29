import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# --- KONFIGURACJA PÓL ---
def pole_elektryczne(t, r):
    """Zwraca wektor pola E [Ex, Ey, Ez] w danej pozycji r i czasie t."""
    # Przykład: stałe pole elektryczne skierowane w górę osi Z
    # E = 0,1 * k
    return np.array([1.0, 0.0, 0.1])


def pole_magnetyczne(t, r):
    """Zwraca wektor pola B [Bx, By, Bz] w danej pozycji r i czasie t."""
    # Przykład: stałe pole magnetyczne wzdłuż osi Z
    # B = 1.0 * k
    return np.array([0.0, 1.0, 1.0])


# --- FIZYKA (SIŁA LORENTZA) ---
def rownanie_ruchu(t, y, q, m):
    """
    Funkcja definiująca układ równań różniczkowych.
    y to wektor stanu: [x, y, z, vx, vy, vz]
    """
    # Rozpakowanie pozycji (r) i prędkości (v)
    r = y[:3]
    v = y[3:]

    # Pobranie wartości pól w danym punkcie
    E = pole_elektryczne(t, r)
    B = pole_magnetyczne(t, r)

    # Obliczenie siły Lorentza: F = q(E + v x B)
    # np.cross to iloczyn wektorowy
    F = q * (E + np.cross(v, B))

    # Przyspieszenie a = F / m
    a = F / m

    # Zwracamy pochodne: [dr/dt, dv/dt] czyli [v, a]
    dydt = np.concatenate((v, a))
    return dydt


# --- PARAMETRY SYMULACJI ---
# Jednostki umowne (dla elektronu w realnych jednostkach liczby byłyby bardzo małe)
q = 1.0  # Ładunek
m = 1.0  # Masa
t_span = (0, 30)  # Czas symulacji od 0 do 20 sekund
t_eval = np.linspace(t_span[0], t_span[1], 1000)  # Punkty czasowe do zapisu

# Warunki początkowe: [x, y, z, vx, vy, vz]
# Cząstka startuje w (0,0,0) z prędkością w kierunku X
y0 = np.array([0.0, 0.0, 0.0, 1.0, 0.5, 0.0])

# --- ROZWIĄZANIE RÓWNANIA ---
sol = solve_ivp(
    fun=lambda t, y: rownanie_ruchu(t, y, q, m),
    t_span=t_span,
    y0=y0,
    t_eval=t_eval,
    method='RK45'  # Metoda Runge-Kutta rzędu 4/5 (standardowa)
)

# --- WIZUALIZACJA ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Wyciągnięcie współrzędnych z rozwiązania
x, y, z = sol.y[0], sol.y[1], sol.y[2]

ax.plot(x, y, z, label='Tor ruchu cząsteczki', color='b')
ax.scatter(x[0], y[0], z[0], color='g', label='Start')  # Punkt startowy
ax.scatter(x[-1], y[-1], z[-1], color='r', label='Koniec')  # Punkt końcowy

# Opisy osi
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(f'Ruch ładunku w polach E i B\nq={q}, m={m}')
ax.legend()

plt.show()