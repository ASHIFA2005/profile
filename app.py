from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def profile():
    
    user_info = {
        'name': 'TEAM X',
        'email': 'teamx@gmail.com',
        'location': 'Trivandrum,Kerala',
    
        'profile_pic': 'images/x.avif'  
    }
    return render_template('index.html', user=user_info)

if __name__ == '_main_':
    app.run(debug=True)