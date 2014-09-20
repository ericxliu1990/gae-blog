"""
The main google app engine file for rendering blog content
"""
import webapp2
from handler import *
from google.appengine.ext import db
from newpost import Newpost 
from blog import Blog
from signup import Signup, Welcome
		
class MainPage(Handler):
	"""the index page"""
	def render_blog(self):
		db_blogs = db.GqlQuery("SELECT * FROM Blog  ORDER BY created_time DESC")
		self.render("index.html", db_blogs = db_blogs)
	def get(self):
		#self.response.headers['Content-Type'] = 'text/plain'
		self.render_blog()

class Pages(Handler):
	"""pages of blogs"""
	def render_blog(self, page_id):
		a_blog = Blog.get_by_id(ids = int(page_id))
		self.render("pages.html", a_blog = a_blog)
	def get(self, page_id):
		#self.response.headers['Content-Type'] = 'text/plain'
		self.render_blog(page_id)

application = webapp2.WSGIApplication([
					('/', MainPage),
					("/newpost", Newpost),
					("/signup", Signup),
					 ('/welcome', Welcome),
					(r"/(\d+)", Pages),
					], debug=True)
