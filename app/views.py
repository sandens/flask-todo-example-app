from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_bootstrap import __version__ as FLASK_BOOTSTRAP_VERSION
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
import logging 
from .nav import nav
from .forms import TodoForm
from .models import Todo, db
from flask import current_app as app


frontend = Blueprint("frontend",__name__)
logger = logging.getLogger()

# We're adding a navbar as well through flask-navbar. In our example, the
# navbar has an usual amount of Link-Elements, more commonly you will have a
# lot more View instances.
# We're adding a navbar as well through flask-navbar. In our example, the
# navbar has an usual amount of Link-Elements, more commonly you will have a
# lot more View instances.
nav.register_element('frontend_top', Navbar(
    View('Todos Example', '.index'),
    Subgroup(
        'Docs',
        Link('Flask-Bootstrap', 'http://pythonhosted.org/Flask-Bootstrap'),
        Link('Flask-AppConfig', 'https://github.com/mbr/flask-appconfig'),
        Link('Flask-Debug', 'https://github.com/mbr/flask-debug'),
        Separator(),
        Text('Bootstrap'),
        Link('Getting started', 'http://getbootstrap.com/getting-started/'),
        Link('CSS', 'http://getbootstrap.com/css/'),
        Link('Components', 'http://getbootstrap.com/components/'),
        Link('Javascript', 'http://getbootstrap.com/javascript/'),
        Link('Customize', 'http://getbootstrap.com/customize/'), ),
    Text('Using Flask-Bootstrap {}'.format(FLASK_BOOTSTRAP_VERSION)), ))


@frontend.route('/', methods=('GET', 'POST'))
def index():
    form = TodoForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        todo = Todo(name=form.name.data)
    
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('frontend.index'))

    all_todos = Todo.query.all()
    return render_template('index.html', form=TodoForm(), todos=all_todos)
    
   
@frontend.route("/add")
def add_todo():
    pass

@frontend.route("/remove", methods=["POST"])
def remove_todo():
    form = TodoForm(request.form)
    
    if request.method == 'POST':
        todo_id = request.form.get("todo_id")
        logger.info(f"Delete this todo: {todo_id}")

        #for specific value
        db.session.query(Todo).filter(Todo.id==todo_id).delete()
        db.session.commit()
        return redirect(url_for('frontend.index'))
