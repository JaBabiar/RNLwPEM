# Moduł I: Podstawy Pól Elektrycznego i Magnetycznego

## 1. Pole Elektryczne (E)

### Definicja i źródła

> [!NOTE]
> **Pole elektryczne** jest stanem przestrzeni, w której na obiekt fizyczny mający ładunek elektryczny działają siły o naturze elektromagnetycznej. Jest to składowa pola elektromagnetycznego.

1.  **Źródło**: Źródłem pola elektrycznego są **ładunki elektryczne**.
2.  **Oddziaływanie**: Pole to powoduje:
    * Działanie siły na naładowaną cząstkę.
    * Zmianę energii (wykonanie pracy) ładunku elektrycznego.

### Wektor natężenia pola ($E$)
Natężenie pola elektrycznego ($E$) definiowane jest jako siła ($F$) działająca na dodatni ładunek próbny ($q_0$) umieszczony w danym punkcie:

$$
E = \frac{F}{q_0}
$$

Wartość natężenia pola w punkcie oddalonym o $r$ od ładunku punktowego ($q$) określa **Prawo Coulomba**:

$$
E = \frac{1}{4\pi\epsilon_0} \cdot \frac{|q|}{r^2}
$$

### Linie Pola
* **Kierunek**: Wektor natężenia pola w dowolnym punkcie jest styczny do linii pola.
* **Zwrot**: Przyjmuje się, że linie pola biorą początek w **ładunkach dodatnich**, a kończą w **ładunkach ujemnych** (lub w nieskończoności).
* **Ładunek próbny**: Do określenia kierunku zawsze używa się ładunku *dodatniego*.

---

## 2. Pole Magnetyczne (B)

### Definicja i Źródła
1.  **Źródła**:
    * Materia o właściwościach magnetycznych (np. magnesy trwałe).
    * **Poruszający się ładunek elektryczny** (prąd elektryczny) – odkrycie Hansa Oersteda (1819 r.).
    * W magnesach trwałych: ustawienie spinów elektronów (mikroskopijne pętle prądu wg Ampère'a).
2.  **Oddziaływanie**: Pole magnetyczne wytwarza siłę, która oddziałuje **wyłącznie na poruszający się ładunek**.

### Wektor Indukcji Magnetycznej ($B$)
* Jest miarą pola magnetycznego.
* Jednostka SI: **Tesla ($T$)**.

### Właściwości Linii Pola Magnetycznego
W przeciwieństwie do pola elektrycznego:
* Linie są **ciągłe i tworzą zamknięte pętle** (pole jest bezźródłowe – brak "ładunków magnetycznych").
* Zorientowane od bieguna północnego (**N**) do południowego (**S**) na zewnątrz magnesu.

---

## 3. Pole Elektromagnetyczne (PEM)

> [!IMPORTANT]
> **Pole elektromagnetyczne** to układ wzajemnie powiązanych pól: **elektrycznego ($E$)** i **magnetycznego ($B$)**. Ich postrzeganie zależy od układu odniesienia obserwatora.

### Powiązanie Pól (Równania Maxwella)
Relacja jest wzajemna:
* Zmienne w czasie pole magnetyczne $\rightarrow$ wytwarza **wirowe pole elektryczne**.
* Poruszające się ładunki (prąd) oraz zmienne pole elektryczne $\rightarrow$ wytwarzają **wirowe pole magnetyczne**.

### Siła Lorentza
Całkowita siła działająca na ładunek ($q$) poruszający się z prędkością ($v$) w polu elektromagnetycznym. Jest sumą siły elektrycznej i magnetycznej:

$$
F = q(E + v \times B)
$$

| Rodzaj siły | Wzór | Właściwości |
| :--- | :--- | :--- |
| **Siła elektryczna** | $F_{el} = qE$ | Decyduje o zmianie energii (wykonuje pracę). |
| **Siła magnetyczna** | $F_{magn} = qv \times B$ | Działa **prostopadle** do wektora prędkości i indukcji $B$. **Nie wykonuje pracy**. |
