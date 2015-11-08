import webbrowser
# call the mobie class
class Movie():
# init the class to get the value self is the same as this in other languages
	def __init__(self, movie_title,movie_story,movie_image,movie_trailer):
		self.title = movie_title
		self.storyline = movie_story
		self.poster_image_url = movie_image
		self.trailer_youtube_url = movie_trailer
		
    # function to call the youtube URL
	def this_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
	
