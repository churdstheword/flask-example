import os
import sqlite3
import click
from flask import current_app, g


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config['DATABASE'], detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def init_db():
    db = get_db()
    filename = os.path.join(os.path.dirname(__file__), 'schema.sql')
    with current_app.open_resource(filename) as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    db = get_db()
    db.execute(
        "INSERT INTO posts (title, content) VALUES (?, ?)",
        ('First Post', 'Content for the first post')
    )

    db.execute(
        "INSERT INTO posts (title, content) VALUES (?, ?)",
        ('Second Post', 'Content for the second post')
    )
    db.commit()
    close_db()
    click.echo('Initialized the database.')
