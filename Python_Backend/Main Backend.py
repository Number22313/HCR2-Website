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
    Percent = ((TotalStars * 100)//5800000)
    TotalStars = format(TotalStars, ',')
    CountrysideStars = sum(row['distance'] for row in rows if row['map'] == 'Countryside')
    Percent1 = ((CountrysideStars *100)//310000)
    CountrysideStars = format(CountrysideStars, ',')
    ForestStars = sum(row['distance'] for row in rows if row['map'] == 'Forest')
    Percent2 = ((ForestStars *100)//310000)
    ForestStars = format(ForestStars, ',')
    CityStars = sum(row['distance'] for row in rows if row['map'] == 'City')
    Percent3 = ((CityStars *100)//310000)
    CityStars = format(CityStars, ',')
    MountainStars = sum(row['distance'] for row in rows if row['map'] == 'Mountain')
    Percent4 = ((MountainStars *100)//310000)
    MountainStars = format(MountainStars, ',')
    ReefStars = sum(row['distance'] for row in rows if row['map'] == 'Reef')
    Percent5 = ((ReefStars *100)//310000)
    ReefStars = format(ReefStars, ',')
    WinterStars = sum(row['distance'] for row in rows if row['map'] == 'Winter')
    Percent6 = ((WinterStars *100)//310000)
    WinterStars = format(WinterStars, ',')
    MinesStars = sum(row['distance'] for row in rows if row['map'] == 'Mines')
    Percent7 = ((MinesStars *100)//310000)
    MinesStars = format(MinesStars, ',')
    DesertvalleyStars = sum(row['distance'] for row in rows if row['map'] == 'Desert')
    Percent8 = ((DesertvalleyStars *100)//310000)
    DesertvalleyStars = format(DesertvalleyStars, ',')
    BeachStars = sum(row['distance'] for row in rows if row['map'] == 'Beach')
    Percent9 = ((BeachStars *100)//310000)
    BeachStars = format(BeachStars, ',')
    BogStars = sum(row['distance'] for row in rows if row['map'] == 'Bog')
    Percent10 = ((BogStars *100)//310000)
    BogStars = format(BogStars, ',')
    GlacierStars = sum(row['distance'] for row in rows if row['map'] == 'Glacier')
    Percent11 = ((GlacierStars *100)//310000)
    GlacierStars = format(GlacierStars, ',')
    PatchworkStars = sum(row['distance'] for row in rows if row['map'] == 'Patchwork')
    Percent12 = ((PatchworkStars *100)//310000)
    PatchworkStars = format(PatchworkStars, ',')
    SavannaStars = sum(row['distance'] for row in rows if row['map'] == 'Savanna')
    Percent13 = ((SavannaStars *100)//310000)
    SavannaStars = format(SavannaStars, ',')
    GloomvaleStars = sum(row['distance'] for row in rows if row['map'] == 'Gloomvale')
    Percent14 = ((GloomvaleStars *100)//310000)
    GloomvaleStars = format(GloomvaleStars, ',')
    OverspillStars = sum(row['distance'] for row in rows if row['map'] == 'Overspill')
    Percent15 = ((OverspillStars *100)//310000)
    OverspillStars = format(OverspillStars, ',')
    CanyonarenaStars = sum(row['distance'] for row in rows if row['map'] == 'Canyonarena')
    Percent16 = ((CanyonarenaStars *100)//310000)
    CanyonarenaStars = format(CanyonarenaStars, ',')
    CuptownStars = sum(row['distance'] for row in rows if row['map'] == 'Cuptown')
    Percent17 = ((CuptownStars *100)//310000)
    CuptownStars = format(CuptownStars, ',')
    MoonStars = sum(row['distance'] for row in rows if row['map'] == 'Moon')
    Percent18 = ((MoonStars *100)//310000)
    MoonStars = format(MoonStars, ',')
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
                           MoonStars=MoonStars,
                           Percent=Percent,
                           Percent1=Percent1,
                           Percent2=Percent2,
                           Percent3=Percent3,
                           Percent4=Percent4,
                           Percent5=Percent5,
                           Percent6=Percent6,
                           Percent7=Percent7,
                           Percent8=Percent8,
                           Percent9=Percent9,
                           Percent10=Percent10,
                           Percent11=Percent11,
                           Percent12=Percent12,
                           Percent13=Percent13,
                           Percent14=Percent14,
                           Percent15=Percent15,
                           Percent16=Percent16,
                           Percent17=Percent17,
                           Percent18=Percent18
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
    Forms = {}
    for form in forms:
        Forms[(form['map'], form['vehicle'])] = form['distance']

    return render_template('10k_Form.html', forms=forms, Forms=Forms)


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