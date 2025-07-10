import readline from 'readline';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

rl.question('Enter a word: ', async (word) => {
    if (word) {
        const { capitalize } = await import('./stringUtils.js');
        console.log(`Capitalized: ${capitalize(word)}`);
    } else {
        console.log('No word entered.');
    }
    rl.close();
});