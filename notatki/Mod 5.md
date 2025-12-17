#fizyka #elektromagnetyzm #siła_elektrodynamiczna #moment_siły #silnik #notatka

# Moduł V: Siły Działające na Przewodniki i Pętle z Prądem

Ten moduł przenosi analizę z poziomu mikroskopowego (pojedynczy ładunek) na makroskopowy (przewodnik z prądem).

---

## 1. Siła Magnetyczna na Przewodnik (Siła Elektrodynamiczna)

Skoro pole magnetyczne działa na poruszający się ładunek, to działa też na przewód, w którym płynie rzeka ładunków (prąd).

### A. Wzór na siłę
Dla prostoliniowego przewodnika o długości $l$ w jednorodnym polu magnetycznym:

$$\vec{F} = I (\vec{l} \times \vec{B})$$

* **Wartość siły ($F$)**:
    * **Max**: Gdy przewodnik jest prostopadły do pola ($90^\circ$).
    * **Zero**: Gdy przewodnik jest równoległy do pola ($0^\circ$).

### B. Kierunek (RHR-1)
Stosujemy **Regułę Prawej Dłoni 1** (tak samo jak przy pojedynczym ładunku):
1.  **Palce**: Wzdłuż przewodu, zgodnie z kierunkiem prądu ($I$).
2.  **Zgięcie**: W stronę pola magnetycznego ($B$).
3.  **Kciuk**: Wskazuje zwrot siły ($F$).



---

## 2. Źródła Pola (Prawo Oersteda)

Prąd płynący w przewodzie nie tylko *odczuwa* pole magnetyczne, ale sam je **wytwarza**.

### Reguła Prawej Dłoni 2 (RHR-2)
Służy do wyznaczania kształtu pola wokół przewodu.

> [!WARNING] RHR-1 vs RHR-2
> * **RHR-1 (Płaska dłoń)**: Używasz do siły działającej na przewodnik/ładunek.
> * **RHR-2 (Kciuk i zaciśnięte palce)**: Używasz do pola wytwarzanego przez prąd.

**Instrukcja RHR-2:**
1.  **Kciuk**: Wskazuje kierunek prądu ($I$).
2.  **Zgięte palce**: Wskazują kierunek wirowania linii pola magnetycznego ($B$) wokół przewodu.



---

## 3. Pętle z Prądem i Moment Siły (Silniki)

To fundament działania silników elektrycznych. Rozważamy ramkę (pętlę) z prądem wrzuconą w jednorodne pole magnetyczne.

### A. Siła Wypadkowa
> [!IMPORTANT] Siły się równoważą
> W jednorodnym polu magnetycznym siła wypadkowa działająca na zamkniętą pętlę wynosi **ZERO** ($\sum F = 0$).
> Siła ciągnąca górną część ramki równoważy siłę ciągnącą dolną część itd.

### B. Moment Siły ($\vec{M}$)
Mimo że pętla nie "przesunie się" w przestrzeni (bo siła wypadkowa to 0), to **zacznie się obracać**.
Moment siły powodujący obrót opisuje wzór:

$$\vec{M} = \vec{\mu} \times \vec{B}$$

Gdzie:
* $\vec{M}$ – Moment siły (odpowiedzialny za obrót).
* $\vec{\mu}$ – Magnetyczny moment dipolowy ramki.
* $\vec{B}$ – Indukcja magnetyczna.

### C. Magnetyczny Moment Dipolowy ($\vec{\mu}$)
Wektor opisujący "siłę magnetyczną" samej ramki.
$$\vec{\mu} = I \cdot S \cdot \vec{n}$$
* $I$ – Prąd.
* $S$ – Pole powierzchni pętli.
* $\vec{n}$ – Wektor normalny (prostopadły do powierzchni pętli).

**Kierunek $\vec{\mu}$ (znowu RHR-2):**
Zwiń palce zgodnie z prądem w pętli $\rightarrow$ Kciuk pokaże wektor $\vec{\mu}$ (czyli biegun północny "magnesu", którym stała się ramka).



### D. Energia Potencjalna ($E_p$)
Układ dąży do minimum energii. Energia potencjalna dipola w polu:

$$E_p = - \vec{\mu} \cdot \vec{B} = -\mu B \cos \theta$$

| Ustawienie | Kąt | Energia | Opis |
| :--- | :--- | :--- | :--- |
| **Zgodne** ($\vec{\mu} \parallel \vec{B}$) | $0^\circ$ | **Minimum** ($-\mu B$) | Stan stabilny. Ramka chce tu zostać. |
| **Prostopadłe** ($\vec{\mu} \perp \vec{B}$) | $90^\circ$ | **Zero** | Moment siły jest tu największy (maksymalny obrót). |
| **Przeciwne** ($\vec{\mu}$ anty-równoległe do $\vec{B}$) | $180^\circ$ | **Maximum** ($+\mu B$) | Stan niestabilny. Najmniejsze trącenie spowoduje obrót. |

> [!SUMMARY] Podsumowanie działania silnika
> Pole magnetyczne stara się obrócić ramkę tak, aby jej moment dipolowy ($\vec{\mu}$) ustawił się zgodnie z liniami pola ($\vec{B}$). Gdy to zrobi, silnik stanąłby w miejscu – dlatego w silnikach używa się komutatora, który w odpowiednim momencie odwraca prąd, zmuszając ramkę do ciągłego obrotu.