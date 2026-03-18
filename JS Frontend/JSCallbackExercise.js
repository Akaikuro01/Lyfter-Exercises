function checkNumber(number, isEven, isOdd) {
    if (number % 2 === 0) {
        isEven();
    }
    else {
        isOdd();
    }
}

function isEven () {
    console.log("The number is even!.")
}

function isOdd () {
    console.log("The number is odd!.")
}

checkNumber(2, isEven, isOdd);


