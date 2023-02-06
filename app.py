from flask import Flask, render_template, request, redirect
import datetime

app = Flask(__name__)
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
            event = "Monday 5:30am"

    if day_of_week == "Sunday":
            date = (now + datetime.timedelta(days=1)).strftime("%m/%d/%Y")
            event = "Monday 5:30am"
            
    if day_of_week == "Monday":
            date = (now + datetime.timedelta(days=0)).strftime("%m/%d/%Y")
            if now.hour < 6:
                event = "Monday 5:30am"
            else:
                event = "Monday 12:00pm"

    if day_of_week == "Tuesday":
            event = "Wednesday 5:30am"
            date = (now + datetime.timedelta(days=1)).strftime("%m/%d/%Y")

    if day_of_week == "Wednesday":
            date = (now + datetime.timedelta(days=0)).strftime("%m/%d/%Y")
            if now.hour < 6:
                event = "Wednesday 5:30am"
            else:
                event = "Wednesday 12:00pm"      

    if day_of_week == "Thursday":
            event = "Friday 5:30am"
            date = (now + datetime.timedelta(days=1)).strftime("%m/%d/%Y") 

    if day_of_week == "Friday":
            date = (now + datetime.timedelta(days=0)).strftime("%m/%d/%Y") 
            if now.hour < 6:
                event = "Friday 5:30am"
            else:
                event = "Friday 12:00pm"

    return render_template("index.html", date=date, event=event, attendees=events[event])



@app.route("/checkin", methods=["POST"])
def checkin():
    name = request.form["name"]
    event = request.form["event"]
    events[event].append(name)
    return redirect("/")

if __name__ == "__main__":
    app.run()
