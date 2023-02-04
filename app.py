from flask import Flask, render_template, request, redirect
import datetime

app = Flask(__name__)
events = {
    "Monday 5:30am": [],
    "Wednesday 5:30am": [],
    "Friday 5:30am": [],
}

@app.route("/")
def index():
    now = datetime.datetime.now()
    day_of_week = now.strftime("%A")
    # now = datetime.datetime(2022,2,18,10,5,0)
    # day_of_week = "Saturday"
    time = now.strftime("%I:%M%p")

    if day_of_week == "Saturday":
            event = "Monday 5:30am"
            date = (now + datetime.timedelta(days=2)).strftime("%m/%d/%Y")
    if day_of_week == "Sunday":
            event = "Monday 5:30am"
            date = (now + datetime.timedelta(days=1)).strftime("%m/%d/%Y")
    if day_of_week == "Monday":
            event = "Monday 5:30am"
            date = (now + datetime.timedelta(days=0)).strftime("%m/%d/%Y")
    if day_of_week == "Tuesday":
            event = "Wednesday 5:30am"
            date = (now + datetime.timedelta(days=1)).strftime("%m/%d/%Y")
    if day_of_week == "Wednesday":
            event = "Wednesday 5:30am"
            date = (now + datetime.timedelta(days=0)).strftime("%m/%d/%Y")      
    if day_of_week == "Thursday":
            event = "Friday 5:30am"
            date = (now + datetime.timedelta(days=1)).strftime("%m/%d/%Y") 
    if day_of_week == "Friday":
            event = "Friday 5:30am"
            date = (now + datetime.timedelta(days=0)).strftime("%m/%d/%Y") 

    return render_template("index.html", date=date, event=event, attendees=events[event])



@app.route("/checkin", methods=["POST"])
def checkin():
    name = request.form["name"]
    event = request.form["event"]
    events[event].append(name)
    return redirect("/")

if __name__ == "__main__":
    app.run()
