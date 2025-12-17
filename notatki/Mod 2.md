#fizyka #elektromagnetyzm #siła_lorentza #notatka

# Moduł II: Siła Lorentza i Iloczyn Wektorowy

## 1. Wzór Wektorowy Siły Lorentza

> [!INFO] Definicja
> **Siła Lorentza ($F$)** to całkowita siła, jaką pole elektromagnetyczne (suma pola $E$ i $B$) wywiera na ładunek elektryczny ($q$) poruszający się z prędkością $\vec{v}$.

Wzór wektorowy:

$$\vec{F} = q(\vec{E} + \vec{v} \times \vec{B})$$

### Rozkład na składowe

| Cecha | A. Składowa Elektryczna (Siła Coulomba) | B. Składowa Magnetyczna |
| :--- | :--- | :--- |
| **Wzór** | $\vec{F}_{el} = q\vec{E}$ | $\vec{F}_{magn} = q(\vec{v} \times \vec{B})$ |
| **Warunek działania** | Działa na cząstkę **niezależnie** od jej prędkości. | Działa **tylko** na poruszający się ładunek. |
| **Kierunek** | Równoległy do wektora $\vec{E}$. | Prostopadły do $\vec{v}$ oraz do $\vec{B}$. |
| **Energia** | **Wykonuje pracę**. Zmienia energię kinetyczną (przyspiesza/spowalnia). | **Nie wykonuje pracy**. Zmienia tylko kierunek ruchu (działa jak siła dośrodkowa). |

> [!TIP] Analogia: Ster łodzi
> Składową magnetyczną można porównać do **manetki steru w łodzi**. Zmienia ona kierunek płynięcia łodzi, ale sama w sobie nie sprawia, że łódź płynie szybciej lub wolniej (nie zmienia energii kinetycznej).

---

## 2. Iloczyn Wektorowy i Wartość Siły

Kierunek i zwrot siły magnetycznej wynika z matematycznej definicji **iloczynu wektorowego** ($\vec{v} \times \vec{B}$).

### Wartość (Moduł) Siły
Wartość skalarna siły zależy od kąta $\theta$ między wektorem prędkości a wektorem indukcji:

$$F = |q|vB \sin\theta$$

* **Siła Maksymalna ($F_{max} = |q|vB$)**: Gdy $\theta = 90^\circ$ (prędkość prostopadła do pola).
* **Siła Zerowa ($F = 0$)**: Gdy $\theta = 0^\circ$ lub $180^\circ$ (prędkość równoległa do linii pola).

### Zapis wektorowy (składowe)
Jeżeli wektory podane są w układzie współrzędnych ($i, j, k$), siłę obliczamy z wyznacznika macierzy.
*Przykład*: Jeśli $\vec{B}$ jest wzdłuż osi $Z$, a prędkość ma składowe w $X, Y, Z$, to siłę generują tylko składowe prędkości $v_x$ i $v_y$ (bo są prostopadłe do $B_z$).



---

## 3. Reguła Prawej Dłoni (RHR-1)

Służy do szybkiego wyznaczania kierunku siły magnetycznej działającej na **ładunek dodatni**.

### Instrukcja RHR-1
1.  **Palce**: Wyprostuj palce prawej dłoni w kierunku wektora prędkości ($\vec{v}$).
2.  **Obrót**: Zegnij palce w kierunku wektora indukcji magnetycznej ($\vec{B}$) po mniejszym kącie.
3.  **Kciuk**: Odgięty kciuk wskaże kierunek siły magnetycznej ($\vec{F}$).



> [!WARNING] Uwaga na ładunki ujemne!
> Jeśli cząstka jest naładowana **ujemnie** (np. elektron), wyznaczony z RHR-1 kierunek należy **odwrócić o 180 stopni**.

### Rozróżnienie od RHR-2
* **RHR-1**: Służy do siły działającej na ładunek (trzy wektory: $v, B, F$).
* **RHR-2 (dla przewodnika)**: Kciuk wskazuje prąd, a zagięte palce wskazują wirowe pole magnetyczne wokół przewodu.