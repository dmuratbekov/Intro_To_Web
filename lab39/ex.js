// ex1:
console.log("Start");

setTimeout(() => {
    console.log("Inside setTimeout");
}, 2000);

console.log("End");


// ex2:
function delayedMessage(message, delay) {
    setTimeout(() => {
        console.log(message);
    }, delay);
}

delayedMessage("Hello, after 3 seconds!", 3000);


// ex3:
function startCounter() {
    let count = 1;

    const timer = setInterval(() => {
        console.log("Counter:", count);

        if (count === 5) {
            clearInterval(timer);
        }

        count++;
    }, 1000);
}

startCounter();


// ex4:
function fetchDataSuccess() {
    return new Promise((resolve) => {
        setTimeout(() => resolve("Data received"), 2000);
    });
}

fetchDataSuccess()
    .then((result) => console.log(result))
    .finally(() => console.log("Request completed"));


// ex5:
function fetchData() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (Math.random() > 0.5) {
                resolve("Data received");
            } else {
                reject("Error: Failed to fetch data");
            }
        }, 2000);
    });
}

fetchData()
    .then((result) => console.log(result))
    .catch((err) => console.error(err))
    .finally(() => console.log("Request completed"));