class MediaElement:
    def __init__(self, title: str):
        self.__title = title

    def show(self, title):
        return title
    

class Movie(MediaElement):
    def __init__(self, title: str, director: str, year: int):
        super().__init__(title)
        self.director = director
        self.year = year

    def show_movie(self, title, director, year):
        return f"Movie: {title} by {director} ({year})"
    
class Music(MediaElement):
    def __init__(self, title: str, singer: str, year: int):
        super().__init__(title)
        self.singer = singer
        self.year = year

    def show_music(self):
        return f"Music: {self.__title} by {self.singer} ({self.year})"
    
class Photo(MediaElement):
    def __init__(self, title: str, width: int, height: int, photographer: str):
        super().__init__(title)
        self.size = {"width": width, "height": height}
        self.photographer = photographer
    
    def show_photo(self):
        return f"Photo: {self.__title} by {self.photographer} ({self.size['width']}, {self.size['height']})"

class MediaCollection:
    def __init__(self):
        self.media_list = []

    def add_media(self, media: MediaElement):
        self.media_list.append(media)

    def get_media(self):
        return self.media_list

    def get_music(self):
        return [media for media in self.media_list if isinstance(media, Music)]
    
    def get_photo(self):
        return [media for media in self.media_list if isinstance(media, Photo)]

    def get_movie(self):
        return [media for media in self.media_list if isinstance(media, Movie)]

media_collection = MediaCollection()

movie = Movie("Titanic", "James Cameron", 1997)
movie.show_movie()
music = Music("Gangnam Style", "PSY", 2012)

photo = Photo("Sea", 800, 300, "Aivaz")

media_collection.add_media(movie)
media_collection.add_media(music)
media_collection.add_media(photo)

all_music = media_collection.get_music()
all_photos = media_collection.get_photo()
all_films = media_collection.get_movie()
