const taskInput = document.getElementById("taskInput");
const addBtn = document.getElementById("addBtn");
const taskList = document.getElementById("taskList");

let tasks = []; // [{id, text, completed}]

function saveTasks() {
    localStorage.setItem("tasks", JSON.stringify(tasks));
}

function loadTasks() {
    const stored = localStorage.getItem("tasks");
    tasks = stored ? JSON.parse(stored) : [];
}

function renderTasks() {
    taskList.innerHTML = "";

    tasks.forEach(task => {
        const li = document.createElement("li");
        if (task.completed) li.classList.add("completed");

        // text span
        const textSpan = document.createElement("span");
        textSpan.className = "task-text";
        textSpan.textContent = task.text;

        // click to toggle completed
        textSpan.addEventListener("click", () => {
            task.completed = !task.completed;
            saveTasks();
            renderTasks();
        });

        // actions
        const actions = document.createElement("div");
        actions.className = "actions";

        // edit button
        const editBtn = document.createElement("button");
        editBtn.className = "edit-btn";
        editBtn.textContent = "Edit";
        editBtn.addEventListener("click", () => startEdit(li, task));

        // delete button
        const delBtn = document.createElement("button");
        delBtn.className = "del-btn";
        delBtn.textContent = "X";
        delBtn.addEventListener("click", () => {
            tasks = tasks.filter(t => t.id !== task.id);
            saveTasks();
            renderTasks();
        });

        actions.appendChild(editBtn);
        actions.appendChild(delBtn);

        li.appendChild(textSpan);
        li.appendChild(actions);

        taskList.appendChild(li);
    });
}

function addTask() {
    const text = taskInput.value.trim();
    if (text === "") {
        alert("Task cannot be empty!");
        return;
    }

    const newTask = {
        id: Date.now(),
        text,
        completed: false
    };

    tasks.push(newTask);
    taskInput.value = "";
    saveTasks();
    renderTasks();
}

function startEdit(li, task) {
    li.innerHTML = "";

    const editInput = document.createElement("input");
    editInput.type = "text";
    editInput.value = task.text;
    editInput.style.flex = "1";

    const saveBtn = document.createElement("button");
    saveBtn.textContent = "Save";

    const cancelBtn = document.createElement("button");
    cancelBtn.textContent = "Cancel";

    saveBtn.addEventListener("click", () => finishEdit(task, editInput.value));
    cancelBtn.addEventListener("click", () => renderTasks());

    editInput.addEventListener("keydown", (e) => {
        if (e.key === "Enter") finishEdit(task, editInput.value);
    });

    li.appendChild(editInput);
    li.appendChild(saveBtn);
    li.appendChild(cancelBtn);

    editInput.focus();
}

function finishEdit(task, newText) {
    const text = newText.trim();
    if (text === "") {
        alert("Task cannot be empty!");
        return;
    }
    task.text = text;
    saveTasks();
    renderTasks();
}

// Events
addBtn.addEventListener("click", addTask);
taskInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") addTask();
});

// Init
loadTasks();
renderTasks();