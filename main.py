import bottle_session
import bottle

# need to install redis for this.

# https://pypi.org/project/bottle-session/#description
# https://github.com/linsomniac/bottlesession/blob/master/app

app = bottle.app()
plugin = bottle_session.SessionPlugin(cookie_lifetime=600)
app.install(plugin)

@bottle.route('/')
def index(session):
    user_name = session.get('name')
    if user_name is not None:
    	return "Hello, %s"%user_name
    else:
    	return bottle.redirect('/login')


#@bottle.route('/register')
#def register(email,user,passw):
#	user = str(request.GET.get('user_id'))
#	email = str(request.GET.get('email'))
#	passw = str(request.GET.get('passw'))
#	# store somewhere (may be SQLITE)

@bottle.route('/login')
def login():
    return '''
        <form action="/login" method="post">
            username: <input name="username" type="text" />
            password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
           '''

@bottle.route('/login', method='POST') 
def do_login(session):
    username = bottle.request.forms.get('username')
    password = bottle.request.forms.get('password')
    # Authenticate against LDAP or any other AUTH 
    if username==username and password==password:
    	session['name']=username
    	return "<p>You have logged in successfuly</p>"
    else:
        return "<p>Your log in attempt has failed</p>"


# This function should get POST req \
# After validation of user need to set session as session['name']=user_name \
# If validation fail need to redirect login page again return bottle.redirect('/someehere')

@bottle.route('/set/:user_name')
def set_name(session,user_name=None):
    if user_name is not None:
        session['name']=user_name
        return "I recognize you now."
    else:
        return "What was that?"


bottle.debug(True)
bottle.run(app=app,host='localhost',port=8888)
