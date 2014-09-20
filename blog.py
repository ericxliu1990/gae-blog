"""
"""
from google.appengine.ext import db
class Blog(db.Model):
	"""a class represents a blog"""
	subject = db.StringProperty(required = True)
	blog_content = db.TextProperty(required = True)
	created_time = db.DateTimeProperty(auto_now_add = True)