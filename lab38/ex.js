// ex1:
function parseJSON(jsonStr) {
    try {
        const result = JSON.parse(jsonStr);
        console.log("Parsed object:", result);
    } catch (error) {
        console.error("Invalid JSON format");
    }
}

parseJSON('{"name":"John","age":30}');
parseJSON('{name:John}');


// ex2:
let numbers = [10, 15, 20, 25, 30];
let sum = 0;

for (let num of numbers) {
    console.log("Current number:", num);
    if (num % 2 == 0) {
        sum += num;
    }
}
console.log("Total sum of even numbers:", sum);


// ex3:
let users = [
    { name: "Alice", age: 25 },
    { name: "Bob", age: 30 },
    { name: "Charlie", age: 22 }
];

console.table(users);


// ex4:
function divide(a, b) {
    try {
        if (b === 0) {
            throw new Error("Cannot divide by zero");
        }
        return a / b;
    } catch (error) {
        console.error(error.message);
    }
}

console.log(divide(10, 2));
console.log(divide(10, 0));


// ex5:
try {
    console.log(myVariable);
} catch (error) {
    console.error("Variable is not defined");
}