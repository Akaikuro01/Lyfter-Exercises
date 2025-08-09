from flask import Flask, request, jsonify
import data_handling
import json

app = Flask(__name__)

def get_task_list_file():
    try:
        open_json = data_handling.HandleJson("tasks.json")
        tasks_list = open_json.read_json()
        return tasks_list
    except FileNotFoundError as ex:
        return jsonify({"message": f"File not found: {ex}"}), 404
    except PermissionError as ex:
        return jsonify({"message": f"Permission denied: {ex}"}), 403
    except json.JSONDecodeError as ex:
        return jsonify({"message": f"Invalid JSON format: {ex}"}), 400
    except Exception as ex:
        return jsonify({"message": f"Unexpected error: {ex}"}), 500

def save_task_list_file(tasks_list):
    try:
        save_json = data_handling.HandleJson("tasks.json")
        save_json.write_json(tasks_list)
    except FileNotFoundError as ex:
        return jsonify({"message": f"File not found: {ex}"}), 404
    except PermissionError as ex:
        return jsonify({"message": f"Permission denied: {ex}"}), 403
    except json.JSONDecodeError as ex:
        return jsonify({"message": f"Invalid JSON format: {ex}"}), 400
    except Exception as ex:
        return jsonify({"message": f"Unexpected error: {ex}"}), 500

def check_existing_id(tasks_list, id):
    for task in tasks_list:
        if task["id"] == id:
            return True
        else:
            return False

tasks_list = get_task_list_file()



@app.route("/tasks")
def list_all_tasks():
    try:
        filtered_tasks = tasks_list
        task_filter = request.args.get("status")
        if task_filter:
            filtered_tasks = list(
                filter(lambda show: show["status"] == task_filter, filtered_tasks)
            )
        return filtered_tasks
    except ValueError as ex:
        return jsonify(message=str(ex)), 400
    except Exception as ex:
        return jsonify(message=str(ex)), 400


@app.route("/register", methods=["POST"])
def add_new_task():
    try:
        if "status" not in request.json:
            raise ValueError("error: Status required.")
        if "title" not in request.json:
            raise ValueError("error: title required.")
        if "id" not in request.json:
            raise ValueError("error: id required.")
        if "description" not in request.json:
            raise ValueError("error: description required.")

        if check_existing_id(tasks_list, int(request.json["id"])):
            raise ValueError("error: Task id already exists.")

        if request.json["status"] not in ["Completed", "In progress", "Pending"]:
            raise ValueError("error: Invalid status entered.")

        tasks_list.append(
            {
                "id": request.json["id"],
                "title": request.json["title"],
                "description": request.json["description"],
                "status": request.json["status"]
            }
        )

        save_task_list_file(tasks_list)
        return tasks_list
    except ValueError as ex:
        return jsonify(message=str(ex)), 400
    except Exception as ex:
        return jsonify(message=str(ex)), 400

# Modifying using put and path parameters
@app.route("/<int:task_id>", methods=["PUT"])
def modify_tasks(task_id):
    try:
        idx_to_modify = -1
        for index, task in enumerate(tasks_list):
            if task["id"] == task_id:
                idx_to_modify = index
                break
        
        if idx_to_modify == -1:
            return jsonify({"error": "Task not found"})
        else:
            if "status" not in request.json:
                return jsonify({"error": "Status required."})
            if "title" not in request.json:
                return jsonify({"error": "Title required."})
            if "id" not in request.json:
                return jsonify({"error": "id required."})
            if "description" not in request.json:
                return jsonify({"error": "id description."})
            tasks_list[idx_to_modify] = {
                "id": request.json["id"],
                "title": request.json["title"],
                "description": request.json["description"],
                "status": request.json["status"]
        }
        save_task_list_file(tasks_list)
        return tasks_list
    except ValueError as ex:
        return jsonify(message=str(ex)), 400
    except Exception as ex:
        return jsonify(message=str(ex)), 400

# Deleting using query parameters
@app.route("/delete", methods=["DELETE"])
def delete_task():
    try:
        task_id = int(request.args.get("id"))
        if not task_id:
            raise ValueError("Error: Incorrect id")
        
        idx_to_modify = -1
        for index, task in enumerate(tasks_list):
            if task["id"] == task_id:
                idx_to_modify = index
                break
        
        if idx_to_modify == -1:
            return jsonify({"error": "Task not found"})
        
        tasks_list.pop(idx_to_modify)

        save_task_list_file(tasks_list)
        return tasks_list
    except ValueError as ex:
        return jsonify(message=str(ex)), 400
    except Exception as ex:
        return jsonify(message=str(ex)), 400


if __name__ == "__main__":
    app.run(host="localhost", debug=True)