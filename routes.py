"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime
import prim_form

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/prim')
@view('prim')
def prim():
    """Renders the contact page."""
    return dict(
        title='Prim',
        answer="",
        message='Prim`s algorithm',
        year=datetime.now().year
    )

@route('/authors')
@view('authors')
def authors():
    """Renders the contact page."""
    return dict(
        title='Authors',
        message='',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )
