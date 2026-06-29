from django.core.management.base import BaseCommand

from courses.models import Course, Lesson, Module


COURSES_DATA = [
    {
        "title": "Python podstawy",
        "description": (
            "Kurs wprowadzający do języka Python "
            "dla osób początkujących."
        ),
        "level": Course.BEGINNER,
        "modules": [
            {
                "title": "Wprowadzenie do Pythona",
                "lessons": [
                    {
                        "title": "Instalacja Pythona",
                        "content": (
                            "Jak zainstalować Pythona "
                            "i przygotować środowisko pracy."
                        ),
                    },
                    {
                        "title": "Zmienne i typy danych",
                        "content": (
                            "Podstawowe typy danych, zmienne "
                            "i operacje w Pythonie."
                        ),
                    },
                ],
            },
        ],
    },
    {
        "title": "Django od podstaw",
        "description": (
            "Poznaj podstawy frameworka Django: projekt, aplikacje, "
            "modele, widoki, szablony i routing."
        ),
        "level": Course.INTERMEDIATE,
        "modules": [
            {
                "title": "Wprowadzenie do Django",
                "lessons": [
                    {
                        "title": "Co to jest Django?",
                        "content": (
                            "Wprowadzenie do frameworka Django "
                            "i jego zastosowań przy budowie "
                            "aplikacji webowych."
                        ),
                    },
                    {
                        "title": "Struktura projektu",
                        "content": (
                            "Poznasz pliki projektu Django, aplikacje "
                            "i rolę settings.py, urls.py oraz manage.py."
                        ),
                    },
                    {
                        "title": "Pierwsza aplikacja",
                        "content": (
                            "Tworzymy nową aplikację Django "
                            "i podłączamy ją do projektu."
                        ),
                    },
                ],
            },
            {
                "title": "Modele i baza danych",
                "lessons": [
                    {
                        "title": "Modele danych",
                        "content": (
                            "Nauczysz się tworzyć modele "
                            "reprezentujące dane w bazie."
                        ),
                    },
                    {
                        "title": "Migracje",
                        "content": (
                            "Omówienie makemigrations i migrate "
                            "oraz aktualizacji schematu bazy."
                        ),
                    },
                    {
                        "title": "Panel admina",
                        "content": (
                            "Poznasz możliwości panelu administracyjnego "
                            "Django i zarządzania danymi."
                        ),
                    },
                ],
            },
            {
                "title": "Widoki i szablony",
                "lessons": [
                    {
                        "title": "Widoki funkcyjne",
                        "content": (
                            "Tworzymy pierwsze widoki "
                            "i zwracamy odpowiedzi HTML."
                        ),
                    },
                    {
                        "title": "Szablony HTML",
                        "content": (
                            "Dowiesz się, jak działa renderowanie "
                            "szablonów i dziedziczenie base.html."
                        ),
                    },
                    {
                        "title": "Routing URL",
                        "content": (
                            "Łączenie widoków z adresami URL "
                            "i używanie nazwanych ścieżek."
                        ),
                    },
                ],
            },
        ],
    },
    {
        "title": "Bazy danych i SQL",
        "description": (
            "Kurs pokazujący podstawy relacyjnych baz danych, "
            "SQL i pracy z danymi."
        ),
        "level": Course.BEGINNER,
        "modules": [
            {
                "title": "Podstawy baz danych",
                "lessons": [
                    {
                        "title": "Czym jest baza danych?",
                        "content": (
                            "Podstawy baz danych, rekordów, "
                            "tabel i relacji."
                        ),
                    },
                    {
                        "title": "Tabele i rekordy",
                        "content": (
                            "Jak organizować dane w tabelach "
                            "i interpretować rekordy."
                        ),
                    },
                    {
                        "title": "Klucze główne i obce",
                        "content": (
                            "Poznasz podstawy relacji między tabelami "
                            "przy użyciu kluczy."
                        ),
                    },
                ],
            },
            {
                "title": "Zapytania SQL",
                "lessons": [
                    {
                        "title": "SELECT i WHERE",
                        "content": (
                            "Pobieranie danych z tabel "
                            "i filtrowanie wyników."
                        ),
                    },
                    {
                        "title": "ORDER BY i GROUP BY",
                        "content": (
                            "Sortowanie danych i podstawowe "
                            "grupowanie wyników."
                        ),
                    },
                    {
                        "title": "INSERT UPDATE DELETE",
                        "content": (
                            "Dodawanie, aktualizacja i usuwanie "
                            "rekordów w SQL."
                        ),
                    },
                ],
            },
            {
                "title": "Łączenie tabel i praktyka",
                "lessons": [
                    {
                        "title": "JOIN",
                        "content": (
                            "W tej lekcji omówimy łączenie danych "
                            "z wielu tabel."
                        ),
                    },
                    {
                        "title": "Praktyczne zapytania",
                        "content": (
                            "Przykłady praktycznych zapytań do bazy "
                            "danych w codziennej pracy."
                        ),
                    },
                    {
                        "title": "Najczęstsze błędy SQL",
                        "content": (
                            "Błędy początkujących i sposoby "
                            "ich diagnozowania."
                        ),
                    },
                ],
            },
        ],
    },
    {
        "title": "Tworzenie aplikacji webowych",
        "description": (
            "Praktyczny kurs łączący HTML, CSS, logikę backendu "
            "i wdrażanie prostych aplikacji."
        ),
        "level": Course.ADVANCED,
        "modules": [
            {
                "title": "Frontend aplikacji",
                "lessons": [
                    {
                        "title": "HTML w praktyce",
                        "content": (
                            "Budowa struktury strony z użyciem "
                            "podstawowych znaczników HTML."
                        ),
                    },
                    {
                        "title": "Stylowanie CSS",
                        "content": (
                            "Wprowadzenie do stylów, klas, kolorów, "
                            "odstępów i prostego layoutu."
                        ),
                    },
                    {
                        "title": "Responsywność",
                        "content": (
                            "Dostosowanie wyglądu strony do ekranów "
                            "mobilnych i desktopowych."
                        ),
                    },
                ],
            },
            {
                "title": "Backend aplikacji",
                "lessons": [
                    {
                        "title": "Obsługa formularzy",
                        "content": (
                            "Poznasz wysyłanie danych z formularza "
                            "i odbieranie ich po stronie serwera."
                        ),
                    },
                    {
                        "title": "Logika aplikacji",
                        "content": (
                            "Tworzenie prostych reguł działania aplikacji "
                            "i przetwarzanie danych."
                        ),
                    },
                    {
                        "title": "Autoryzacja użytkownika",
                        "content": (
                            "Omówienie logowania, wylogowania "
                            "i ograniczania dostępu do zasobów."
                        ),
                    },
                ],
            },
            {
                "title": "Publikacja projektu",
                "lessons": [
                    {
                        "title": "Przygotowanie projektu",
                        "content": (
                            "Porządkowanie aplikacji przed publikacją "
                            "i testowaniem."
                        ),
                    },
                    {
                        "title": "Podstawy wdrożenia",
                        "content": (
                            "Co trzeba przygotować, aby aplikację uruchomić "
                            "poza lokalnym środowiskiem."
                        ),
                    },
                    {
                        "title": "Utrzymanie i rozwój",
                        "content": (
                            "Dalsza rozbudowa projektu, poprawki "
                            "i organizacja pracy po wdrożeniu."
                        ),
                    },
                ],
            },
        ],
    },
    {
        "title": "Git i GitHub",
        "description": (
            "Nauka pracy z repozytorium, commitami, branchami "
            "i publikacją kodu na GitHubie."
        ),
        "level": Course.BEGINNER,
        "modules": [
            {
                "title": "Podstawy Gita",
                "lessons": [
                    {
                        "title": "Instalacja Gita",
                        "content": (
                            "Instalacja Gita i sprawdzenie poprawności "
                            "konfiguracji."
                        ),
                    },
                    {
                        "title": "Pierwsze repozytorium",
                        "content": (
                            "Tworzenie repozytorium i podstawowy "
                            "workflow pracy."
                        ),
                    },
                    {
                        "title": "Commit i historia zmian",
                        "content": (
                            "Zapisywanie zmian i przegląd historii projektu."
                        ),
                    },
                ],
            },
            {
                "title": "Praca na branchach",
                "lessons": [
                    {
                        "title": "Tworzenie branchy",
                        "content": (
                            "Jak tworzyć osobne gałęzie do nowych funkcji."
                        ),
                    },
                    {
                        "title": "Merge branchy",
                        "content": (
                            "Łączenie zmian z różnych gałęzi projektu."
                        ),
                    },
                    {
                        "title": "Rozwiązywanie konfliktów",
                        "content": (
                            "Podstawy naprawy konfliktów podczas scalania."
                        ),
                    },
                ],
            },
            {
                "title": "GitHub w praktyce",
                "lessons": [
                    {
                        "title": "Push do GitHuba",
                        "content": (
                            "Wysyłanie lokalnego repozytorium na GitHuba."
                        ),
                    },
                    {
                        "title": "Pull request",
                        "content": (
                            "Współpraca przez pull requesty i code review."
                        ),
                    },
                    {
                        "title": "README projektu",
                        "content": (
                            "Tworzenie prostego i czytelnego README."
                        ),
                    },
                ],
            },
        ],
    },
    {
        "title": "HTML i CSS od zera",
        "description": (
            "Podstawy tworzenia stron internetowych z użyciem HTML i CSS."
        ),
        "level": Course.BEGINNER,
        "modules": [
            {
                "title": "HTML podstawy",
                "lessons": [
                    {
                        "title": "Struktura dokumentu HTML",
                        "content": (
                            "Poznasz podstawowe znaczniki "
                            "i układ dokumentu HTML."
                        ),
                    },
                    {
                        "title": "Nagłówki, akapity i linki",
                        "content": (
                            "Tworzenie podstawowych elementów treści w HTML."
                        ),
                    },
                    {
                        "title": "Listy i obrazy",
                        "content": (
                            "Dodawanie list oraz obrazów do strony."
                        ),
                    },
                ],
            },
            {
                "title": "CSS podstawy",
                "lessons": [
                    {
                        "title": "Selektory CSS",
                        "content": (
                            "Podstawowe sposoby stylowania elementów strony."
                        ),
                    },
                    {
                        "title": "Kolory i czcionki",
                        "content": (
                            "Zmiana kolorów, tła i wyglądu tekstu."
                        ),
                    },
                    {
                        "title": "Margin, padding, border",
                        "content": (
                            "Model pudełkowy i odstępy w CSS."
                        ),
                    },
                ],
            },
            {
                "title": "Układ strony",
                "lessons": [
                    {
                        "title": "Flexbox",
                        "content": (
                            "Nowoczesne układanie elementów "
                            "w jednym wymiarze."
                        ),
                    },
                    {
                        "title": "Grid",
                        "content": (
                            "Tworzenie bardziej złożonych layoutów "
                            "przy użyciu CSS Grid."
                        ),
                    },
                    {
                        "title": "Responsywność",
                        "content": (
                            "Dostosowanie strony do różnych urządzeń."
                        ),
                    },
                ],
            },
        ],
    },
    {
        "title": "JavaScript podstawy",
        "description": (
            "Wprowadzenie do JavaScriptu i interakcji "
            "na stronach internetowych."
        ),
        "level": Course.INTERMEDIATE,
        "modules": [
            {
                "title": "Start z JavaScriptem",
                "lessons": [
                    {
                        "title": "Zmienne i typy",
                        "content": (
                            "Podstawowe typy danych i deklarowanie "
                            "zmiennych w JavaScript."
                        ),
                    },
                    {
                        "title": "Operatory i warunki",
                        "content": (
                            "Instrukcje warunkowe i operatory logiczne."
                        ),
                    },
                    {
                        "title": "Pętle",
                        "content": (
                            "Powtarzanie operacji z użyciem pętli."
                        ),
                    },
                ],
            },
            {
                "title": "Funkcje i DOM",
                "lessons": [
                    {
                        "title": "Funkcje",
                        "content": (
                            "Tworzenie i wywoływanie funkcji."
                        ),
                    },
                    {
                        "title": "Manipulacja DOM",
                        "content": (
                            "Zmiana zawartości strony przy użyciu JavaScript."
                        ),
                    },
                    {
                        "title": "Obsługa zdarzeń",
                        "content": (
                            "Kliknięcia, formularze i reakcja "
                            "na akcje użytkownika."
                        ),
                    },
                ],
            },
            {
                "title": "Praktyka",
                "lessons": [
                    {
                        "title": "Prosty kalkulator",
                        "content": (
                            "Ćwiczenie praktyczne z logiką i interfejsem."
                        ),
                    },
                    {
                        "title": "Lista zadań",
                        "content": "Budowa małej aplikacji TODO.",
                    },
                    {
                        "title": "Walidacja formularza",
                        "content": (
                            "Sprawdzanie poprawności danych w formularzu."
                        ),
                    },
                ],
            },
        ],
    },
    {
        "title": "Django REST Framework",
        "description": (
            "Tworzenie prostych API w Django REST Framework "
            "krok po kroku."
        ),
        "level": Course.ADVANCED,
        "modules": [
            {
                "title": "Podstawy API",
                "lessons": [
                    {
                        "title": "Czym jest REST API",
                        "content": (
                            "Poznasz podstawowe założenia REST "
                            "i komunikacji klient-serwer."
                        ),
                    },
                    {
                        "title": "Instalacja DRF",
                        "content": (
                            "Dodanie Django REST Framework do projektu "
                            "i podstawowa konfiguracja."
                        ),
                    },
                    {
                        "title": "Pierwszy endpoint",
                        "content": (
                            "Tworzenie pierwszego widoku API "
                            "zwracającego dane."
                        ),
                    },
                ],
            },
            {
                "title": "Serializery i widoki",
                "lessons": [
                    {
                        "title": "Serializery",
                        "content": (
                            "Konwersja danych modeli na JSON "
                            "i walidacja danych wejściowych."
                        ),
                    },
                    {
                        "title": "APIView i generics",
                        "content": (
                            "Budowa endpointów przy użyciu klas DRF."
                        ),
                    },
                    {
                        "title": "CRUD API",
                        "content": (
                            "Tworzenie pełnych endpointów do dodawania, "
                            "edycji i usuwania danych."
                        ),
                    },
                ],
            },
            {
                "title": "Autoryzacja i testy",
                "lessons": [
                    {
                        "title": "Permission classes",
                        "content": (
                            "Ograniczanie dostępu do endpointów."
                        ),
                    },
                    {
                        "title": "Token authentication",
                        "content": (
                            "Podstawy autoryzacji tokenowej."
                        ),
                    },
                    {
                        "title": "Testowanie API",
                        "content": (
                            "Pisanie prostych testów dla endpointów REST."
                        ),
                    },
                ],
            },
        ],
    },
    {
        "title": "Docker dla początkujących",
        "description": (
            "Podstawy konteneryzacji aplikacji z użyciem Dockera."
        ),
        "level": Course.INTERMEDIATE,
        "modules": [
            {
                "title": "Wprowadzenie do Dockera",
                "lessons": [
                    {
                        "title": "Czym jest Docker",
                        "content": (
                            "Wprowadzenie do kontenerów "
                            "i ich zastosowań."
                        ),
                    },
                    {
                        "title": "Instalacja Dockera",
                        "content": (
                            "Instalacja Dockera i sprawdzenie działania "
                            "środowiska."
                        ),
                    },
                    {
                        "title": "Pierwszy kontener",
                        "content": (
                            "Uruchomienie pierwszego kontenera "
                            "i zrozumienie podstawowych komend."
                        ),
                    },
                ],
            },
            {
                "title": "Obrazy i Dockerfile",
                "lessons": [
                    {
                        "title": "Budowanie obrazu",
                        "content": (
                            "Tworzenie własnego obrazu aplikacji."
                        ),
                    },
                    {
                        "title": "Dockerfile",
                        "content": (
                            "Pisanie pliku Dockerfile krok po kroku."
                        ),
                    },
                    {
                        "title": "Tagowanie i wersje",
                        "content": "Zarządzanie wersjami obrazów.",
                    },
                ],
            },
            {
                "title": "Docker Compose",
                "lessons": [
                    {
                        "title": "Compose basics",
                        "content": (
                            "Łączenie kilku usług w jednym środowisku."
                        ),
                    },
                    {
                        "title": "Aplikacja + baza danych",
                        "content": (
                            "Uruchamianie aplikacji wraz z bazą danych "
                            "w Docker Compose."
                        ),
                    },
                    {
                        "title": "Praca developerska",
                        "content": (
                            "Najwygodniejszy workflow lokalny z Dockerem."
                        ),
                    },
                ],
            },
        ],
    },
]


