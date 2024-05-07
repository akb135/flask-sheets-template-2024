from flask import Blueprint, render_template, current_app #, session

from app.models.destination import Destination

destination_routes = Blueprint("destination_routes", __name__)

@destination_routes.route("/destinations")
def destinations():
    destinations = Destination.all()
    return render_template("destinations.html", destinations=destinations)
