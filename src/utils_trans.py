from pyflightdata import FlightData
from typing import TypedDict
from datetime import datetime

class FlightInfo(TypedDict):
    departure_airport: str
    arrival_airport: str
    departure_region: str
    arrival_region: str
    departure_time: str
    estimated_arrival_time: str

class FlightInfoData(TypedDict):
    start_flight: FlightInfo
    return_flight: FlightInfo

def search_flight_details(start_flight: str = None, return_flight: str = None) -> FlightInfoData:
    f = FlightData()
    
    departure_result = f.get_history_by_flight_number(start_flight)[-1]
    start_info = {
        "departure_airport": departure_result["airport"]["origin"]["name"],
        "arrival_airport": departure_result["airport"]["destination"]["name"],
        "departure_region": departure_result["airport"]["origin"]["position"]["region"]["city"],
        "arrival_region": departure_result["airport"]["destination"]["position"]["region"]["city"],
        "departure_time": datetime.fromtimestamp(departure_result["time"]["real"]["departure_millis"] / 1000).strftime('%H:%M'),
        "estimated_arrival_time": datetime.fromtimestamp(departure_result["time"]["other"]["eta_millis"] / 1000).strftime('%H:%M')
    }
    
    return_result = f.get_history_by_flight_number(return_flight)[-1]
    return_info = {
        "departure_airport": return_result["airport"]["origin"]["name"],
        "arrival_airport": return_result["airport"]["destination"]["name"],
        "departure_region": return_result["airport"]["origin"]["position"]["region"]["city"],
        "arrival_region": return_result["airport"]["destination"]["position"]["region"]["city"],
        "departure_time": datetime.fromtimestamp(return_result["time"]["real"]["departure_millis"] / 1000).strftime('%H:%M'),
        "estimated_arrival_time": datetime.fromtimestamp(return_result["time"]["other"]["eta_millis"] / 1000).strftime('%H:%M')
    }
    
    return {
        "start_flight": start_info,
        "return_flight": return_info
    }

if __name__ == "__main__":
    flight_data = search_flight_details()
    print(flight_data)


    activity = {"location":"part", "suggested_duration":"2h", "type":"sightseeing"}