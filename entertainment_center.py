import media
import fresh_tomatoes


godfather = media.Movie("The Godfather",
                        "The story spans the years from 1945 to 1955 and chronicles the fictional "
                        "Italian-American Corleone crime family. When organized crime family patriarch "
                        "Vito Corleone barely survives an attempt on his life, his youngest son, "
                        "Michael, steps in to take care of the would-be killers, launching a campaign "
                        "of bloody revenge.",
                        "https://image.tmdb.org/t/p/w600_and_h900_bestv2/d4KNaTrltq6bpkFS01pYtyXa09m.jpg",
                        "https://youtu.be/sY1S34973zA")
airplane = media.Movie("Airplane",
                       "Still craving for the love of his life, ex-Air Force pilot Ted Striker "
                       "follows Elaine onto the flight that she is working on as cabin crew. "
                       "Elaine doesn't want to be with Ted anymore, but when the crew and passengers "
                       "fall ill from food poisoning, Ted might be the only one who can save them.",
                       "https://image.tmdb.org/t/p/w600_and_h900_bestv2/b4sAWNIbfXw4WTdc1wiVRBk2Vko.jpg",
                       "https://youtu.be/si3E43eaRac")
birdman = media.Movie("Birdman",
                      "A fading actor best known for his portrayal of a popular superhero attempts to mount a "
                      "comeback by appearing in a Broadway play. As opening night approaches, his attempts to become "
                      "more altruistic, rebuild his career, and reconnect with friends and family prove more difficult "
                      "than expected.",
                      "https://image.tmdb.org/t/p/w600_and_h900_bestv2/rSZs93P0LLxqlVEbI001UKoeCQC.jpg",
                      "https://youtu.be/2bqh-UCY6Zg")
up = media.Movie("Up", "After a lifetime of dreaming of traveling the world, 78-year-old homebody Carl flies away on an"
                       " unbelievable adventure with Russell, an 8-year-old Wilderness Explorer, unexpectedly in tow."
                       " Together, the unlikely pair embarks on a thrilling odyssey full of jungle beasts and"
                       " rough terrain.",
                 "https://image.tmdb.org/t/p/w600_and_h900_bestv2/gfFqBcoFW8uczyl2ytVmVmUg82k.jpg",
                 "https://youtu.be/YOOIK0baLvM")
wonka = media.Movie("Willy Wonka & the Chocolate Factory",
                    "Eccentric candy man Willy Wonka prompts a worldwide frenzy when he announces that golden tickets"
                    " hidden inside five of his delicious candy bars will admit their lucky holders into his top-secret"
                    " confectionary. But does Wonka have an agenda hidden amid a world of Oompa Loompas and"
                    " chocolate rivers?",
                    "https://image.tmdb.org/t/p/w600_and_h900_bestv2/b94qXd1FcIwgzv0NYMUe2bjrzJR.jpg",
                    "https://youtu.be/Y_Pyp0liDeE")
perfecta = media.Movie("La dictadura perfecta",
                       "La dictadura perfecta proyecta una lamentable realidad y deja entrever que, cuando se"
                       " trata del poder, hasta Nicolas Maquiavelo se queda corto.",
                       "https://image.tmdb.org/t/p/w600_and_h900_bestv2/m0Our7wh91YieK86piDmmiOWkeR.jpg",
                       "https://youtu.be/ZriH9uEDgsI")

movies = [godfather, airplane, birdman, up, wonka, perfecta]
fresh_tomatoes.open_movies_page(movies)
