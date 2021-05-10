from application import app, db
from application.models import Tasks
from flask import render_template, url_for
from flask import redirect, request
from application.forms import AddTask

@app.route('/', methods=['GET','POST'])

@app.route('/home', methods=['GET','POST'])
def home():
    all_tasks = Tasks.query.all()
    print(all_tasks)
    return render_template('home.html',  title="Home", all_tasks=all_tasks)

@app.route('/about', methods=['GET','POST'])
def about():
    
    return render_template("about.html", title="About")

@app.route('/addtask', methods=['GET','POST'])
def addtask():
    form = AddTask()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_task = Tasks(
                title = form.title.data,
                description = form.description.data
            )

        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template('add_task.html', title='Add a Task', form=form)
    

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    form = AddTask()
    task = Tasks.query.filter_by(id=id).first()
    if request.method == "POST":
        task.title = form.title.data
        task.description = form.description.data
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("update.html", form=form, title="Update Task", task=task)

@app.route('/complete/<int:id>')
def complete(id):
    task = Tasks.query.filter_by(id=id).first()
    task.done = True
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/delete/<int:id>', methods=["GET", "POST"])
def delete(id):
    tasktodelete = Tasks.query.get(id)
    
    db.session.delete(tasktodelete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/count', methods=["GET", "POST"])
def count():
    number_of_tasks = Tasks.query.count()
    db.session.commit()
    return render_template("count.html", title="Count")

@app.route('/done/<int:task_id>')
def resolve_task(task_id):
    task = Tasks.query.get(task_id)

    if not task:
        return redirect('/')
    if task.done:
        task.done = False
    else:
        task.done = True

    db.session.commit()
    return redirect('/')