class Command(BaseCommand):
    help = "Dodaje przykładowe kursy, moduły i lekcje do bazy danych."

    def handle(self, *args, **options):
        created_courses = 0
        created_modules = 0
        created_lessons = 0
        updated_courses = 0
        updated_lessons = 0

        for course_data in COURSES_DATA:
            course, course_created = Course.objects.update_or_create(
                title=course_data["title"],
                defaults={
                    "description": course_data["description"],
                    "level": course_data["level"],
                },
            )

            if course_created:
                created_courses += 1
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Dodano kurs: {course.title}"
                    )
                )
            else:
                updated_courses += 1
                self.stdout.write(
                    self.style.WARNING(
                        f"Zaktualizowano kurs: {course.title}"
                    )
                )

            for module_data in course_data["modules"]:
                module, module_created = Module.objects.get_or_create(
                    course=course,
                    title=module_data["title"],
                )

                if module_created:
                    created_modules += 1
                    self.stdout.write(f"  Dodano moduł: {module.title}")

                for lesson_data in module_data["lessons"]:
                    lesson, lesson_created = Lesson.objects.update_or_create(
                        module=module,
                        title=lesson_data["title"],
                        defaults={
                            "content": lesson_data["content"],
                        },
                    )

                    if lesson_created:
                        created_lessons += 1
                        self.stdout.write(
                            f"    Dodano lekcję: {lesson.title}"
                        )
                    else:
                        updated_lessons += 1

        self.stdout.write("")
        self.stdout.write(self.style.SUCCESS("Seed zakończony."))
        self.stdout.write(f"Nowe kursy: {created_courses}")
        self.stdout.write(f"Nowe moduły: {created_modules}")
        self.stdout.write(f"Nowe lekcje: {created_lessons}")
        self.stdout.write(f"Zaktualizowane kursy: {updated_courses}")
        self.stdout.write(f"Zaktualizowane lekcje: {updated_lessons}")