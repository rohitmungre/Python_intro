import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc"
                        )
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8"
                     )
#print(avatar.storyline)
#avatar.show_trailer()

shutter_island = media.Movie("Shutter Island",
                     "Story of a psychiatrist - doctor on an island for a case study",
                     "https://upload.wikimedia.org/wikipedia/en/7/76/Shutterislandposter.jpg",
                     "https://www.youtube.com/watch?v=5iaYLCiq5RM"
                     )

lotr = media.Movie("Lord of the Rings",
                     "Epic saga of how a tiny hobbit saves the middle earth from evil forces",
                     "https://upload.wikimedia.org/wikipedia/en/8/87/Ringstrilogyposter.jpg",
                     "https://www.youtube.com/watch?v=V75dMMIW2B4"
                     )

mask = media.Movie("The Mask",
                     "Tale of the magical mask that gives superpowers to this ordinary man",
                     "https://upload.wikimedia.org/wikipedia/en/4/4b/The_Mask_%28film%29_poster.jpg",
                     "https://www.youtube.com/watch?v=hOqVRwGVUkA"
                     )

dark_knight = media.Movie("The Dark Knight",
                     "A mindboggling Story of batman and joker",
                     "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                     "https://www.youtube.com/watch?v=yQ5U8suTUw0"
                     )

movies = [toy_story, avatar, shutter_island, lotr, mask, dark_knight]
print(media.Movie.VALID_RATINGS)
#fresh_tomatoes.open_movies_page(movies)
