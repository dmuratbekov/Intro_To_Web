// ex1:
let fruits = [];

fruits.push("Apple");
fruits.push("Banana");
fruits.push("Cherry");

let removed = fruits.pop();

console.log(fruits);
console.log("Removed:", removed);


// ex2:
let numbers = [10, 20, 30, 40, 50];

let part = numbers.slice(1, 4);
console.log("Sliced part:", part);
console.log("Original numbers:", numbers);


// ex3:
const nums = [1, 2, 3, 4, 5];
const squared = nums.map(n => n * n);

console.log("Original nums:", nums);
console.log("Squared nums:", squared);


// ex4:
const ages = [12, 18, 25, 30, 15];
const adults = ages.filter(a => a >= 18);

console.log("Filtered:", adults);


// ex5:
const user = {
    name: "Alice",
    age: 25,
    city: "New York"
};

console.log("User name:", user.name);

user.age = 26;
console.log("Updated user:", user);


// ex6:
const car = { brand: "Tesla", model: "Model S", year: 2023 };

console.log("Keys:", Object.keys(car));
console.log("Values:", Object.values(car));