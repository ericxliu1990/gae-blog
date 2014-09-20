"""

"""
import time, re, hmac
from handler import *

username_error = """
That's not a valid username.
"""
password_error  = """
That wasn't a valid password.
"""
verfiy_password_error = """
Your passwords didn't match.
"""
email_error = """
That's not a valid email.
"""
SECRET = "eric"
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

def _hash_str(original_str):
	""""""
	return hmac.new(SECRET, original_str).hexdigest()

def _make_secure_val(original_str):
	""""""
	return "%s|%s" % (original_str, _hash_str(original_str))

def _check_secure_val(to_check_str):
	try:
		original_str, hash_val = to_check_str.split("|")
	except :
		return "0"
	if _hash_str(original_str) == hash_val:
		return original_str
	else:
		return None

def is_username_valid(username):
	""""""
	return username and USER_RE.match(username)

def is_password_valid(password):
	""""""
	return password and PASSWORD_RE.match(password)

def is_email_valid(email):
	if email == "":
		return True
	else:
		return EMAIL_RE.match(email)

class Signup(Handler):
	"""the page for posting a new blog"""
	def render_signup(self, username = "", 
				password = "", 
				verfiy = "",
				email = "",
				username_error = "",
				password_error = "",
				verfiy_password_error = "",
				email_error = ""):
		self.render("signup.html", username = username, 
				password = password, 
				verfiy = verfiy,
				email = email,
				username_error = username_error,
				password_error = password_error,
				verfiy_password_error = verfiy_password_error,
				email_error = email_error)

	def get(self):
		self.render_signup()

	def post(self):
		username = self.request.get("username")
		password = self.request.get("password")
		verfiy = self.request.get("verfiy")
		email = self.request.get("email")
		#self.response.write(self.request)
		error_flag  = False 
		if not is_username_valid(username):
			self.render_signup(username_error = username_error)
			error_flag = True
		if not is_password_valid(password):
			self.render_signup(username = username, 
				email =  email, 
				password_error = password_error)
			error_flag = True
		if not verfiy == password:
			self.render_signup(username = username, 
				email = email, 
				verfiy_password_error = verfiy_password_error)
			error_flag = True
		if not is_email_valid(email):
			self.render_signup(username = username, 
				email_error = email_error)
			error_flag = True
		if not error_flag:
			username_cookie = _make_secure_val(str(username))
			self.response.headers.add_header("Set-Cookie", "name=%s" % username_cookie)
			self.redirect("/welcome")

class  Welcome(Handler):
	""""""
	def get(self):
		username_cookie = self.request.cookies.get('name')
		if username_cookie:
			username_cookie_check = _check_secure_val(username_cookie)
			if username_cookie_check:
				username  = str(username_cookie_check)
				if is_username_valid(username):
					self.render("welcome.html", username = username)
			else:
				self.redirect("/signup")