import sys
import unittest

from flask.cli import FlaskGroup
import coverage

from project import create_app, db
from project.api.models import User


COV = coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
        'projects/tests/*',
        'projects/config.py'
    ]
)
COV.start()

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command('test')
def test():
    """ Runs tests without code coverage """
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    
    if result.wasSuccessful():
        return 0

    sys.exit(result)

@cli.command('seed_db')
def seed_db():
    """ Seeds the database """
    db.session.add(User(username='John Doe', email='johndoe@email.com'))
    db.session.add(User(username='Jane Doe', email='janedoe@email.com'))
    db.session.commit()

@cli.command('cov')
def cov():
    """ Run unit tests with code coverage """
    tests = unittest.TestLoader().discover('project/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    if result.wasSuccessful():
        COV.stop()
        COV.start()
        print('Coverage Summary:')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0

    sys.exit(result)


if __name__ == '__main__':
    cli()
