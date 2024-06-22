from flask import Flask, render_template, request, redirect
from models import create_user, get_users, update_user, delete_user

app = Flask(__name__)

@app.route('/')
def user_list():
    users = get_users()
    print(users)
    return "users"

@app.route('/create',methods=['GET','POST'])
def create():
    if request.method == 'POST':
        return redirect('/')
    return 'post'

@app.route('/update/<int:user_id>',methods=['GET',"PUT"])
def update(user_id):
    if request.method == 'PUT':
        return redirect('/')
    return f" {user_id} put"

@app.route('/delete/<int:user_id>',methods=['GET',"DELETE"])
def delete(user_id):
    if request.method == 'DELETE':
        return redirect('/')
    return f'{user_id} delete'

if __name__ == "__main__":
    app.run(debug=True)


    