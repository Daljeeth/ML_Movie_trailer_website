import media
import fresh_tomatoes

#Creating instances of Movie class by passing parameters:
#Title,Storyline, poster image, trailer url, rating, duration, launch date
transformers = media.Movie("Transformers: The Last Knight",
                        "Quintessa brainwashes Optimus Prime and heads to Earth to search for an ancient staff. Cade, Bumblebee and the Autobots race against time to find it, while also escaping an anti-Transformers force.",
                        "https://images3.alphacoders.com/801/thumb-1920-801097.jpg", 
                        "https://www.youtube.com/watch?v=yCOvcyfRPRk",
                        "7.1/10",
                        "2h 24m", "23 June 2017")

walk_to_remember = media.Movie("A walk to remember",
                    "A Walk to Remember is a 2002 American coming-of-age romantic drama film directed by Adam Shankman and written by Karen Janszen, based on Nicholas Sparks' 1999 novel of the same name.",
                    "https://upload.wikimedia.org/wikipedia/en/d/dc/A_Walk_to_Remember_Poster.jpg",
                    "https://www.youtube.com/watch?v=i72wRvPw_ik",
                    "7.4/10",
                    "1h 42m","25 January 2002")

the_intern = media.Movie("The Intern",
                        "Seventy-year-old Ben Whittaker realises that retirement isn't an enjoyable experience. As a result, he decides to work as an intern at an online fashion store managed by an extremely sceptical boss.",
                        "https://upload.wikimedia.org/wikipedia/en/c/c9/The_Intern_Poster.jpg",
                        "https://www.youtube.com/watch?v=ZU3Xban0Y6A",
                        "7.1/10",
                        "2h 1m","25 September 2015")

captain_america = media.Movie("Captain America: The First Avenger",
                 "After Steve Rogers decides to volunteer as a guinea pig in an experiment, his weak body is fully enhanced. A secret Nazi organisation tries to exploit the technology and he must stand against them.",
                 "https://upload.wikimedia.org/wikipedia/en/3/37/Captain_America_The_First_Avenger_poster.jpg",
                 "https://www.youtube.com/watch?v=JerVrbLldXw",
                 "6.9/10",
                 "2h 4m","29 July 2011")

chef = media.Movie("Chef",
                 "After losing his job at a popular restaurant, Chef Carl Casper attempts to start afresh by fixing up a food truck. In the process, he ends up becoming closer to his family.",
                 "https://upload.wikimedia.org/wikipedia/en/b/b8/Chef_2014.jpg",
                 "https://www.youtube.com/watch?v=jYmtP2XPNc4",
                 "7.3/10",
                 "1h 55m", "8 May 2014")

batman = media.Movie("The Dark Knight Rises",
                 "Bane, an imposing terrorist, attacks Gotham City and disrupts its eight-year-long period of peace. This forces Bruce Wayne to come out of hiding and don the cape and cowl of Batman again.",
                 "http://t1.gstatic.com/images?q=tbn:ANd9GcQSGF8_VbDqKF0B_4IQ0NF87VMDSy7_MPKryawR-qLnSIPQwo5z",
                 "https://www.youtube.com/watch?v=J9DlV9qwtF0",
                 "8.4/10",
                 "2h 45m", "20 July 2012")

#creating a list of movies to pass to freshtomatoes
movies = [transformers, walk_to_remember, the_intern, captain_america, chef, batman]
fresh_tomatoes.open_movies_page(movies)

