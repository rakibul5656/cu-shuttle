let browserWatchId = null;

let tracking = false;

let usingTelegramLocation = false;

let lastSentTime = 0;


function startTracking() {

    tracking = true;

    console.log("[LOCATION] Tracking started");


    if (
        tg.LocationManager &&
        typeof tg.LocationManager.init === "function"
    ) {

        startTelegramLocation();

    } else {

        startBrowserLocation();
    }
}


function startTelegramLocation() {

    try {

        tg.LocationManager.init(function () {

            if (!tracking) {
                return;
            }


            if (!tg.LocationManager.isLocationAvailable) {

                console.log(
                    "[LOCATION] Telegram location unavailable"
                );

                startBrowserLocation();

                return;
            }


            requestTelegramLocation();

        });

    } catch (error) {

        console.error(
            "[LOCATION] Telegram LocationManager error:",
            error
        );

        startBrowserLocation();
    }
}


function requestTelegramLocation() {

    tg.LocationManager.getLocation(function (location) {

        if (!tracking) {
            return;
        }


        if (!location) {

            console.log(
                "[LOCATION] Telegram location unavailable"
            );

            startBrowserLocation();

            return;
        }


        usingTelegramLocation = true;

        handleTelegramLocation(location);

    });
}


if (tg.LocationManager) {

    tg.LocationManager.onEvent(
        "locationRequested",
        function (event) {

            if (!tracking) {
                return;
            }


            if (
                event &&
                event.locationData
            ) {

                usingTelegramLocation = true;

                handleTelegramLocation(
                    event.locationData
                );
            }
        }
    );
}


function handleTelegramLocation(location) {

    const latitude = location.latitude;

    const longitude = location.longitude;

    const accuracy =
        location.horizontal_accuracy;

    const speed =
        location.speed;

    const heading =
        location.course;


    processLocation(
        latitude,
        longitude,
        accuracy,
        speed,
        heading
    );
}


function startBrowserLocation() {

    if (!navigator.geolocation) {

        console.error(
            "[LOCATION] Geolocation not supported"
        );

        return;
    }


    navigator.geolocation.getCurrentPosition(

        function (position) {

            if (!tracking) {
                return;
            }


            handleBrowserLocation(position);

            startBrowserWatch();

        },


        function (error) {

            console.error(
                "[LOCATION] Browser GPS error:",
                error
            );


            navigator.geolocation.getCurrentPosition(

                function (position) {

                    if (!tracking) {
                        return;
                    }


                    handleBrowserLocation(
                        position
                    );

                    startBrowserWatch();

                },

                function (retryError) {

                    console.error(
                        "[LOCATION] GPS retry failed:",
                        retryError
                    );
                },

                {
                    enableHighAccuracy: true,
                    timeout: 15000,
                    maximumAge: 5000
                }
            );
        },

        {
            enableHighAccuracy: false,
            timeout: 8000,
            maximumAge: 30000
        }
    );
}


function startBrowserWatch() {

    if (browserWatchId !== null) {
        return;
    }


    browserWatchId =
        navigator.geolocation.watchPosition(

            function (position) {

                if (!tracking) {
                    return;
                }


                handleBrowserLocation(
                    position
                );
            },


            function (error) {

                console.error(
                    "[LOCATION] Watch error:",
                    error
                );
            },


            {
                enableHighAccuracy: false,
                maximumAge: 5000,
                timeout: 20000
            }
        );
}


function handleBrowserLocation(position) {

    const latitude =
        position.coords.latitude;

    const longitude =
        position.coords.longitude;

    const accuracy =
        position.coords.accuracy;

    const speed =
        position.coords.speed;

    const heading =
        position.coords.heading;


    processLocation(
        latitude,
        longitude,
        accuracy,
        speed,
        heading
    );
}


function processLocation(
    latitude,
    longitude,
    accuracy,
    speed,
    heading
) {

    const location = {

        latitude,
        longitude,
        accuracy,
        speed,
        heading,

        source:
            usingTelegramLocation
                ? "telegram"
                : "browser",

        timestamp:
            Date.now()
    };


    console.log(
        "[LOCATION]",
        location
    );


    displayLocation(location);


    sendLocationIfNeeded(location);
}


function sendLocationIfNeeded(location) {

    const now = Date.now();


    if (
        now - lastSentTime <
        CONFIG.SEND_INTERVAL
    ) {

        return;
    }


    lastSentTime = now;


    if (
        typeof window.sendLocation ===
        "function"
    ) {

        window.sendLocation(location);
    }
}


function stopTracking() {

    tracking = false;


    if (browserWatchId !== null) {

        navigator.geolocation.clearWatch(
            browserWatchId
        );

        browserWatchId = null;
    }


    usingTelegramLocation = false;

    console.log(
        "[LOCATION] Tracking stopped"
    );
}