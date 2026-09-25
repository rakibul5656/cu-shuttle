const route = getRoute();

const userId = getTelegramUserId();


console.log("[APP] Route:", route);

console.log("[APP] User ID:", userId);


window.sendLocation = async function (location) {

    if (!userId) {

        console.error(
            "[APP] Telegram user ID not available"
        );

        return;
    }


    if (!route) {

        console.error(
            "[APP] Route not specified"
        );

        return;
    }


    const payload = {

        user_id: userId,

        route: route,

        latitude: location.latitude,

        longitude: location.longitude,

        accuracy: location.accuracy,

        speed: location.speed,

        heading: location.heading,

        timestamp: location.timestamp
    };


    try {

        const result =
            await sendLocationToServer(
                payload
            );


        console.log(
            "[APP] Server response:",
            result
        );


        updateServerStatus(
            "Connected"
        );

    } catch (error) {

        updateServerStatus(
            "Server connection failed"
        );
    }
};


function displayLocation(location) {

    const latElement =
        document.getElementById("latitude");

    const lonElement =
        document.getElementById("longitude");

    const accuracyElement =
        document.getElementById("accuracy");

    const statusElement =
        document.getElementById("location-status");


    if (latElement) {

        latElement.textContent =
            location.latitude.toFixed(6);
    }


    if (lonElement) {

        lonElement.textContent =
            location.longitude.toFixed(6);
    }


    if (accuracyElement) {

        accuracyElement.textContent =
            location.accuracy
                ? `${location.accuracy.toFixed(1)} m`
                : "N/A";
    }


    if (statusElement) {

        statusElement.textContent =
            "GPS Active";
    }
}


function updateServerStatus(status) {

    const element =
        document.getElementById(
            "server-status"
        );


    if (element) {

        element.textContent = status;
    }
}


document.addEventListener(
    "DOMContentLoaded",
    function () {

        const routeElement =
            document.getElementById(
                "route"
            );


        if (routeElement) {

            routeElement.textContent =
                route || "Unknown";
        }


        const startButton =
            document.getElementById(
                "start-button"
            );


        const stopButton =
            document.getElementById(
                "stop-button"
            );


        if (startButton) {

            startButton.addEventListener(
                "click",
                function () {

                    startTracking();

                }
            );
        }


        if (stopButton) {

            stopButton.addEventListener(
                "click",
                function () {

                    stopTracking();

                }
            );
        }
    }
);