function counter() {
    let count = 0;

    return function () {
        count++;
        return count;
    };
}

const counter1 = counter();
const counter2 = counter();

for (let i = 0; i < 5; i++) {
    counter1();
    counter2();
    counter1();
}

console.log("counter2:");
console.log("counter1:");