"""
The main google app engine file for rendering blog content
"""

import webapp2
from handler import *;

class MainPage(Handler):
	def render_blog(self):
		self.render("blog.html")
	def get(self):
		#self.response.headers['Content-Type'] = 'text/plain'
		self.render_blog()

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
