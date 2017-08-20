import webbrowser
import os

# holds the first part of the future html file
# it won't be modified in any way
first_bunch_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>My favorite movies</title>
<link rel="stylesheet"
href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
integrity=
"sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u"
crossorigin="anonymous">
<script src=
"https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js">
</script>
<script
src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"
integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa"
crossorigin="anonymous"></script>
<style>
body {
background-image: url(https://theamazingworldofpsychiatry.files.wordpress.com/2010/09/istock_000009307982large.jpg);
background-size: 100% 100%;
background-attachment: fixed;
}
#main {
background: white; /* For browsers that do not support gradients */
background: -webkit-linear-gradient(#D3D3D3, white); /* For Safari */
background: -o-linear-gradient(#D3D3D3, white); /* For Opera  */
background: -moz-linear-gradient(#D3D3D3, white); /* For Firefox  */
background: linear-gradient(#D3D3D3, white); /* Standard syntax */
}
#synopsis > div {
margin-top: 10px;
border-bottom: 2px solid black;
text-align: justify;
}
footer {
color: white;
background: #34495e;
}
</style>
<script>
jQuery(document).ready(function($){
$('.carousel-inner > div').first().addClass('active');
function autoPlayVideo(currentObject, vcode){
currentObject.find('.embed-responsive')
.html('<iframe src="https://www.youtube.com/embed/' +
vcode + '?autoplay=1"></iframe>');
}
'''
# holds the second part of the html file. It will be iterated as many times
# as movies contained in the list containing objects created
# from the class Movie
second_bunch_content = '''
//%s
$('#%s-trailer').on('shown.bs.modal', function () {
autoPlayVideo($(this),'%s');
});
$("#%s-trailer").on('hidden.bs.modal', function (e) {
$("#%s-trailer .embed-responsive").html("");
});
'''
# holds the third part of the html, it won't be modified
third_bunch_content = '''
});
</script>
</head>
<body>
<div class="container" id="main">
<nav class="navbar navbar-default">
<div class="container">
<!-- Brand and toggle get grouped for better mobile display -->
<div class="navbar-header">
<button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
data-target="#menu-elements" aria-expanded="false">
<span class="sr-only">Toggle navigation</span>
<span class="icon-bar"></span>
<span class="icon-bar"></span>
<span class="icon-bar"></span>
</button>
<a class="navbar-brand" href="#">
Movies
</a>
</div>
<!-- Collect the nav links, forms, and other content for toggling -->
<div class="collapse navbar-collapse" id="menu-elements">
<ul class="nav navbar-nav">
<li class="active">
<a href="#">My favorite movies <span class="sr-only">(current)</span></a>
</li>
</ul>
</div><!-- /.navbar-collapse -->
</div><!-- /.container -->
</nav>
<!-- Bootstrap carousel -->
<h1>My favorite movies</h1>
<div id="displaying-movies" class="carousel slide" data-ride="carousel">
<!-- Indicators -->
<ol class="carousel-indicators">
<li data-target="#displaying-movies" data-slide-to="0" class="active"></li>
<li data-target="#displaying-movies" data-slide-to="1"></li>
<li data-target="#displaying-movies" data-slide-to="2"></li>
</ol>

<!-- Wrapper for slides -->
<div class="carousel-inner">
'''
# holds the fourth part of the html. It will be put through
# the an iteration to substitute the %s with the appropriate
# information as many times as movies contained in the list containing objects
# created from the class Movie
fourth_bunch_content = '''
<div class="item">
<img src="%s" alt="%s">
<div class="carousel-caption">
<h3>%s</h3>
<p>%s</p>
</div>
</div>
'''
# holds the fifth part of the html. It won't be modified
fifth_bunch_content = '''
</div>

<!-- Left and right controls -->
<a class="left carousel-control" href="#displaying-movies" data-slide="prev">
<span class="glyphicon glyphicon-chevron-left"></span>
<span class="sr-only">Previous</span>
</a>
<a class="right carousel-control" href="#displaying-movies" data-slide="next">
<span class="glyphicon glyphicon-chevron-right"></span>
<span class="sr-only">Next</span>
</a>
</div>
<div class="row" id="synopsis">
'''
# holds the sixth part of the html. It will be put through
# an iteration as many times as movies in the list containing object
# created from the class Movie
sixth_bunch_content = '''
<div class="col-md-4">
<h2>%s</h2>
<img src="%s" alt="%s" class="img-responsive center-block img-thumbnail" />

<p>%s</p>
<button type="button" class="btn btn-default btn-lg" data-toggle="modal"
data-target="#%s-trailer">Watch Trailer</button>
</div>
'''
# holds the seventh part of the html. It won't be modified
seventh_bunch_content = '''
</div>
</div>
<footer class="container">
<p class="lead">All the information used in this page is courtesy of
<a href="http://www.imdb.com">imdb</a>.</p>
</footer>
'''
# holds the eighth part of the html. It will be put through an
# iteration as many times as movies in the list containing objects
# created from the class Movie
eighth_bunch_content = '''
<!-- Modal %s -->
<div id="%s-trailer" class="modal fade" role="dialog">
<div class="modal-dialog">
<!-- Modal content-->
<div class="modal-content">
<div class="modal-header">
<button type="button" class="close" data-dismiss="modal">&times;</button>
</div>
<div class="embed-responsive embed-responsive-4by3">
</div>
<div class="modal-footer">
<button type="button" class="btn btn-default" data-dismiss="modal">Close
</button>
</div>
</div>
</div>
</div>
'''
# last part of the html. It won't be modified
ninth_bunch_content = '''
</body>
</html>
'''


def first_iteration(bunched_movies):
    # Go over the movies list, and get their different properties
    # into the second_bunch_content variable.
    divs_together = ''
    for movie in bunched_movies:
        tuple_variable = (
            movie.title,
            movie.title.lower().replace(' ', '-'),
            movie.trailer_youtube_url,
            movie.title.lower().replace(' ', '-'),
            movie.title.lower().replace(' ', '-')
        )
        divs_together += second_bunch_content % tuple_variable
    return divs_together


def second_iteration(bunched_movies):
    # Go over the movies list, and get their different properties
    # into the fourth_bunch_content variable.
    divs_together = ''
    for movie in bunched_movies:
        divs_together += fourth_bunch_content % (
            movie.photo_movie,
            movie.title,
            movie.title,
            movie.slogan
        )
    return divs_together


def third_iteration(bunched_movies):
    # Go over the movies list, and get their different properties into
    # the sixth_bunch_content variable.
    divs_together = ''
    for movie in bunched_movies:
        tuple_variable = (
            movie.title,
            movie.poster_image_url,
            movie.title,
            movie.synopsis,
            movie.title.lower().replace(' ', '-')
        )
        divs_together += sixth_bunch_content % tuple_variable
    return divs_together


def fourth_iteration(bunched_movies):
    # Go over the movies list, and get their different properties into
    # the eighth_bunch_content variable.
    divs_together = ''
    for movie in bunched_movies:
        tuple_variable = (
            movie.title,
            movie.title.lower().replace(' ', '-')
        )
        divs_together += eighth_bunch_content % tuple_variable
    return divs_together


def open_movies_page(bunched_movies):
    # Call the first_iteration function, second_iteration function,
    # third_iteration function and fourth_iteration function to get
    # all of the movies divs and put them into the html content, then
    # create an html file and put the html content into it, and finally
    # open it in the default browser
    second_segment = first_iteration(bunched_movies)
    fourth_segment = second_iteration(bunched_movies)
    sixth_segment = third_iteration(bunched_movies)
    eighth_segment = fourth_iteration(bunched_movies)
    html = first_bunch_content + second_segment + third_bunch_content + \
        fourth_segment + fifth_bunch_content + sixth_segment + \
        seventh_bunch_content + eighth_segment + ninth_bunch_content
    html_document = open('fresh_tomatoes.html', 'w')
    html_document.write(html)
    html_document.close()
    path = os.path.abspath(html_document.name)
    webbrowser.open('file://' + path, new=2)  # open in a new tab, if possible
