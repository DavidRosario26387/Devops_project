const apiUrl = "http://localhost:5000/tasks";

async function fetchTasks() {
    const res = await fetch(apiUrl);
    const tasks = await res.json();
    const list = document.getElementById("taskList");
    list.innerHTML = "";

    tasks.forEach(task => {
        const li = document.createElement("li");

        const span = document.createElement("span");
        span.textContent = task.task;
        li.appendChild(span);

        // Update button
        const updateBtn = document.createElement("button");
        updateBtn.textContent = "Edit";
        updateBtn.classList.add("update-btn");
        updateBtn.onclick = () => {
            const newTask = prompt("Edit task:", task.task);
            if (newTask) updateTask(task.id, newTask);
        };
        li.appendChild(updateBtn);

        // Delete button
        const delBtn = document.createElement("button");
        delBtn.textContent = "Delete";
        delBtn.onclick = () => deleteTask(task.id);
        li.appendChild(delBtn);

        list.appendChild(li);
    });
}

async function addTask() {
    const input = document.getElementById("taskInput");
    if (!input.value) return;
    await fetch(apiUrl, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ task: input.value })
    });
    input.value = "";
    fetchTasks();
}

async function deleteTask(id) {
    await fetch(`${apiUrl}/${id}`, { method: "DELETE" });
    fetchTasks();
}

async function updateTask(id, newTask) {
    await fetch(`${apiUrl}/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ task: newTask })
    });
    fetchTasks();
}

// Initial fetch
fetchTasks();
