function sum(a, b) {
    return a + b;
}

function greet(a, b) {
    if (a > b) {
        return a;
    } else if (b > a) {
        return b;
    } else {
        return "They are equal";
    }
}

let square = (num) => {
    return num * num;
}

console.log(sum(5, 10));
console.log(square(5));
console.log(greet(5, 10));