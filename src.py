from typing import Dict, List, Iterator, Optional

class Movie:
    def __init__(self, title: str, year: int, genre: str, director: str) -> None:
        self.title = title
        self.year = year
        self.genre = genre
        self.director = director

class MovieIterator:
    def __init__(self, movies: Dict[str, Movie]) -> None:
        self._movies = list(movies.values())
        self._index: int = 0

    def __iter__(self) -> Iterator[Movie]:
        return self

    def __next__(self) -> Movie:
        if self._index < len(self._movies):
            movie = self._movies[self._index]
            self._index += 1
            return movie
        raise StopIteration

class MovieCollection:
    def __init__(self) -> None:
        self._movies: Dict[str, Movie] = {}

    def add_movie(self, movie: Movie) -> None:
        if movie.title in self._movies:
            raise ValueError(f"Фильм '{movie.title}' уже существует в коллекции.")
        self._movies[movie.title] = movie

    def remove_movie(self, title: str) -> None:
        if title not in self._movies:
            raise KeyError(f"Фильм '{title}' не найден в коллекции.")
        del self._movies[title]

    def search_by_title(self, title: str) -> Optional[Movie]:
        return self._movies.get(title)

    def search_by_year(self, year: int) -> List[Movie]:
        return [movie for movie in self._movies.values() if movie.year == year]

    def search_by_genre(self, genre: str) -> List[Movie]:
        return [movie for movie in self._movies.values() if movie.genre == genre]

    def __iter__(self) -> MovieIterator:
        return MovieIterator(self._movies)

# Пример использования
if __name__ == "__main__":
    # Создание фильмов
    movie1 = Movie("Начало", 2010, "Фантастика", "Кристофер Нолан")
    movie2 = Movie("Темный рыцарь", 2008, "Боевик", "Кристофер Нолан")

    # Инициализация коллекции
    collection = MovieCollection()

    # Добавление фильмов
    collection.add_movie(movie1)
    collection.add_movie(movie2)

    # Перебор коллекции с использованием итератора
    print("Все фильмы в коллекции:")
    for movie in collection:
        print(f"- {movie.title} ({movie.year})")

    # Поиск по году
    print("\nФильмы 2010 года:")
    movies_2010 = collection.search_by_year(2010)
    for movie in movies_2010:
        print(f"- {movie.title}")

    # Удаление фильма
    collection.remove_movie("Начало")
    print("\nПосле удаления 'Начало':")
    for movie in collection:
        print(f"- {movie.title}")