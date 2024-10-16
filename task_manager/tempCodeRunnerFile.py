def load_tasks(filename="tasks.json"):
    global tasks
    try:
        with open(filename, "r") as file:
            tasks_data = json.load(file)
            tasks = [Task(**task) for task in tasks_data]
    except FileNotFoundError:
        tasks = []