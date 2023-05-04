import os

import numpy as np
import orhelper
from orhelper import FlightDataType, FlightEvent


def run_simulation(fin=0, length=0, diameter=0, nose=0):
    with orhelper.OpenRocketInstance(jar_path="../../data/OpenRocket-15.03.jar") as instance:
        orh = orhelper.Helper(instance)
        fl = open('../../data/teste.ork')
        fl.close()
        doc = orh.load_doc(os.path.join('teste.ork'))
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
print("\nApogee =", apg, "m")

if __name__ == '__main__':
    run_simulation()
