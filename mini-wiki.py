import codecs, markdown, os, re
from functools import wraps
from flask import Flask, g, render_template, request, Markup, Response, abort, url_for, redirect, session
from jinja2.environment import Environment 

app = Flask(__name__)

try:
	app.config.from_object('settings_local')
except ImportError:
	app.config.from_object('settings')


users = app.config['USERS']
auth_password = app.config['PASSWORD']
app.secret_key = app.config['SECRET_KEY']

@app.before_request
def before_request():
    pass

@app.teardown_request
def teardown_request(exception):
	pass

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        if 'l' not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/login", methods=["POST", "GET"])
def login():
	if request.method == "GET":
		redir_url = url_for('index')
		if request.args.get('next'):
			redir_url = request.args.get('next')
		return render_template('login.html', redir_url=redir_url, loggedIn=False)

	if request.method == "POST":
		redir_url = url_for('index')
		if request.form.get("redir_url"):
			redir_url = str(request.form.get("redir_url"))
		username = str(request.form.get("username"))
		password = str(request.form.get("password"))

		if username in users and password == auth_password:
			session['l'] = True
			return redirect(redir_url)
		else:
			return render_template('login.html', loggedIn=False, badLogin=True)

@app.route("/logout")
def logout():
	session.clear()
	return redirect(url_for('index'))

@app.route("/")
@login_required
def index():
	return render_template('index.html', loggedIn=True)

@app.route("/info")
@login_required
def info():	
	item = request.args.get('i')
	path = request.args.get("p")

	#sanitize params
	regex = re.compile("\W+")
	nameCheck = regex.findall(item)
	roleCheck  = regex.findall(path)
	print path + item

	nameLen  = len(nameCheck)
	roleLen  = len(roleCheck)

	if(nameLen  == 0 & roleLen == 0):
		#path = path.lower()
		try:
			f = codecs.open('%s/%s.md' % (path, item), 'r', encoding='utf-8')
			content = f.read()
			print '%s/%s.md' % (path, item)
			f.close()
			content = Markup(markdown.markdown(content)) #converts markup to html
			return Response(content, mimetype='text/html')
		except IOError:
			return abort(404)
	else:
		return abort(403)


@app.route("/analyst")
@login_required
def analyst():
	return get_template("analyst")

@app.route("/programmer")
@login_required
def programmer():
	return get_template("programmer")

@app.route("/communications")
@login_required
def communications():
	return get_template("communications")

@app.route("/intern")
@login_required
def intern():
	return get_template("intern")

#Utility Funcs:
def get_template(role):
	role_menu_items = get_menu_items("content/" + role)
	for_all_menu_items = get_menu_items("content/for_all")
	greeting = get_role_greeting(role)

	return render_template('role.html', role=role, greeting = greeting,
			role_menu_items = role_menu_items, for_all_menu_items = for_all_menu_items, loggedIn=True)

#retireves a greeting message specific to the role of the user
def get_role_greeting(role):
	try:
		f = codecs.open('content/role_greetings/%s_greeting.md' % (role), 'r', encoding='utf-8')
		greeting = f.read()
		f.close()
		return Markup(markdown.markdown(greeting))
	except IOError:
		return ""

def get_menu_items(path):	
	items = get_dir_items(path)
	return items


#get_dir_tems() and organize_dir_items() become recursive methods for each ecounter with a child directory within its parent directory


#creates a list of files or directories (these will be displayed at menu options a user can select to view)
def get_dir_items(path):
	dir_items = os.listdir(path)
	items = []

	for i in dir_items:
		if '.txt' not in i:
			items.append(organize_dir_item(path, i))
		
	return items

#removes underscores and file extension, then adds the original name cleaned name and path to a dict
def organize_dir_item(path, item):
	orig_name = item.replace(".md", "")
	cleaned_name = orig_name.replace("_", " ")
	item_is_dir = os.path.isdir(os.path.join(path, item))
	dir_dict = {'orig':orig_name, 'cleaned':cleaned_name, 'path': path}	

	#if an item is a subdirectory, its dict will contain the original name, cleaned name, path, and the files within  
	if item_is_dir:
		dir_dict['files'] = get_dir_items(path + "/" + item)
		return dir_dict
	else: 
		return dir_dict		
#END Utils


if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'], host="0.0.0.0")

