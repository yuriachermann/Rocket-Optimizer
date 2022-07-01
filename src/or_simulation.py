import os
import orhelper
import numpy as np
import xml.etree.ElementTree as ET
from orhelper import FlightDataType, FlightEvent


def run_simulation(fin=0, length=0, diameter=0, nose=0):
    with orhelper.OpenRocketInstance() as instance:
        orh = orhelper.Helper(instance)
        fl = open('rocket.ork')
        fl.close()
        doc = orh.load_doc(os.path.join('rocket.ork'))
        sim = doc.getSimulation(0)
        orh.run_simulation(sim)
        dt = orh.get_timeseries(sim,
                                [FlightDataType.TYPE_TIME, FlightDataType.TYPE_ALTITUDE,
                                 FlightDataType.TYPE_VELOCITY_Z])
        events = orh.get_events(sim)
        apogee = np. \
            interp(events.get(FlightEvent.APOGEE), dt[FlightDataType.TYPE_TIME], dt[FlightDataType.TYPE_ALTITUDE])

    return apogee[0]


apg = round(run_simulation(), 2)
print("\nApogeu =", apg, "m")
