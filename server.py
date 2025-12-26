from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', 
                         title='my home page',
                         msg="This is Elon Mask")

@app.route('/user/info')
def info():
  return render_template('info.html',title='My Info',name='Satitkhun Singkrut',email="std.67122420317@ubru.ac.th",mobile='061-6483176',age=20)

@app.route('/favorite/sports')
def fav_sports():
  sports = ['Basketball','Football','PingPong']
  return render_template('favorite_sports.html',
                         title='My Favorite Sports Page',
                         sports= sports)

@app.route('/favorite/food')
def fav_food():
  foods = ['ไข่ดาว','ไข่เจียว','ไข่แมว','ไข่แมว Pro Max','ไข่แมว Ultra max ']
  return render_template('favorite_food.html',
                         title='My Favorite Food Page',
                         foods = foods)


@app.route('/favorite/movie')
def movies():
  movies = ['วันนี้วันไหนยังไงก็เธอ','ตำนานจั้งไห่','แอบรักให้เธอรู้','มาราธอน','รักแห่งสยาม']
  return render_template('favorite_movie.html',
                         title='My Favorite Movies Page',
                         movies = movies)

if __name__ == '__main__':
  app.run(debug=True)