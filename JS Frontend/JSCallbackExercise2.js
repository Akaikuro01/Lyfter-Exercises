const fs = require('fs');

let data1 = '';
let data2 = '';
let done = 0;
let wordsMatching = [];

function filesLoaded(compareFiles) {
    done++;
    if (done === 2) {
        compareFiles(data1, data2);
    }
}

function compareFiles(data1, data2) {
    const words1 = data1.split("\r\n");
    const words2 = data2.split("\r\n");

    for (const word of words1) {
        for (const word2 of words2) {
            if (word === word2) {
                wordsMatching.push(word);
                break;
            }
        }
    }

    console.log("The next words repeat in both files: " + wordsMatching);
}

const logData1 = (err, data) => {
	data1 = data;
    filesLoaded(compareFiles);
}

const logData2 = (err, data) => {
	data2 = data;
    filesLoaded(compareFiles);
}

fs.readFile('file1.txt', 'utf8', logData1);
console.log("Reading file1.txt!.")
fs.readFile('file2.txt', 'utf8', logData2);
console.log("Reading file2.txt!.")