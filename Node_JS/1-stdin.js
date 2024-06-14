// Program that excutes through command line

process.stdout.write('Welcome to Holberton School, what is your name?\n')
process.stdin.setEncoding('utf8');
process.stdin.on('data', (data) => {
    const word = data.trim();

    if (word.toLowerCase() === 'end' || word.toLowerCase() === 'exit' || word.toLowerCase() === 'close') {
        process.stdout.write('This important software is now closing\n')
        process.exit()
    }
    else if(word === ''){
        process.stdout.write('Please enter your name\n')
    } else {
        process.stdout.write(`Your name is: ${word}\n`);
    }
});

process.on('SIGINT', () => {
    process.stdout.write('This important software is now closing\n')
    process.exit()
});
