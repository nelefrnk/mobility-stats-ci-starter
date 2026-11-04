import csv
import os
from collections import defaultdict


def load_rides(csv_path: str) -> list[dict[str, object]]:
    """Load ride data from a CSV file."""
    new_rides = []
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Could not find file: {csv_path}")
    with open(csv_path, newline="", encoding="utf-8") as f:
        old_rides = csv.DictReader(f)
        for ride in old_rides:
            new_rides.append(
                {
                    "ride_id": ride["ride_id"],
                    "start_station": ride["start_station"],
                    "end_station": ride["end_station"],
                    "duration_min": float(ride["duration_min"]),
                    "rider_type": ride["rider_type"],
                }
            )
    return new_rides


def average_duration(rides):
    """Return the average ride duration in minutes."""
    if len(rides) == 0:
        return 0.0
    ges_dur = 0.0
    for ride in rides:
        ges_dur += ride["duration_min"]
    return ges_dur / len(rides)


def count_by_rider_type(rides):
    """Count rides for each rider type."""
    rider_types = defaultdict(int)
    for ride in rides:
        rider_types[ride["rider_type"]] += 1
    return dict(rider_types)


def busiest_start_station(rides):
    """Return the start station with the most rides."""
    if rides is None:
        raise ValueError("rides must not be None")
    if len(rides) == 0:
        raise ValueError("rides must not be empty")
    start_stations = defaultdict(int)
    for ride in rides:
        start_stations[ride["start_station"]] += 1
    return max(start_stations, key=start_stations.get)


def filter_long_rides(rides, min_duration=30):
    """Return all rides with duration greater than or equal to b minutes."""
    loner_rides = []
    for ride in rides:
        if ride["duration_min"] >= min_duration:
            loner_rides.append(ride)
    return loner_rides
