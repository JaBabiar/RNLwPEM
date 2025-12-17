#fizyka #elektromagnetyzm #zastosowania #spektrometr #cyklotron #efekt_halla #notatka

# Moduł IV: Ruch Ładunków w Skrzyżowanych Polach i Zastosowania

Ten moduł koncentruje się na praktycznym wykorzystaniu siły Lorentza do manipulowania cząstkami (przyspieszania, selekcjonowania) oraz do pomiarów.

---

## 1. Rozdzielacz Prędkości (Selektor Prędkości)

Urządzenie filtrujące cząstki tak, aby przepuścić tylko te o konkretnej prędkości.

### Zasada: Skrzyżowane Pola
Pola elektryczne ($\vec{E}$) i magnetyczne ($\vec{B}$) są ustawione **prostopadle do siebie** oraz **prostopadle do wektora prędkości** cząstki.

Na cząstkę działają dwie przeciwne siły:
1.  **Siła elektryczna**: $\vec{F}_{el} = q\vec{E}$
2.  **Siła magnetyczna**: $\vec{F}_{magn} = q(\vec{v} \times \vec{B})$

Aby cząstka przeleciała prosto (bez ugięcia), siły muszą się równoważyć ($\sum F = 0$):
$$|q|E = |q|vB$$

> [!KEY] Warunek Selekcji
> Po przekształceniu otrzymujemy prędkość "uprzywilejowaną":
> $$v = \frac{E}{B}$$
> Każda cząstka o innej prędkości zostanie odchylona w stronę silniejszej siły.



---

## 2. Spektrometr Masowy
Urządzenie do "ważenia" atomów – rozdziela jony na podstawie stosunku ładunku do masy ($q/m$).

### Etapy działania
1.  **Selekcja**: Jony przechodzą przez *Rozdzielacz Prędkości* (patrz pkt 1), więc wszystkie wpadające do analizatora mają znaną prędkość $v = E/B$.
2.  **Analiza Masy**: Jony wpadają w obszar jednorodnego pola magnetycznego ($B_0$). Zgodnie z Modułem III, zaczynają poruszać się po okręgu.
3.  **Pomiar**: Promień okręgu ($R$) zależy od masy.

$$R = \frac{mv}{qB_0}$$

Łącząc wzory z obu etapów, wyznaczamy stosunek ładunku do masy:

$$\frac{q}{m} = \frac{E}{B B_0 R}$$

> [!INFO] Zastosowanie
> Identyfikacja substancji, datowanie izotopowe, wykrywanie nieszczelności.



---

## 3. Cyklotron
Akcelerator cząstek, przyspieszający je do wysokich energii (rzędu MeV) po spiralnym torze.

### Budowa i Działanie
* **Dwie połówki (duanty "D")**: Znajdują się w stałym polu magnetycznym $\vec{B}$, które zakrzywia tor cząstki (ruch po okręgu).
* **Szczelina**: Między połówkami występuje zmienne pole elektryczne $\vec{E}$, które przyspiesza cząstkę przy każdym przejściu.

### Klucz do sukcesu: Synchronizacja
Okres obiegu cząstki w polu magnetycznym **nie zależy od jej prędkości ani promienia** (wniosek z Modułu III):
$$T = \frac{2\pi m}{qB} = const$$
Dzięki temu generator napięcia może pracować ze stałą częstotliwością rezonansową, idealnie trafiając w moment przelotu cząstki przez szczelinę.

### Maksymalna Energia
Ograniczona promieniem urządzenia ($R$):
$$E_{k\_max} = \frac{q^2 B^2 R^2}{2 m}$$



[Image of cyclotron particle accelerator diagram]


---

## 4. Efekt Halla
Zjawisko w przewodniku z prądem umieszczonym w polu magnetycznym.

### Mechanizm
1.  Prąd płynie w przewodniku (ruch nośników ładunku).
2.  Zewnętrzne pole magnetyczne ($B$) wywiera na nośniki siłę Lorentza, spychając je na jedną krawędź taśmy.
3.  Powstaje różnica potencjałów – **Napięcie Halla ($U$)**.
4.  Stan równowagi następuje, gdy wytworzone pole elektryczne zrównoważy siłę magnetyczną ($eE = ev_d B$).

### Zastosowania
1.  **Sonda Halla**: Do pomiaru indukcji pola magnetycznego ($B$).
    $$U = \frac{I B l}{n e S}$$
2.  **Określanie znaku nośników**: Pozwala stwierdzić, czy prąd przenoszą "plusy" (dziury) czy "minusy" (elektrony).



---

> [!SUMMARY] Analogia podsumowująca
> * **Spektrometr masowy** działa jak sito: najpierw "przesiewa" cząstki o złej prędkości, a potem sortuje resztę według wagi (masy).
> * **Cyklotron** używa siły magnetycznej jako "uprzęży" (trzyma cząstkę na uwięzi kołowej), a siły elektrycznej jako "bicz" (przyspiesza ją co okrążenie).