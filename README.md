# EduPortal Integracja

Portal e-learningowy zbudowany w Django. Aplikacja umożliwia przeglądanie kursów, podział materiału na moduły i lekcje, zapisywanie użytkownika na kurs, śledzenie postępu nauki oraz podstawową obsługę kont użytkowników.[cite:3268]

## Opis projektu

Projekt został przygotowany jako końcowy system w ramach przedmiotu Integracja Systemów Informatycznych. Założeniem było stworzenie kompletnej aplikacji webowej z wykorzystaniem nowoczesnych praktyk inżynierii oprogramowania: wersjonowania w GitHub, konteneryzacji Docker, konfiguracji przez zmienne środowiskowe oraz przygotowania pod CI/CD.[cite:3268]

Główne funkcjonalności:
- przegląd listy kursów,
- widok szczegółów kursu,
- podział kursów na moduły i lekcje,
- zapis użytkownika na kurs,
- oznaczanie lekcji jako ukończonych,
- śledzenie progresu użytkownika,
- logowanie użytkownika.[cite:3268]

## Stos technologiczny

- Python
- Django
- SQLite (lokalnie)
- Docker
- Docker Compose
- Git + GitHub
- GitHub Actions (CI)

## Struktura projektu

```text
eduportal-integracja/
├── config/
├── courses/
├── users/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
├── .env.example
└── README.md
```

## Architektura aplikacji

Aplikacja działa w architekturze webowej, gdzie użytkownik komunikuje się z backendem Django, a dane przechowywane są w bazie danych. W wersji lokalnej projekt może działać z SQLite, a w wersji kontenerowej może zostać podpięty do osobnego serwisu bazy danych zdefiniowanego w `docker-compose.yml`.[cite:3268]

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
- jeden `User` może mieć wiele rekordów `LessonProgress`.[cite:3268]

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

### 3. Instalacja zależności

```bash
pip install -r requirements.txt
```

### 4. Konfiguracja zmiennych środowiskowych

Skopiuj plik przykładowy:

```bash
copy .env.example .env
```

Następnie uzupełnij potrzebne wartości w `.env`.[cite:3268]

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

Jeśli projekt wymaga migracji po starcie kontenerów, można wykonać:

```bash
docker-compose exec web python manage.py migrate
```

## CI/CD

Projekt jest przygotowany pod automatyzację z użyciem GitHub Actions. Pipeline CI powinien uruchamiać się przy `push` i `pull request`, wykonywać instalację zależności, linter, testy oraz weryfikować poprawność budowania obrazu Dockera.[cite:3268]

## Bezpieczeństwo

Wrażliwe dane, takie jak `SECRET_KEY`, hasła lub klucze API, nie powinny znajdować się bezpośrednio w repozytorium. Konfiguracja powinna być przekazywana przez zmienne środowiskowe lub systemy typu GitHub Secrets.[cite:3268]

## Status wymagań projektowych

Zrealizowane elementy:
- repozytorium GitHub,
- aplikacja webowa w Django,
- konteneryzacja przez Docker i Docker Compose,
- konfiguracja przez `.env.example`,
- przygotowanie pod CI.[cite:3268]

Do pełnego domknięcia projektu można dodatkowo uzupełnić:
- wdrożenie wersji live,
- pełny pipeline CI/CD,
- rozszerzone testy i pomiar coverage.[cite:3268]
