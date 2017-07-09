import media
import fresh_tomatoes as ft

movies = []
lord_of_the_rings = media.Movie("Lord of the Rings",
                                "Fantastic story about an almighty ring",
                                "https://upload.wikimedia.org/wikipedia/en/8/"
                                "87/Ringstrilogyposter.jpg",
                                "https://www.youtube.com/watch?v=V75dMMIW2B4")
pulp_fiction = media.Movie("Pulp Fiction",
                           "bla",
                           "https://upload.wikimedia.org/wikipedia/en/3/3b/"
                           "Pulp_Fiction_%281994%29_poster.jpg",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")
citizen = media.Movie("Law Abiding Citizen",
                      "Bla",
                      "https://upload.wikimedia.org/wikipedia/en/9/95/"
                      "Law_abiding_citizen_ver5.jpg",
                      "https://www.youtube.com/watch?v=LX6kVRsdXW4")
brice = media.Movie("Brice de Nice",
                    "Bla",
                    "https://upload.wikimedia.org/wikipedia/en/5/51/"
                    "Brice_de_Nice_poster.jpg",
                    "https://www.youtube.com/watch?v=uXBm7RTUizw")
movies = [lord_of_the_rings, pulp_fiction, citizen, brice]
ft.open_movies_page(movies)
