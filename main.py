"""
The main google app engine file for rendering blog content
"""
import time
import webapp2
from handler import *;
from google.appengine.ext import db

class Blog(db.Model):
	"""a class represents a blog"""
	subject = db.StringProperty(required = True)
	blog_content = db.TextProperty(required = True)
	created_time = db.DateTimeProperty(auto_now_add = True)
		

class MainPage(Handler):
	"""the index page"""
	def render_blog(self):
		db_blogs = db.GqlQuery("SELECT * FROM Blog  ORDER BY created_time DESC")
		self.render("index.html", db_blogs = db_blogs)
	def get(self):
		#self.response.headers['Content-Type'] = 'text/plain'
		self.render_blog()

POSTNEW_ERROR = "You need both the subject and the blog content."
class Newpost(Handler):
	"""the page for posting a new blog"""
	def render_newpost(self, subject = "", blog_content = "", error = ""):
		self.render("newpost.html", subject = subject, 
					content = blog_content, 
					error = error)

	def get(self):
		self.render_newpost()
	def post(self):
		subject = self.request.get("subject")
		blog_content = self.request.get("content")
		if subject and blog_content:
			a_blog = Blog(subject = subject, blog_content = blog_content)
			a_blog.put()
			#db.allocate_ids(a_blog.key(), 1000)
			time.sleep(1)
			self.redirect('/' + str(a_blog.key().id()))
		else:
			self.render_newpost(subject = subject, 
					blog_content = blog_content, 
					error = POSTNEW_ERROR)

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
					(r"/(\d+)", Pages)
					], debug=True)
