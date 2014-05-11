import webapp2

main_html= """
	<form method = "post" action = "/testfrom"> 
		<input name = "q">
		<input type = "submit">
	</form>
	"""

class MainPage(webapp2.RequestHandler):
  def get(self):
	#self.response.headers['Content-Type'] = 'text/html'
	self.response.out.write(main_html)

class TestHandler(webapp2.RequestHandler):
  def post(self):
	q = self.request.get("q")
	self.response.write(q)
	
	#self.response.headers['Content-Type'] = 'text/plain'
	#self.response.out.write(self.request)

app = webapp2.WSGIApplication([('/', MainPage),
								('/testfrom', TestHandler)], 
								debug = True)
