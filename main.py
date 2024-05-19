
# Flask Application Design

# HTML Files
# agentville.html contains the main interface

# Routes
# @app.route('/agentville', methods=['GET', 'POST']): Main interface
# @app.route('/create_agent', methods=['POST']): Create new agents
# @app.route('/edit_agent/<int:id>', methods=['GET', 'POST']): Edit existing agents
# @app.route('/delete_agent/<int:id>', methods=['POST']): Delete existing agents

# Code Generation
# ...

# Code Validation
# ...

# Output
main.py:

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agentville.db'
db = SQLAlchemy(app)

class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    age = db.Column(db.Integer)
    city = db.Column(db.String(80))

@app.route('/agentville', methods=['GET', 'POST'])
def agentville():
    if request.method == 'POST':
        new_agent = Agent(name=request.form['name'], age=request.form['age'], city=request.form['city'])
        db.session.add(new_agent)
        db.session.commit()
        return redirect(url_for('agentville'))
    agents = Agent.query.all()
    return render_template('agentville.html', agents=agents)

@app.route('/create_agent', methods=['POST'])
def create_agent():
    if request.method == 'POST':
        new_agent = Agent(name=request.form['name'], age=request.form['age'], city=request.form['city'])
        db.session.add(new_agent)
        db.session.commit()
        return redirect(url_for('agentville'))

@app.route('/edit_agent/<int:id>', methods=['GET', 'POST'])
def edit_agent(id):
    agent = Agent.query.get_or_404(id)
    if request.method == 'POST':
        agent.name = request.form['name']
        agent.age = request.form['age']
        agent.city = request.form['city']
        db.session.commit()
        return redirect(url_for('agentville'))
    return render_template('agentville.html', agent=agent)

@app.route('/delete_agent/<int:id>', methods=['POST'])
def delete_agent(id):
    agent = Agent.query.get_or_404(id)
    db.session.delete(agent)
    db.session.commit()
    return redirect(url_for('agentville'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
