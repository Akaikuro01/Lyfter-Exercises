async function runPromises() {
    try {
        const promise1 = fetch("https://pokeapi.co/api/v2/pokemon/4").then(r => r.json());
        const promise2 = fetch("https://pokeapi.co/api/v2/pokemon/5").then(r => r.json());
        const promise3 = fetch("https://pokeapi.co/api/v2/pokemon/6").then(r => r.json());

        const firstPokemon = await Promise.any([promise1, promise2, promise3]);
        console.log("First pokemon fulfilled:", firstPokemon.name);
        
    } catch (error) {
        console.error(error);
    }
}

runPromises();