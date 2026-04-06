# CLI Task Manager

## Project Vision
A simple CLI-based task manager to practice Python fundamentals and simulate real-world development using Agile Scrum.

---

## Features
- Add task
- View tasks
- Mark task as done
- Delete task
- Edit task
- Save/load tasks to `data.json`
- Input validation and error handling

---

## How It Works

Tasks are stored as JSON objects with two fields:
```json
{ "task": "task name", "mark": false }
```

Data is loaded from `data.json` on startup and saved after every action.

### Functions

| Function | Description |
|---|---|
| `option()` | Displays the styled menu |
| `add_task(user)` | Appends a new task dict to the task list |
| `list_task()` | Prints all tasks with checkmark status |
| `mark_task(user_input)` | Marks a task as done by index |

### Menu Options

| Option | Action |
|---|---|
| 1 | Add Task |
| 2 | View Tasks |
| 3 | Mark Task as Done |
| 4 | Remove Task |
| 5 | Edit Task |
| 6 | Exit |

---

## Sprint Plan

### Sprint 1 — Core Structure
- [x] Add task
- [x] List tasks
- [x] Menu system

### Sprint 2 — Task Status
- [x] Mark task as done

### Sprint 3 — Task Management
- [x] Delete task
- [x] Edit task

### Sprint 4 — Persistence
- [x] Save tasks to `data.json`
- [x] Load tasks from `data.json`

### Sprint 5 — Polish
- [x] Styled box UI with Unicode borders
- [x] Error handling (ValueError, empty input, FileNotFoundError, JSONDecodeError)

---

## Progress Tracker
- [x] Add task
- [x] List tasks
- [x] Menu system
- [x] Mark task as done
- [x] Delete task
- [x] Edit task
- [x] Save tasks
- [x] Load tasks
- [x] Improve UI
- [x] Error handling
