from flask import Flask, render_template, request, g, redirect, url_for
import sqlite3
import logging
logging.getLogger('werkzeug').setLevel(logging.WARNING) #Supress 304 and terminal flood messages

app = Flask(__name__)


def get_db(): #Database connection function
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('Python_Backend/Distances.db')
        db.row_factory = sqlite3.Row
        c = db.cursor()
        db.commit()
    return db

@app.teardown_appcontext
def close_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


# @app.route('/desert-valley-jeep.html')
# def dvj():
#     return('/desert-valley-jeep.html')

#Main home page route with database table
@app.route('/home', methods=['GET', 'POST'])
def home():
    db = get_db()
    cur = db.cursor()
    rows = cur.execute('SELECT * FROM Distances').fetchall()
    return render_template('home.html', rows=rows)


#10k form page route and POST debugging
@app.route('/10k_Form.html', methods=['GET', 'POST'])
def Form10k():
    print("10kform ", request.method)
    db = get_db()
    c = db.cursor()

    if request.method == 'POST':
        print("POSTED")
        Distance = request.form.get('Distance')
        Map = request.form.get('Map')
        Vehicle = request.form.get('Vehicle')
        print("Distance:", Distance)
        print("Map:", Map)
        print("Vehicle:", Vehicle)
        try: #Insert form data into db
            c.execute(
                'INSERT INTO Distances (map, vehicle, distance) VALUES (?,?,?)',
                (Map, Vehicle, Distance))
            print("Inserted")
            db.commit()
        except sqlite3.IntegrityError: #Update db for duplicate data
            c.execute(
                'UPDATE Distances SET distance = ? WHERE map = ? AND vehicle = ?',
                (Distance, Map, Vehicle))
            print("Updated")
            db.commit()

        return redirect(url_for('Form10k')) #Prevent form resubmition when reloading page

    forms = c.execute('SELECT * FROM Distances').fetchall()

    #Convert forms to dictionary
    Rows = {}
    for form in forms:
        Rows[(form['map'], form['vehicle'])] = form['distance']

    return render_template('10k_Form.html', forms=forms, Rows=Rows)


#Delete function for form inputs
@app.route('/delete_distance/<int:id>', methods=['POST'])
def delete_distance(id):
    db = get_db()
    db.execute("DELETE FROM Distances WHERE id = ?", (id,))
    db.commit()
    return redirect(url_for('home'))

#Funciton for terminal debugging
if __name__ == '__main__':
    app.run(debug = True)