# services/location_service.py

from datetime import datetime, timezone

from database import get_connection
from models import LocationData


def save_location(data: LocationData):

    conn = get_connection()
    cursor = conn.cursor()

    server_time = datetime.now(timezone.utc).isoformat()

    cursor.execute("""
        INSERT INTO locations (
            user_id,
            route,
            latitude,
            longitude,
            accuracy,
            speed,
            heading,
            timestamp
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data.user_id,
        data.route,
        data.latitude,
        data.longitude,
        data.accuracy,
        data.speed,
        data.heading,
        server_time
    ))

    conn.commit()

    location_id = cursor.lastrowid

    conn.close()

    print(
        f"[LOCATION] "
        f"user={data.user_id} "
        f"route={data.route} "
        f"lat={data.latitude} "
        f"lon={data.longitude} "
        f"accuracy={data.accuracy}"
    )

    return location_id