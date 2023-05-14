from quiz_functions import store_score, movie_score, cartoon_score
# Defining the function
def test_store_score():
    # calls store_score function with the arguments "Brandon", 25 and movie
    store_score("Brandon", 25, "movie")
    # Assert valve "Brandon" to the Movie_score dictionary
    assert movie_score["Brandon"] == 25
    # Calls store_score function with arguments Cartoon, Bob and 3
    store_score("Bob", 3, "cartoon")
    # Assert Bob value to cartoon score dictionary
    assert cartoon_score["Bob"] == 3

# platform linux -- Python 3.10.6, pytest-7.3.1, pluggy-1.0.0
# rootdir: /mnt/c/Users/ninja/Desktop/BrandonPowell_T1A3
# collected 5 items

                                                                                                                                                                            
# test_read_files.py ..     80%                                                                                                                                                                               [ 80%]
# test_store_score.py .     100%