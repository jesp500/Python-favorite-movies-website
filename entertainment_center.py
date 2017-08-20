import media
import fresh_tomatoes

# Creating instances of the class Movie for each movie
# title, poster_image_url, photo_movie, trailer_youtube_url, synopsis, slogan
# Create instance of Movie class for Braveheart
braveheart_synopsis = '''
William Wallace is a Scottish rebel who leads an uprising against the cruel
English ruler Edward the Longshanks, who wishes to inherit the crown of
Scotland for himself. When he was a young boy, William Wallace's father and
brother, along with many others, lost their lives trying to free Scotland.
Once he loses another of his loved ones, William Wallace begins his long quest
to make Scotland free once and for all, along with the assistance of Robert
the Bruce.
'''
braveheart_slogan = '''
When his secret bride is executed for assaulting an English soldier who tried
to rape her, Sir William Wallace begins a revolt against King Edward I of
England.
'''
braveheart = media.Movie(
    'Braveheart',
    'https://images-na.ssl-images-amazon.com/images/M/MV5BODg4NzA0MTktOGU5ZS00ODlkLWE3ZmQtYjAzNjNmM2E3NmEzL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_SX675_AL_.jpg',  # noqa
    'http://images.mentalfloss.com/sites/default/files/411363.jpg',
    '1cnoM8EiGGU',
    braveheart_synopsis,
    braveheart_slogan
)

# Create instance of Movie class for Gladiator
gladiator_synopsis = '''
Maximus is a powerful Roman general, loved by the people and the aging Emperor
, Marcus Aurelius. Before his death, the Emperor chooses Maximus to be his
heir over his own son, Commodus, and a power struggle leaves Maximus and his
family condemned to death. The powerful general is unable to save his family,
and his loss of will allows him to get captured and put into the Gladiator
games until he dies. The only desire that fuels him now is the chance to rise
to the top so that he will be able to look into the eyes of the man who will
feel his revenge.
'''
gladiator_slogan = '''
When a Roman general is betrayed and his family murdered by an emperor's
corrupt son, he comes to Rome as a gladiator to seek revenge.
'''
gladiator = media.Movie(
    'Gladiator',
    'https://images-na.ssl-images-amazon.com/images/M/MV5BMDliMmNhNDEtODUyOS00MjNlLTgxODEtN2U3NzIxMGVkZTA1L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,675,1000_AL_.jpg',  # noqa
    'http://www.factinate.com/wp-content/uploads/2017/02/Gladiator-wallpaper.jpg',  # noqa
    'owK1qxDselE',
    gladiator_synopsis,
    gladiator_slogan
)

# Create instance of Movie class for Kill Bill
kill_bill_synopsis = '''
The lead character, called 'The Bride,' was a member of the Deadly Viper
Assassination Squad, led by her lover 'Bill.' Upon realizing she was pregnant
with Bill's child, 'The Bride' decided to escape her life as a killer. She
fled to Texas, met a young man, who, on the day of their wedding rehearsal was
gunned down by an angry and jealous Bill (with the assistance of the Deadly
Viper Assassination Squad). Four years later, 'The Bride' wakes from a coma,
and discovers her baby is gone. She, then, decides to seek revenge upon the
five people who destroyed her life and killed her baby. The saga of Kill Bill
Volume I begins.
'''
kill_bill_slogan = '''
The Bride wakens from a four-year coma. The child she carried in her womb is
gone. Now she must wreak vengeance on the team of assassins who betrayed her
- a team she was once part of.
'''
kill_bill = media.Movie(
    'Kill Bill',
    'https://images-na.ssl-images-amazon.com/images/M/MV5BYTczMGFiOWItMjA3Mi00YTU5LWIwMDgtYTEzNjRkNDkwMTE2XkEyXkFqcGdeQXVyNzQ1ODk3MTQ@._V1_.jpg',  # noqa
    'https://i.ytimg.com/vi/ot6C1ZKyiME/maxresdefault.jpg',
    '7kSuas6mRpk',
    kill_bill_synopsis,
    kill_bill_slogan
)

movies = [
    braveheart,
    gladiator,
    kill_bill
]
fresh_tomatoes.open_movies_page(movies)
