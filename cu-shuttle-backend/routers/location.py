from fastapi import APIRouter, HTTPException

from config import VALID_ROUTES
from models import LocationData
from services.location_service import save_location
from database import get_connection


router = APIRouter(
    prefix="/api",
    tags=["Location"]
)


@router.post("/location")
def receive_location(data: LocationData):

    if data.route not in VALID_ROUTES:
        raise HTTPException(
            status_code=400,
            detail="Invalid route"
        )

    location_id = save_location(data)

    return {
        "success": True,
        "message": "Location received",
        "location_id": location_id
    }


@router.get("/locations")
def get_locations():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            user_id,
            route,
            latitude,
            longitude,
            accuracy,
            speed,
            heading,
            timestamp
        FROM locations
        ORDER BY id DESC
        LIMIT 100
    """)

    rows = cursor.fetchall()

    conn.close()

    return {
        "count": len(rows),
        "locations": [dict(row) for row in rows]
    }