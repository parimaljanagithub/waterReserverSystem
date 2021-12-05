from flask import Blueprint, request, render_template
from src import db
from src.main.staticData import insert_static_data

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
   # page = request.args.get('page', 1, type=int)
    #posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    insert_static_data()
    return render_template('home.html', posts=1)




    



    
    