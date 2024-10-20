from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/Game'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Teams(db.Model):
    __tablename__ = 'teams' 
    Team_ID = db.Column(db.Integer, primary_key=True)
    Team_Name = db.Column(db.String(50), nullable=False, unique=True)
    State = db.Column(db.String(50), nullable=False)
    members = db.relationship("Players", backref="teams")

    def __repr__(self):
        return f"Team '{self.Team_Name}', State'{self.State}'"

class Players(db.Model):
    __tablename__ = 'players' 
    Player_ID = db.Column(db.Integer, primary_key=True)
    Player_Name = db.Column(db.String(50), nullable=False)
    Nationality = db.Column(db.String(50), nullable=False)
    Team_ID = db.Column(db.Integer, db.ForeignKey("teams.Team_ID"))  

    def __repr__(self):
        return f"Name '{self.Player_Name}', Nationality'{self.Nationality}'"


if __name__ == '__main__':
    app.run(debug=True)
