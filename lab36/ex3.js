if (true) {
    var a = "var";
    let b = "let";
    const c = "const";
    console.log("Inside block:", a, b, c);
}

console.log("Outside (var):", a);
console.log("Outside (let):", b);
console.log("Outside (const):", c);