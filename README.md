Dominik Nowik 122392
## 1. Instrukcje uruchamiania aplikacji

### Uruchamianie lokalnie

1. Utwórz i aktywuj środowisko wirtualne.

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Zainstaluj zależności:
```bash
pip install -r requirements.txt
```

3. Uruchom aplikację:
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

4. Test działania:
```bash
curl http://127.0.0.1:8000/health
```

---

### Uruchamianie za pomocą Dockera

1. Zbuduj obraz:
```bash
docker build -t ml-api .
```

2. Uruchom kontener:
```bash
docker run -d -p 8000:8000 --name ml-api-container ml-api
```

3. Test działania:
```bash
curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d "{\"hours\":3}"
```

4. Zatrzymanie i usunięcie kontenera:
```bash
docker stop ml-api-container
docker rm ml-api-container
```

---

### Uruchamianie za pomocą Docker Compose

1. Uruchom usługi:
```bash
docker compose up --build -d
```

2. Sprawdź działające kontenery:
```bash
docker compose ps
```

3. Test działania:
```bash
curl http://127.0.0.1:8000/health
```

lub

```bash
curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d "{\"hours\":3}"
```

4. Zatrzymanie usług:
```bash
docker compose down
```

---

## 2. Konfiguracja parametrów i wymagane zasoby

### Konfiguracja parametrów

Aplikacja działa domyślnie na:
- porcie `8000`
- hoście `0.0.0.0`

Najważniejsze parametry można konfigurować przy uruchamianiu serwera, np.:
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

W środowisku Docker lub Docker Compose parametry mogą być przekazywane także przez zmienne środowiskowe.

Przykładowe zmienne środowiskowe, które można stosować przy dalszym rozwoju aplikacji:
- `APP_HOST=0.0.0.0`
- `APP_PORT=8000`
- `REDIS_HOST=redis`
- `REDIS_PORT=6379`

### Wymagane zasoby

Do działania aplikacji potrzebne są:
- Python 3.9 lub nowszy albo Docker Desktop,
- biblioteki z pliku `requirements.txt`,
- wolny port `8000`,
- przy uruchamianiu przez Docker Compose także działające środowisko Docker i dodatkowy serwis, np. Redis.

Minimalne zasoby sprzętowe:
- 1 rdzeń CPU,
- około 512 MB RAM dla samej aplikacji,
- więcej pamięci przy pracy z Docker Desktop i dodatkowymi kontenerami.

### Dokumentacja API

Po uruchomieniu aplikacji dokumentacja FastAPI jest dostępna pod adresem:
```text
http://127.0.0.1:8000/docs
```
