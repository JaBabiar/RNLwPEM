#fizyka #elektromagnetyzm #ruch_ładunku #cyklotron #notatka

# Moduł III: Ruch Ładunków w Polu Magnetycznym ($B$)

## Wstęp: Zasada Zerowej Pracy
Kluczowa zasada wynikająca z Modułu II:
> [!IMPORTANT] Siła magnetyczna nie wykonuje pracy
> Ponieważ siła magnetyczna jest zawsze prostopadła do prędkości ($\vec{F}_{magn} \perp \vec{v}$):
> 1.  Praca siły wynosi **zero** ($W = 0$).
> 2.  Energia kinetyczna cząstki jest **stała** ($E_k = const$).
> 3.  Wartość prędkości ($v$) jest **stała** (zmienia się tylko kierunek wektora prędkości).

---

## 1. Ruch po Okręgu ($\vec{v} \perp \vec{B}$)
Występuje, gdy cząstka wpada w pole magnetyczne idealnie prostopadle do linii pola ($\theta = 90^\circ$).

### A. Mechanizm
Siła magnetyczna pełni rolę **siły dośrodkowej** ($F_d$). Zakrzywia ona tor ruchu, zamykając go w okrąg.
Wartość siły (dla $\sin 90^\circ = 1$):
$$F = |q|vB$$

### B. Promień orbity ($r$)
Przyrównujemy siłę magnetyczną do siły dośrodkowej:
$$|q|vB = \frac{mv^2}{r}$$

Po przekształceniu otrzymujemy wzór na **promień cyklotronowy**:

$$r = \frac{mv}{|q|B}$$

> [!NOTE] Interpretacja
> Promień jest wprost proporcjonalny do pędu cząstki ($p=mv$). Im szybsza lub cięższa cząstka, tym większy łuk zatacza. Im silniejsze pole ($B$), tym ciaśniejszy łuk.

### C. Okres ($T$) i Częstość ($\omega$)
Czas pełnego obiegu (okres) to obwód okręgu podzielony przez prędkość:

$$T = \frac{2\pi r}{v} = \frac{2\pi m}{|q|B}$$

**Częstość kołowa (cyklotronowa):**
$$\omega = \frac{|q|B}{m}$$

> [!TIP] Kluczowa właściwość (Zasada Cyklotronu)
> Zauważ, że we wzorze na okres $T$ **nie ma prędkości $v$ ani promienia $r$**.
> Oznacza to, że czas jednego okrążenia jest **stały** dla danej cząstki w danym polu, niezależnie od tego, jak szybko się ona porusza. Jest to podstawa działania akceleratorów cząstek (cyklotronów).



---

## 2. Ruch Śrubowy / Helisa ($\vec{v}$ pod kątem $\theta$)
Gdy prędkość $\vec{v}$ tworzy z polem $\vec{B}$ kąt inny niż $0^\circ$ lub $90^\circ$, ruch jest złożeniem dwóch składowych. Rozkładamy wektor prędkości na dwie części:

| Składowa prędkości | Kierunek względem $B$ | Rodzaj ruchu | Siła Lorentza |
| :--- | :--- | :--- | :--- |
| **Równoległa ($v_{\parallel}$)** | $v_{\parallel} = v \cos \theta$ | **Jednostajny prostoliniowy** | $0$ (brak siły) |
| **Prostopadła ($v_{\perp}$)** | $v_{\perp} = v \sin \theta$ | **Jednostajny po okręgu** | $F = |q|v_{\perp}B$ |

**Rezultat:** Cząstka krąży po okręgu, który jednostajnie przesuwa się wzdłuż linii pola, tworząc **linii śrubową (helisę)**.



[Image of helical motion of charged particle in magnetic field]


### Parametry helisy

1.  **Promień helisy ($r$):**
    Zależy tylko od składowej prostopadłej prędkości:
    $$r = \frac{m v_{\perp}}{|q|B} = \frac{m v \sin \theta}{|q|B}$$

2.  **Skok helisy ($p$):**
    Odległość między sąsiadującymi zwojami. To droga przebyta wzdłuż pola w czasie jednego okresu ($T$):
    $$p = v_{\parallel} \cdot T$$

---

## 3. Zastosowanie w naturze: Pułapkowanie magnetyczne

Siła Lorentza sprawia, że naładowane cząstki mają tendencję do "nawijania się" na linie pola magnetycznego.

* **Zorza polarna**: Cząstki wiatru słonecznego poruszają się ruchem śrubowym wzdłuż linii pola magnetycznego Ziemi, uderzając w atmosferę w okolicach biegunów.
* **Pasy Van Allena**: Obszary wokół Ziemi, gdzie cząstki są "uwięzione" w magnetycznej pułapce, krążąc po helisach tam i z powrotem między biegunami.