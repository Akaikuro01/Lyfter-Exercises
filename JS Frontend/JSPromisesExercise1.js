async function runPromises() {
    try {
        const promise1 = fetch("https://pokeapi.co/api/v2/pokemon/4").then(r => r.json());
        const promise2 = fetch("https://pokeapi.co/api/v2/pokemon/5").then(r => r.json());
        const promise3 = fetch("https://pokeapi.co/api/v2/pokemon/6").then(r => r.json());

        const pokemons = await Promise.all([promise1, promise2, promise3]);
        console.log(pokemons[0].name, pokemons[1].name, pokemons[2].name);
        
    } catch (error) {
        console.error(error);
    }
}

runPromises();
