async function fetchUser() {
    console.log("1. Sending request");
    const user = fetch("https://reqres.in/api/users/23", {
        headers: {
            "x-api-key": "reqres_9eadd5193dff42ce87cf12ae48d022e1",
            "accept": "application/json",
            "user-agent": "reqres-student-exercise/1.0"
        }
    });
    console.log("2. Response received");

    user.then((response) => {
        if (response.status === 404) {
                throw new Error(`User 23 does not exist (404)`);
            }

        response.json().then((data) => {
            if (data)
                console.log("User:", data);
        })
    }).catch((error) => {
            console.log(`3. There was a problem: ${error}`);
        })
}

fetchUser();

console.log("5. Code reached the end");