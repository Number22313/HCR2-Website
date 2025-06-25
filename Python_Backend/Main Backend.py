from flask import Flask, render_template, request, g
import sqlite3
import logging
logging.getLogger('werkzeug').setLevel(logging.WARNING)

app = Flask(__name__)


# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect('/10k_Database.db')
#         c = db.cursor()
#         c.execute('''CREATE TABLE IF NOT EXISTS Distance (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     name TEXT
#                   )''')
        
#         c.execute('''CREATE TABLE IF NOT EXISTS Map (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     name TEXT
#                   )''')
        
#         c.execute('''CREATE TABLE IF NOT EXISTS Vehicle (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     name TEXT
#                   )''')
        
#         c.execute('''CREATE TABLE IF NOT EXISTS VehicleMap (
#                     vehicle_id INTEGER,
#                     map_id INTEGER,
#                     FOREIGN KEY(vehicle_id) REFERENCES Vehicle(id),
#                     FOREIGN KEY(map_id) REFERENCES Map(id),
#                     PRIMARY KEY (vehicle_id, map_id)
#                   )''')

#         c.execute('''CREATE TABLE IF NOT EXISTS ten_ks(
#                     id Integer PRIMARY KEY AUTOINCREMENT,
#                     name TEXT UNIQUE,
#                     Distance INT,
#                     Map TEXT,
#                     Vehicle TEXT,
#                   )''')
#         db.commit()
#     return db

# @app.teardown_appcontext
# def close_db(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()

#make home.html the first page to load
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/desert-valley-jeep.html')
def dvj():
    return('/desert-valley-jeep.html')


# @app.route('/specific_combo.html')
# def ten_ks():
#     conn = sqlite3.connect('10k_Database.db')
#     cur = conn.cursor()
#     cur.execute('SELECT * FROM Map WHERE id=?;',) #(id)
#     map = cur.fetchone()
#     cur.execute('SELECT name FROM Vehicle WHERE id IN (SELECT tid FROM VehicleMap WHERE pid=?)')
#     vehicle = cur.fetchall()
#     print(map, vehicle)
#     conn.close()
#     if map is None:
#         print("No Map")
#     else:
#         print("nothing")
#     return render_template('specific_combo.html', map=map,vehicle=vehicle)


#10k form page route and render
# @app.route('/10k_Form.html', methods=['GET', 'POST'])
# def Form10k():
#     if request.method == 'POST':
#         Distance = request.form['Distance']
#         Map = request.form['Map']
#         print("Distance:", Distance)
#         print("Map:", Map)
#         db = get_db()
#         c = db.cursor()
#         try:
#             c.execute(
#                 'INSERT INTO ten_ks (Distance, Map) VALUES (?,?)',
#                 (Distance, Map))
#             db.commit()
#         except sqlite3.IntegrityError:
#             c.execute(
#                 'UPDATE ten_ks SET Distance = ?, Map = ?',
#                 (Distance, Map))
#             db.commit()
#         return render_template('desert-valley-jeep.html')
    
#     return render_template('10k_Form.html')


#enable debugging
if __name__ == '__main__':
    app.run(debug = True)


#database example code
#@app.route('/page_1/<int:id>')
#def page_1():
#   return render_template('page_1.html')