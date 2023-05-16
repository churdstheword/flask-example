from app.posts import bp
from flask import render_template, request, url_for, flash, redirect, g
from app.db import init_app
from app.models.posts import Posts as PostModel


@bp.route('/<int:post_id>')
def post(post_id):
    model = PostModel(g.db)
    posts = model.getPost(post_id)
    if posts is None:
        return render_template('404.html'), 404
    return render_template('post.html', post=posts)


@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            model = PostModel(g.db)
            model.insertPost(title, content)
            return redirect(url_for('main.index'))

    return render_template('create.html')


@bp.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    model = PostModel(g.db)
    post = model.getPost(id)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title:
            flash('Title is required!')
        else:
            model.updatePost(title, content, id)
            return redirect(url_for('main.index'))

    return render_template('edit.html', post=post)


@bp.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    model = PostModel(g.db)
    post = model.getPost(id)
    model.deletePost(id)
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('main.index'))