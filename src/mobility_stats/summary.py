from mobility_stats.rides import average_duration, busiest_start_station, count_by_rider_type


def build_summary(rides):
    """Build a compact dictionary with headline statistics."""
    ride_stats = {
        "ride_count": len(rides),
        "average_duration": average_duration(rides),
        "rider_types": count_by_rider_type(rides),
    }
    if rides:
        ride_stats["busiest_start_station"] = busiest_start_station(rides)
    else:
        ride_stats["busiest_start_station"] = None
    return ride_stats


def format_summary(rides):
    """Create a human-readable text summary."""
    title = "Mobility summary"
    line_rides = f"Rides: {rides['ride_count']}"
    line_av_dur = f"Average duration: {rides['average_duration']:.1f} min"
    line_bus_start = f"Busiest start: {rides['busiest_start_station']}"
    return title + "\n" + line_rides + "\n" + line_av_dur + "\n" + line_bus_start
