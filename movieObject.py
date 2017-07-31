import fresh_tomatoes


# A movie object has four parameters:
# movie_title, year, poster_image, trailer_youtube
class Movie():
    def __init__(self, movie_title, year, poster_image, trailer_youtube):
        self.title = movie_title
        self.release_year = year
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        print(self.trailer_youtube_url)

# Declare four instances of Movie, passing
# movie_title, year, poster_image, and trailer_youtube
# (in that order)
casinoroyale = Movie("Casino Royale", 2006, "https://www.cinematerial.com/media/posters/sm/bd/bdpsvoir.jpg?v=1456761712", "https://www.youtube.com/watch?v=36mnx8dBbGE")
butterflies = Movie("Flight of the Butterflies", 2012, "http://www.impawards.com/intl/canada/2012/posters/flight_of_the_butterflies.jpg", "https://www.youtube.com/watch?v=Nww3L5b0wno")
pi = Movie("Pi", 1998, "http://www.impawards.com/1998/posters/pi_ver2.jpg", "https://www.youtube.com/watch?v=oQ1sZSCz47w")
janegotagun = Movie("Jane Got a Gun", 2015, "http://dl9fvu4r30qs1.cloudfront.net/4e/e7/a30a232f4b63a4f59b8252764bfc/jane-got-a-gun-poster.jpg", "https://www.youtube.com/watch?v=QniNBM1gBVk")

# This is a List of the four movies
listofmovies = [casinoroyale, butterflies, pi, janegotagun]

# Generate output.
# I like having the terminal tell me where it is in its process.
print("Calling fresh_tomatoes now.")
fresh_tomatoes.open_movies_page(listofmovies)
print("fresh_tomatoes has been executed")
