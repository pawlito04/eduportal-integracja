# EduPortal Integracja

Portal e-learningowy zbudowany w Django. Aplikacja umożliwia przeglądanie kursów, podział materiału na moduły i lekcje, zapisywanie użytkownika na kurs, śledzenie postępu nauki oraz podstawową obsługę kont użytkowników.

## Wersja live

Aplikacja dostępna online:
https://eduportal-integracja-1.onrender.com

## Opis projektu

Projekt został przygotowany jako końcowy system w ramach przedmiotu Integracja Systemów Informatycznych. Celem było stworzenie kompletnej aplikacji webowej z wykorzystaniem nowoczesnych praktyk inżynierii oprogramowania, takich jak wersjonowanie w GitHub, konteneryzacja Docker, konfiguracja przez zmienne środowiskowe, automatyzacja CI oraz wdrożenie wersji live.

Główne funkcjonalności:
- przegląd listy kursów,
- widok szczegółów kursu,
- podział kursów na moduły i lekcje,
- zapis użytkownika na kurs,
- oznaczanie lekcji jako ukończonych,
- śledzenie progresu użytkownika,
- logowanie użytkownika.

## Stos technologiczny

- Python
- Django
- SQLite
- Docker
- Docker Compose
- Git + GitHub
- GitHub Actions
- Render

## Struktura projektu

```text
eduportal-integracja/
├── config/
├── courses/
├── users/
├── .github/
│   └── workflows/
│       └── ci.yml
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
├── .env.example
└── README.md
```

## Architektura aplikacji

Aplikacja działa w architekturze webowej, gdzie użytkownik komunikuje się z backendem Django, a dane przechowywane są w bazie danych. W środowisku lokalnym projekt korzysta z SQLite, natomiast aplikacja została przygotowana do uruchamiania także w środowisku kontenerowym oraz do wdrożenia w chmurze.

Przykładowy przepływ żądania:
1. Użytkownik otwiera stronę w przeglądarce.
2. Żądanie trafia do routingu Django (`urls.py`).
3. Routing przekazuje żądanie do odpowiedniego widoku.
4. Widok pobiera dane z modeli i bazy danych.
5. Django renderuje szablon HTML i zwraca odpowiedź do przeglądarki.

## Model danych

Najważniejsze encje w projekcie:
- **User** – użytkownik systemu,
- **Course** – kurs,
- **Module** – moduł należący do kursu,
- **Lesson** – lekcja należąca do modułu,
- **Enrollment** – zapis użytkownika na kurs,
- **LessonProgress** – postęp użytkownika w lekcjach.

Relacje:
- jeden `Course` ma wiele `Module`,
- jeden `Module` ma wiele `Lesson`,
- jeden `User` może mieć wiele `Enrollment`,
- jeden `User` może mieć wiele rekordów `LessonProgress`.

## Uruchomienie lokalne

### 1. Klonowanie repozytorium

```bash
git clone https://github.com/pawlito04/eduportal-integracja.git
cd eduportal-integracja
```

### 2. Utworzenie i aktywacja środowiska wirtualnego

Windows:
```bash
py -m venv .venv
.venv\Scripts\activate
```

Linux / macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalacja zależności

```bash
pip install -r requirements.txt
```

### 4. Konfiguracja zmiennych środowiskowych

Skopiuj plik przykładowy:

Windows:
```bash
copy .env.example .env
```

Linux / macOS:
```bash
cp .env.example .env
```

Następnie uzupełnij wymagane wartości w `.env`.

### 5. Migracje

```bash
py manage.py migrate
```

### 6. Uruchomienie aplikacji

```bash
py manage.py runserver
```

Aplikacja będzie dostępna pod adresem:

```text
http://127.0.0.1:8000/
```

## Uruchomienie przez Docker

```bash
docker-compose up --build
```

Jeśli po starcie kontenerów potrzebne są migracje:

```bash
docker-compose exec web python manage.py migrate
```

## CI/CD

Projekt wykorzystuje GitHub Actions do automatycznej weryfikacji jakości kodu. Pipeline CI uruchamia się przy zmianach w repozytorium i obejmuje między innymi linter `flake8`, testy oraz weryfikację poprawności konfiguracji projektu.

Wersja produkcyjna została wdrożona na platformie Render:
https://eduportal-integracja-1.onrender.com

## Deployment

Aplikacja została wdrożona jako web service na platformie Render. Render automatycznie pobiera kod z repozytorium GitHub i wykonuje ponowny deploy po kolejnych zmianach na głównej gałęzi projektu.

Przy wdrożeniu wykorzystano konfigurację środowiskową, w tym między innymi:
- `SECRET_KEY`
- `DEBUG`
- `ALLOWED_HOSTS`

Dla środowiska produkcyjnego aplikacja powinna mieć ustawione `DEBUG=False`, a `ALLOWED_HOSTS` powinno zawierać domenę usługi Render, np. `eduportal-integracja-1.onrender.com`.

## Bezpieczeństwo

Wrażliwe dane, takie jak `SECRET_KEY`, hasła lub klucze API, nie powinny znajdować się bezpośrednio w repozytorium. Konfiguracja powinna być przekazywana przez zmienne środowiskowe lub mechanizmy sekretów dostępne w środowisku uruchomieniowym.

Do repozytorium nie powinny trafiać pliki takie jak:
- `.env`
- `db.sqlite3`
- `__pycache__/`
- pliki tymczasowe i artefakty środowiska lokalnego

## Status projektu

Zrealizowane elementy:
- repozytorium GitHub,
- aplikacja webowa w Django,
- konteneryzacja przez Docker i Docker Compose,
- konfiguracja przez `.env.example`,
- pipeline CI w GitHub Actions,
- wdrożenie wersji live na Render.

Możliwe dalsze rozszerzenia:
- rozbudowa testów i pomiar coverage,
- wdrożenie pełnego CD sterowanego po sukcesie CI,
- podpięcie zewnętrznej bazy PostgreSQL,
- rozszerzenie modułu użytkowników i panelu administracyjnego.

## Autor

Projekt przygotowany w ramach przedmiotu Integracja Systemów Informatycznych.