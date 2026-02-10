// Exersice 1
const MyArray = [10, 11, 9, 5, 1]

for (const number of MyArray) {
    console.log(number);
}

// Exersice 2
// Solution with "For"
const MyList = [1, 2, 3, 4, 5, 6];
let EvenList = [];
for (let i = 0; i < 6; i++) {
    if (MyList[i] % 2 === 0) {
        EvenList.push(MyList[i])
    }
}

console.log(EvenList)

// Solution with "Filter"
const numbers = [1, 2, 3, 4, 5, 6];
const EvenNumbers = numbers.filter(function (value) {
    if (value % 2 === 0) {
        return value
    }
});

console.log(EvenNumbers);


// Exersice 3
const celsiusTemps = [28, 30, 32, 37, 2000];
const FarenheitTemps = celsiusTemps.map((value) => {
    return value * 1.8 + 32
});

console.log(FarenheitTemps);

// Exersice 4
const string = "I will become the king of the pirates";
const wordList = [];
let word = ""

for (char of string) {
    if (char !== " "){
        word += char;
    }
    else {
        wordList.push(word);
        word = "";
    }
}
wordList.push(word);
console.log(wordList)

// Exersice 5
const student = {
	name: "John Doe",
	grades: [
		{name: "math",grade: 80},
		{name: "science",grade: 100},
		{name: "history",grade: 60},
		{name: "PE",grade: 90},
		{name: "music",grade: 98}
	]
}

let name = student.name;
let gradeAvg = 0;
let highesGrade = "";
let lowestGrade = "";

const gradesList = student.grades;

let maxGrade = 0;
let minGrade = 0;
let addedGrades = 0;

for (let i = 0; i < gradesList.length; i++ ) {
    addedGrades += gradesList[i].grade;

    if (i === 0) {
        maxGrade = gradesList[i].grade;
        minGrade = gradesList[i].grade;
        highesGrade = gradesList[i].name;
        lowestGrade = gradesList[i].name;
    }
    else {
        if (gradesList[i].grade > maxGrade) {
            maxGrade = gradesList[i].grade;
            highesGrade = gradesList[i].name;
        }
        if (gradesList[i].grade < minGrade) {
            minGrade = gradesList[i].grade;
            lowestGrade = gradesList[i].name;
        }
    }
    if (i === (gradesList.length -1))
    {
        gradeAvg = addedGrades/(gradesList.length);
    }
}

const result = {
    name: name,
    gradeAvg: gradeAvg,
    highesGrade: highesGrade,
    lowestGrade: lowestGrade
}

console.log(result)


