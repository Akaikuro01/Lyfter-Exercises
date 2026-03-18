
const catchButton = document.getElementById('catchButton');
const textInput = document.getElementById("inputText");

async function fetchUser() {
    console.log("1. Sending request");
    try {        
        const inputElement = document.getElementById("myInput");
        const userId = inputElement.value.trim();

        const response = await fetch(`https://reqres.in/api/users/${userId}`, {
            headers: {
                "x-api-key": "reqres_9eadd5193dff42ce87cf12ae48d022e1",
                "accept": "application/json",
                "user-agent": "reqres-student-exercise/1.0"
            }
        });
        console.log("2. Response received");
        const data = await response.json();

        if (await response.status === 404) {
            textInput.textContent = `User ${userId} does not exist (404)`;
        }

        if (data) {
            console.log("User:", data);
            const name = data.data.first_name;
            const lastName = data.data.last_name;
            const email = data.data.email;
            textInput.textContent = `name: ${name},  Last Name: ${lastName}, Email: ${email}`;
        }
    } catch (error) {
        textInput.textContent = `3. There was a problem: ${error}`
        console.log(`3. There was a problem: ${error}`);
    }
    console.log("4. Await finished");
}

catchButton.addEventListener('click', fetchUser);

console.log("5. Code reached the end");