from flask import render_template, g
from app.main import bp
from app.models.posts import Posts as PostModel

@bp.route('/')
def index():
    model = PostModel(g.db)
    posts = model.getPosts()
    return render_template('index.html', posts=posts)
