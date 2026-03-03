let message = "Hello from global";

function helloGlobal() {
    console.log(message);
}

function helloLocal() {
    let message = "Hello from local";
    console.log(message);
}

helloGlobal();
console.log(message);
helloLocal();
