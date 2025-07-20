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
    TotalStars = sum(row['distance'] for row in rows)
    TotalStars = format(TotalStars, ',')
    CountrysideStars = sum(row['distance'] for row in rows if row['map'] == 'Countryside')
    ForestStars = sum(row['distance'] for row in rows if row['map'] == 'Forest')
    CityStars = sum(row['distance'] for row in rows if row['map'] == 'City')
    MountainStars = sum(row['distance'] for row in rows if row['map'] == 'Mountain')
    ReefStars = sum(row['distance'] for row in rows if row['map'] == 'Reef')
    WinterStars = sum(row['distance'] for row in rows if row['map'] == 'Winter')
    MinesStars = sum(row['distance'] for row in rows if row['map'] == 'Mines')
    DesertvalleyStars = sum(row['distance'] for row in rows if row['map'] == 'Desert')
    BeachStars = sum(row['distance'] for row in rows if row['map'] == 'Beach')
    BogStars = sum(row['distance'] for row in rows if row['map'] == 'Bog')
    GlacierStars = sum(row['distance'] for row in rows if row['map'] == 'Glacier')
    PatchworkStars = sum(row['distance'] for row in rows if row['map'] == 'Patchwork')
    SavannaStars = sum(row['distance'] for row in rows if row['map'] == 'Savanna')
    GloomvaleStars = sum(row['distance'] for row in rows if row['map'] == 'Gloomvale')
    OverspillStars = sum(row['distance'] for row in rows if row['map'] == 'Overspill')
    CanyonarenaStars = sum(row['distance'] for row in rows if row['map'] == 'Arena')
    CuptownStars = sum(row['distance'] for row in rows if row['map'] == 'Cuptown')
    MoonStars = sum(row['distance'] for row in rows if row['map'] == 'Moon')
    return render_template('home.html', rows=rows, TotalStars=TotalStars, 
                           CountrysideStars=CountrysideStars,
                           ForestStars=ForestStars,
                           CityStars=CityStars,
                           MountainStars=MountainStars,
                           ReefStars=ReefStars,
                           WinterStars=WinterStars,
                           MinesStars=MinesStars,
                           DesertvalleyStars=DesertvalleyStars,
                           BeachStars=BeachStars,
                           BogStars=BogStars,
                           GlacierStars=GlacierStars,
                           PatchworkStars=PatchworkStars,
                           SavannaStars=SavannaStars,
                           GloomvaleStars=GloomvaleStars,
                           OverspillStars=OverspillStars,
                           CanyonarenaStars=CanyonarenaStars,
                           CuptownStars=CuptownStars,
                           MoonStars=MoonStars
                           )


#10k form page route and POST debugging
@app.route('/10k_Form.html', methods=['GET', 'POST'])
def Form10k():
    print(request.method)
    db = get_db()
    c = db.cursor()

    if request.method == 'POST':
        Distance = request.form.get('Distance').strip()
        Map = request.form.get('Map')
        Vehicle = request.form.get('Vehicle')
        print("Distance:", Distance)
        print("Map:", Map)
        print("Vehicle:", Vehicle)
        if Distance.isdigit():
            Distance = int(Distance)
            if 0 < Distance < 10001:
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
                print("POSTED")
            else:
                print("Not < 10000 or > 0")
        else:
            print("Not numbers")

        return redirect(url_for('Form10k')) #Prevent form resubmition when reloading page

    forms = c.execute('SELECT * FROM Distances').fetchall()

    #Convert data to dictionary
    Rows = {}
    for form in forms:
        Rows[(form['map'], form['vehicle'])] = form['distance']
    
    return render_template('10k_Form.html', forms=forms, Rows=Rows)


#Delete function for removing data
@app.route('/delete_distance/<int:id>', methods=['POST'])
def delete_distance(id):
    db = get_db()
    db.execute("DELETE FROM Distances WHERE id = ?", (id,))
    db.commit()
    return redirect(url_for('home'))

#Function for terminal debugging
if __name__ == '__main__':
    app.run(debug = True)