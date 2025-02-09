//adding
const addButton = document.getElementById("button_add");
const inputField = document.querySelector(".add_task input");

//items
const itemsContainer = document.querySelector(".items");

//adding
function addTask() {
    const taskText = inputField.value;
    if (taskText === "") {
        return;
    }

    const taskItem = document.createElement("div");
    taskItem.classList.add("item");

    const doneButton = document.createElement("button");
    doneButton.textContent = "✓";
    doneButton.classList.add("button_done");
    const taskInput = document.createElement("input");
    taskInput.type = "text";
    taskInput.value = taskText;
    const deleteButton = document.createElement("button");
    deleteButton.textContent = "✗";
    deleteButton.classList.add("button_delete");


    taskItem.appendChild(doneButton);
    taskItem.appendChild(taskInput);
    taskItem.appendChild(deleteButton);
    itemsContainer.appendChild(taskItem);


    inputField.value = "";

    
    doneButton.addEventListener("click", function () {
        toggleTaskDone(taskInput);
    });
    deleteButton.addEventListener("click", function () {
        deleteTask(taskItem);
    });
}

addButton.addEventListener("click", function () {
    addTask();
});
inputField.addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        addTask();
    }
});


//item
function toggleTaskDone(taskInput) {
    taskInput.classList.toggle("completed");
}
function deleteTask(taskItem) {
    taskItem.remove();
}