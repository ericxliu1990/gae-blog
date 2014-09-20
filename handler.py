"""
A general handler class of render jinja2 pages
"""
import os
import webapp2, jinja2

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
	autoescape = True)

class Handler(webapp2.RequestHandler):
	"""
	General hander class for rendering contents to GAE
	"""
	def write(self, *args, **kwargs):
		self.response.out.write(*args, **kwargs)

	def render_string(self, template, **params):
		template = jinja_env.get_template(template)
		return template.render(params)

	def render(self, template, **kwargs):
		self.write(self.render_string(template, **kwargs))