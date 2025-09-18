from flask import Flask, render_template, request, g, redirect, url_for
import sqlite3
import logging
# Supress 304 and terminal flood messages
logging.getLogger('werkzeug').setLevel(logging.WARNING)

app = Flask(__name__)


# Database connection function
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('Python_Backend/Distances.db')
        db.row_factory = sqlite3.Row
        db.commit()
    return db


@app.teardown_appcontext
def close_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


# Information page with instructions
@app.route('/Information', methods=['GET', 'POST'])
def Info():
    return render_template('Information.html')


# Statistics page with Variables to be passed to Jinja in html
@app.route('/Statistics', methods=['GET', 'POST'])
def Stats():
    db = get_db()
    c = db.cursor()
    
    # Back end validation / form submission
    if request.method == 'POST':
        Distance = request.form.get('Distance', '').strip()
        Map = request.form.get('Map', '').strip()
        Vehicle = request.form.get('Vehicle', '').strip()
        print("Distance:", Distance)
        print("Map:", Map)
        print("Vehicle:", Vehicle)

        map_whitelist = [
            "Countryside", "Forest", "City", "Mountain", "Reef",
            "Winter", "Mines", "Desert", "Beach", "Bog",
            "Glacier", "Patchwork", "Savanna", "Gloomvale",
            "Overspill", "Canyonarena", "Cuptown", "Moon"
        ]

        vehicle_whitelist = [
            "Jeep", "Scooter", "Bus", "Mk2", "Tractor", "Motocross",
            "Dune Buggy", "Sports Car", "Monster Truck", "Rotator",
            "Super Diesel", "Chopper", "Tank", "Lowrider", "Snowmobile",
            "Monowheel", "Beast", "RallyCar", "Formula", "Muscle Car",
            "Racing Truck", "Hotrod", "CC-EV", "Superbike", "Supercar",
            "Moonlander", "Rock Bouncer", "Hoverbike", "Raider",
            "Glider", "Bolt"
        ]

        # Backend validation
        if Distance.isdigit():
            Distance = int(Distance)
            if 0 < int(Distance) < 10001:
                if Map in map_whitelist and Vehicle in vehicle_whitelist:
                    map_row = c.execute(
                        "SELECT map_id FROM Maps WHERE map_name = ?",
                        (Map,)).fetchone()
                    vehicle_row = c.execute(
                        "SELECT vehicle_id FROM Vehicles WHERE vehicle_name = ?",
                        (Vehicle,)).fetchone()

                    # Insert or replace distance
                    c.execute(
                        'INSERT OR REPLACE INTO Distances (map_id, vehicle_id, distance) VALUES (?, ?, ?)',
                        (map_row['map_id'], vehicle_row['vehicle_id'], Distance)
                    )
                    db.commit()
                    print("Inserted/Replaced")
                else:
                    print("Not whitelisted")
            else:
                print("Not inbetween 1 and 10,000")
        else:
            print("Distance isnt a number")

        # Prevent form resubmission
        return redirect(url_for('Stats'))

    # Fetch all data from distances table to be displayed
    rows = c.execute('''
        SELECT D.distance, M.map_name AS map, V.vehicle_name AS vehicle,
        D.map_id, D.vehicle_id
        FROM Distances D
        JOIN Maps M ON D.map_id = M.map_id
        JOIN Vehicles V ON D.vehicle_id = V.vehicle_id
        ORDER BY M.map_name, V.vehicle_name
    ''').fetchall()

    # Convert to dictionary for easier Jinja usage
    Forms = {(row['map'], row['vehicle']): row['distance'] for row in rows}

    TotalStars = sum(row['distance'] for row in rows)
    TotalDistance = TotalStars // 1000
    Total10ks = sum(row['distance'] // 10000 for row in rows)
    TotalPercent = (Total10ks * 100) // 558
    Remaining10ks = 558 - Total10ks
    AverageStars = TotalStars // 18
    Percent = (TotalStars * 100) // 5800000

    CountrysideStars = sum(row['distance'] for row in rows if row['map'] == 'Countryside')
    ForestStars = sum(row['distance'] for row in rows if row['map'] == 'Forest')
    CityStars = sum(row['distance'] for row in rows if row['map'] == 'City')
    MountainStars = sum(row['distance'] for row in rows if row['map'] == 'Mountain')
    ReefStars = sum(row['distance'] for row in rows if row['map'] == 'Reef')
    WinterStars = sum(row['distance'] for row in rows if row['map'] == 'Winter')
    MinesStars = sum(row['distance'] for row in rows if row['map'] == 'Mines')
    DesertValleyStars = sum(row['distance'] for row in rows if row['map'] == 'Desert')
    BeachStars = sum(row['distance'] for row in rows if row['map'] == 'Beach')
    BogStars = sum(row['distance'] for row in rows if row['map'] == 'Bog')
    GlacierStars = sum(row['distance'] for row in rows if row['map'] == 'Glacier')
    PatchworkStars = sum(row['distance'] for row in rows if row['map'] == 'Patchwork')
    SavannaStars = sum(row['distance'] for row in rows if row['map'] == 'Savanna')
    GloomvaleStars = sum(row['distance'] for row in rows if row['map'] == 'Gloomvale')
    OverspillStars = sum(row['distance'] for row in rows if row['map'] == 'Overspill')
    CanyonarenaStars = sum(row['distance'] for row in rows if row['map'] == 'Canyonarena')
    CuptownStars = sum(row['distance'] for row in rows if row['map'] == 'Cuptown')
    MoonStars = sum(row['distance'] for row in rows if row['map'] == 'Moon')

    Map_Stars = [
        CountrysideStars, ForestStars, CityStars, MountainStars,
        ReefStars, WinterStars, MinesStars, DesertValleyStars,
        BeachStars, BogStars, GlacierStars, PatchworkStars,
        SavannaStars, GloomvaleStars, OverspillStars, CanyonarenaStars,
        CuptownStars, MoonStars
    ]
    MaxMaps = sum(1 for i in Map_Stars if i == 310000)

    Percent1 = (CountrysideStars * 100) // 310000
    Percent2 = (ForestStars * 100) // 310000
    Percent3 = (CityStars * 100) // 310000
    Percent4 = (MountainStars * 100) // 310000
    Percent5 = (ReefStars * 100) // 310000
    Percent6 = (WinterStars * 100) // 310000
    Percent7 = (MinesStars * 100) // 310000
    Percent8 = (DesertValleyStars * 100) // 310000
    Percent9 = (BeachStars * 100) // 310000
    Percent10 = (BogStars * 100) // 310000
    Percent11 = (GlacierStars * 100) // 310000
    Percent12 = (PatchworkStars * 100) // 310000
    Percent13 = (SavannaStars * 100) // 310000
    Percent14 = (GloomvaleStars * 100) // 310000
    Percent15 = (OverspillStars * 100) // 310000
    Percent16 = (CanyonarenaStars * 100) // 310000
    Percent17 = (CuptownStars * 100) // 310000
    Percent18 = (MoonStars * 100) // 310000

    return render_template(
        'Statistics.html',
        rows=rows,
        Forms=Forms,
        CountrysideStars=CountrysideStars,
        ForestStars=ForestStars,
        CityStars=CityStars,
        MountainStars=MountainStars,
        ReefStars=ReefStars,
        WinterStars=WinterStars,
        MinesStars=MinesStars,
        DesertValleyStars=DesertValleyStars,
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
        TotalStars=TotalStars,
        TotalDistance=TotalDistance,
        Total10ks=Total10ks,
        TotalPercent=TotalPercent,
        Remaining10ks=Remaining10ks,
        AverageStars=AverageStars,
        Percent=Percent,
        MaxMaps=MaxMaps
    )


# Delete function for removing data
@app.route('/delete_distance/<int:map_id>/<int:vehicle_id>', methods=['POST'])
def delete_distance(map_id, vehicle_id):
    db = get_db()
    c = db.cursor()
    c.execute('DELETE FROM Distances WHERE map_id = ? AND vehicle_id = ?', (map_id, vehicle_id))
    db.commit()
    return redirect(url_for('Stats'))


# Function for terminal debugging
if __name__ == '__main__':
    app.run(debug=True)
