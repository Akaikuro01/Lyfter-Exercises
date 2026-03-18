async function runPromises() {
    try {
        const sentence = [];

        const promise1 = new Promise((resolve, reject) => {
            setTimeout(() => {
                resolve("very");
            }, 300);
        }).then(word => sentence.push(word));

        const promise2 = new Promise((resolve, reject) => {
            setTimeout(() => {
                resolve("dogs");
            }, 100);
        }).then(word => sentence.push(word));

        const promise3 = new Promise((resolve, reject) => {
            setTimeout(() => {
                resolve("cute");
            }, 400);
        }).then(word => sentence.push(word));

        const promise4 = new Promise((resolve, reject) => {
            setTimeout(() => {
                resolve("are");
            }, 200);
        }).then(word => sentence.push(word));
        

        await Promise.all([promise1, promise2, promise3, promise4]);

        console.log(sentence.join(" "));

    } catch (error) {
        console.error(error);
    }
}

runPromises();