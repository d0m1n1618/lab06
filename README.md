# LAB06 - Testy jednostkowe i CI/CD dla projektu ML

W ramach laboratorium przygotowano prosty projekt ML z użyciem biblioteki `scikit-learn` oraz skonfigurowano automatyczne testowanie i publikację obrazu Dockera.

### 1. Przygotowanie projektu ML
- utworzono repozytorium GitHub `lab06`,
- dodano pliki projektu, m.in.:
  - `model.py` - logika trenowania modelu i predykcji,
  - `test_model.py` - testy jednostkowe,
  - `requirements.txt` - wymagane biblioteki.

### 2. Testy jednostkowe
Przygotowano 4 testy jednostkowe w `pytest`, które sprawdzają:
- czy model zwraca predykcje,
- czy liczba predykcji jest poprawna,
- czy predykcje należą do oczekiwanych klas,
- czy model osiąga wymaganą dokładność.

Testy zostały uruchomione lokalnie i zakończyły się wynikiem:
- `4 passed`

### 3. GitHub Actions - automatyczne testowanie
Dodano workflow GitHub Actions w folderze:
- `.github/workflows/python-tests.yml`

Workflow:
- uruchamia się przy każdym `push` i `pull request` do gałęzi `main`,
- instaluje zależności z `requirements.txt`,
- uruchamia testy jednostkowe.

### 4. Docker i automatyczna publikacja obrazu
Dodano:
- `Dockerfile`
- `.dockerignore`

Skonfigurowano drugi workflow GitHub Actions, który:
- buduje obraz Dockera po każdym `push` do `main`,
- publikuje obraz do GitHub Container Registry (`ghcr.io`).

Obraz został poprawnie opublikowany jako:
- `ghcr.io/d0m1n1618/lab06:latest`

Laboratorium pozwoliło przećwiczyć przygotowanie projektu ML, napisanie testów jednostkowych oraz automatyzację testowania i publikacji obrazu Dockera z użyciem GitHub Actions.
