"""
The main google app engine file for rendering blog content
"""
import webapp2
from handler import *;

class MainPage(Handler):
	"""the index page"""
	def render_blog(self):
		self.render("blog.html")
	def get(self):
		#self.response.headers['Content-Type'] = 'text/plain'
		self.render_blog()

POSTNEW_ERROR = "You need both subject and blog content."
class Newpost(Handler):
	"""the page for posting a new blog"""
	def render_newpost(self, subject = "", blog_content = "", error = ""):
		self.render("newpost.html", subject = subject, 
					blog_content = blog_content, 
					error = error)

	def get(self):
		self.render_newpost()

	def post(self):
		subject = self.request.get("subject")
		blog_content = self.request.get("blog_content")
		if subject and blog_content:
			self.redirect('/')
		else:
			self.render_newpost(subject = subject, 
					blog_content = blog_content, 
					error = POSTNEW_ERROR)
		

application = webapp2.WSGIApplication([
					('/', MainPage),
					("/newpost", Newpost)
					], debug=True)
