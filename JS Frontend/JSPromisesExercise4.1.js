async function fetchUser() {
    console.log("1. Enviando request");
    const user = fetch("https://reqres.in/api/users/2", {
        headers: {
            "x-api-key": "reqres_9eadd5193dff42ce87cf12ae48d022e1",
            "accept": "application/json",
            "user-agent": "reqres-student-exercise/1.0"
        }
    });

    user.then((response) => {
        console.log("2. Response recibido");
        response.json().then((data) => {
        console.log(data);
        })
    }).catch((error) => {
        console.log(`3. Hubo un problema: ${error}`);
    })
}

fetchUser();

console.log("5. Codigo llegado al final");