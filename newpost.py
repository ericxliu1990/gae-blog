"""

"""
import time
from handler import *
from google.appengine.ext import db
from blog import Blog

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
