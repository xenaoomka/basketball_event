from flask import Flask, render_template, request, redirect
import datetime
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('db/attendees.db', check_same_thread=False)
events = {
    "Monday 5:30am": [],
    "Monday 12:00pm": [],
    "Wednesday 5:30am": [],
    "Wednesday 12:00pm": [],
    "Friday 5:30am": [],
    "Friday 12:00pm": []
}

@app.route("/")
def index():
    now = datetime.datetime.now()
    day_of_week = now.strftime("%A")
    #now = datetime.datetime(2022,2,28,5,5,0)
    #day_of_week = "Tuesday"
    time = now.strftime("%I:%M%p")

    if day_of_week == "Saturday":
            date = (now + datetime.timedelta(days=2)).strftime("%m/%d/%Y")
            event = date+" Monday 5:30am"

    if day_of_week == "Sunday":
            date = (now + datetime.timedelta(days=1)).strftime("%m/%d/%Y")
            event = date+" Monday 5:30am"
            
    if day_of_week == "Monday":
            date = (now + datetime.timedelta(days=0)).strftime("%m/%d/%Y")
            if now.hour < 6:
                event = date+" Monday 5:30am"
            else:
                event = date+" Monday 12:00pm"

    if day_of_week == "Tuesday":
            date = (now + datetime.timedelta(days=1)).strftime("%m/%d/%Y")  
            event = date+" Wednesday 5:30am"
            

    if day_of_week == "Wednesday":
            date = (now + datetime.timedelta(days=0)).strftime("%m/%d/%Y")
            if now.hour < 6:
                event = date+" Wednesday 5:30am"
            else:
                event = date+" Wednesday 12:00pm"      

    if day_of_week == "Thursday":
            date = (now + datetime.timedelta(days=1)).strftime("%m/%d/%Y") 
            event = date+" Friday 5:30am"
 
    if day_of_week == "Friday":
            date = (now + datetime.timedelta(days=0)).strftime("%m/%d/%Y") 
            if now.hour < 6:
                event = date+" Friday 5:30am"
            else:
                event = date+" Friday 12:00pm"

    c = conn.cursor()
    c.execute("SELECT name FROM attendees WHERE event=?", (event,))
    attendees = [row[0] for row in c.fetchall()]
    c.close()
    return render_template("index.html", date=date, event=event, attendees=attendees)


@app.route("/checkin", methods=["POST"])
def checkin():
    name = request.form["name"]
    event = request.form["event"]
    c = conn.cursor()
    c.execute("INSERT INTO attendees (name, event) VALUES (?, ?)", (name, event))
    conn.commit()
    c.close()
    return redirect("/")

if __name__ == "__main__":
    conn.execute("CREATE TABLE IF NOT EXISTS attendees (name TEXT, event TEXT)")
    app.run()
