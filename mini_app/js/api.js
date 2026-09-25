async function sendLocationToServer(locationData) {

    const url = `${CONFIG.API_BASE_URL}/api/location`;

    try {

        const response = await fetch(url, {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(locationData)
        });


        if (!response.ok) {

            throw new Error(
                `Server returned ${response.status}`
            );
        }


        const result = await response.json();

        console.log(
            "[API] Location sent:",
            result
        );


        return result;

    } catch (error) {

        console.error(
            "[API] Failed to send location:",
            error
        );

        throw error;
    }
}