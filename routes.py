"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime
import regression_form

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/regression')
@view('regression')
def regression():
    """Renders the contact page."""
    return dict(
        title='Regression',
        LeanerModel='',
        linCorr="",
        linDeter="",
        QuadraticModel="",
        QuadraticCorr="", 
        QuadraticDeter="",
        conclusion="",
        row=0,
        x=[],
        y=[],
        message='Regression`s algorithm',
        year=datetime.now().year
    )

@route('/task2')
@view('task2')
def task2():
    """Renders the contact page."""
    return dict(
        title='Task 2',
        answer="",
        message='Sofya',
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
