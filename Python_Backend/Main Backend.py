from flask import Flask, render_template, request, g, redirect, url_for
import sqlite3
import logging
#Supress 304 and terminal flood messages
logging.getLogger('werkzeug').setLevel(logging.WARNING)

app = Flask(__name__)


#Database connection function
def get_db():
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

#Information page with instructions
@app.route('/Information', methods=['GET', 'POST'])
def Info():
    return render_template('Information.html')


#Statistics page with Variables to be passed to Jinja in html
@app.route('/Statistics', methods=['GET', 'POST'])
def Stats():
    #Call database funtion
    db = get_db()
    c = db.cursor()
    rows = c.execute('SELECT * FROM Distances').fetchall()
    
    #Variables to be displayed on the page
    TotalStars = sum(row['distance'] for row in rows)
    TotalDistance = TotalStars // 1000
    Total10ks = sum(row['distance'] // 10000 for row in rows)
    TotalPercent = ((Total10ks * 100) // 558)
    Remaining10ks = 558 - Total10ks
    AverageStars = TotalStars // 18
    Percent = ((TotalStars * 100)//5800000)
    CountrysideStars = sum(row['distance'] for row in rows if row['map'] == 'Countryside')
    CountrysideStars = 310000
    Percent1 = ((CountrysideStars * 100)//310000)
    ForestStars = sum(row['distance'] for row in rows if row['map'] == 'Forest')
    Percent2 = ((ForestStars * 100)//310000)
    CityStars = sum(row['distance'] for row in rows if row['map'] == 'City')
    Percent3 = ((CityStars * 100)//310000)
    MountainStars = sum(row['distance'] for row in rows if row['map'] == 'Mountain')
    Percent4 = ((MountainStars * 100)//310000)
    ReefStars = sum(row['distance'] for row in rows if row['map'] == 'Reef')
    Percent5 = ((ReefStars * 100)//310000)
    WinterStars = sum(row['distance'] for row in rows if row['map'] == 'Winter')
    Percent6 = ((WinterStars * 100)//310000)
    MinesStars = sum(row['distance'] for row in rows if row['map'] == 'Mines')
    Percent7 = ((MinesStars * 100)//310000)
    DesertvalleyStars = sum(row['distance'] for row in rows if row['map'] == 'Desert')
    Percent8 = ((DesertvalleyStars * 100)//310000)
    BeachStars = sum(row['distance'] for row in rows if row['map'] == 'Beach')
    Percent9 = ((BeachStars * 100)//310000)
    BogStars = sum(row['distance'] for row in rows if row['map'] == 'Bog')
    Percent10 = ((BogStars * 100)//310000)
    GlacierStars = sum(row['distance'] for row in rows if row['map'] == 'Glacier')
    Percent11 = ((GlacierStars * 100)//310000)
    PatchworkStars = sum(row['distance'] for row in rows if row['map'] == 'Patchwork')
    Percent12 = ((PatchworkStars * 100)//310000)
    SavannaStars = sum(row['distance'] for row in rows if row['map'] == 'Savanna')
    Percent13 = ((SavannaStars * 100)//310000)
    GloomvaleStars = sum(row['distance'] for row in rows if row['map'] == 'Gloomvale')
    Percent14 = ((GloomvaleStars * 100)//310000)
    OverspillStars = sum(row['distance'] for row in rows if row['map'] == 'Overspill')
    Percent15 = ((OverspillStars * 100)//310000)
    CanyonarenaStars = sum(row['distance'] for row in rows if row['map'] == 'Canyonarena')
    Percent16 = ((CanyonarenaStars * 100)//310000)
    CuptownStars = sum(row['distance'] for row in rows if row['map'] == 'Cuptown')
    Percent17 = ((CuptownStars * 100)//310000)
    MoonStars = sum(row['distance'] for row in rows if row['map'] == 'Moon')
    Percent18 = ((MoonStars * 100)//310000)
    Map_Stars = [CountrysideStars, ForestStars, CityStars, 
                 MountainStars, ReefStars, WinterStars, 
                 MinesStars, DesertvalleyStars, BeachStars,
                 BogStars, GlacierStars, PatchworkStars,
                 SavannaStars, GloomvaleStars, OverspillStars,
                 CanyonarenaStars, CuptownStars, MoonStars]
    MaxMaps = sum(1 for i in Map_Stars if i == 310000)
    
    #Formatted Version of star counts with commas
    TotalStars = format(TotalStars, ',')
    CountrysideStars = format(CountrysideStars, ',')
    ForestStars = format(ForestStars, ',')
    CityStars = format(CityStars, ',')
    MountainStars = format(MountainStars, ',')
    ReefStars = format(ReefStars, ',')
    WinterStars = format(WinterStars, ',')
    MinesStars = format(MinesStars, ',')
    DesertvalleyStars = format(DesertvalleyStars, ',')
    BeachStars = format(BeachStars, ',')
    BogStars = format(BogStars, ',')
    GlacierStars = format(GlacierStars, ',')
    PatchworkStars = format(PatchworkStars, ',')
    SavannaStars = format(SavannaStars, ',')
    GloomvaleStars = format(GloomvaleStars, ',')
    OverspillStars = format(OverspillStars, ',')
    CanyonarenaStars = format(CanyonarenaStars, ',')
    CuptownStars = format(CuptownStars, ',')
    MoonStars = format(MoonStars, ',')

    #Back end validation
    if request.method == 'POST':
        Distance = request.form.get('Distance').strip()
        Map = request.form.get('Map')
        Vehicle = request.form.get('Vehicle')
        print("Distance:", Distance)
        print("Map:", Map)
        print("Vehicle:", Vehicle)
        allowed_maps = [
            "Countryside", "Forest", "City", "Mountain", "Reef",
            "Winter", "Mines", "Desert Valley", "Beach", "Bog",
            "Glacier", "Patchwork", "Savanna", "Gloomvale",
            "Overspill", "Canyon Arena", "Cuptown", "Moon"
        ]

        allowed_vehicles = [
            "Jeep", "Scooter", "Bus", "Mk2", "Tractor", "Motocross",
            "Dune Buggy", "Sports Car", "Monster Truck", "Rotator",
            "Super Diesel", "Chopper", "Tank", "Lowrider", "Snowmobile",
            "Monowheel", "Beast", "RallyCar", "Formula", "Muscle Car",
            "Racing Truck", "Hotrod", "CC-EV", "Superbike", "Supercar",
            "Moonlander", "Rock Bouncer", "Hoverbike", "Raider",
            "Glider", "Bolt"
        ]

        if Distance.isdigit() and Map in allowed_maps and Vehicle in allowed_vehicles:
            Distance = int(Distance)
            if 0 < Distance < 10001:
                #Insert form data into db
                try:
                    c.execute(
                        'INSERT INTO Distances (map, vehicle, distance) VALUES (?,?,?)',
                        (Map, Vehicle, Distance))
                    print("Inserted")
                    db.commit()
                #Update db for duplicate data
                except sqlite3.IntegrityError:
                    c.execute(
                        'UPDATE Distances SET distance = ? WHERE map = ? AND vehicle = ?',
                        (Distance, Map, Vehicle))
                    print("Updated")
                    db.commit()
                print("POSTED")
            else:
                print("Distance not < 10000 or > 0")
        else:
            print("Not elegible for insertion")

        #Prevent form resubmition when reloading page
        return redirect(url_for('Form10k'))

    forms = c.execute('SELECT * FROM Distances').fetchall()

    #Convert data to dictionary
    Forms = {}
    for form in forms:
        Forms[(form['map'], form['vehicle'])] = form['distance']

    return render_template('Statistics.html', forms=forms,
                           Forms=Forms,
                           rows=rows,
                           TotalStars=TotalStars,
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
                           Percent18=Percent18,
                           MaxMaps=MaxMaps,
                           TotalDistance=TotalDistance,
                           Total10ks=Total10ks,
                           TotalPercent=TotalPercent,
                           Remaining10ks=Remaining10ks,
                           AverageStars=AverageStars
                           )


#Delete function for removing data
@app.route('/delete_distance/<int:id>', methods=['POST'])
def delete_distance(id):
    db = get_db()
    db.execute("DELETE FROM Distances WHERE id = ?", (id,))
    db.commit()
    return redirect(url_for('Stats'))

#Function for terminal debugging
if __name__ == '__main__':
    app.run(debug=True)
