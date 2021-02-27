import html_render as render
from io import StringIO
import format_data as routes
import os


class renderFile():
    @staticmethod
    def return_page():
        with open("index.html", "r", encoding='utf-8') as f:
            return f.read()

    @staticmethod
    def generate_base():
        taskList = routes.GatherData()._get()
        output = render.Html()
        header = render.Head()
        header.append(render.Meta(charset="UTF-8"))
        header.append(render.BootstrapLink())

        header.append(render.Title("Task List"))
        output.append(header)
        body = render.Body()
        return taskList, output, body

    @staticmethod
    def homepage():
        taskList, output, body = renderFile().generate_base()
        body.append(render.H(1, "Task List"))
        body.append(render.A("/tasklist/new", "Add New Task"))
        unorderedList = render.Ul(id="unordered-task-list")
        for task in taskList:
            item = render.Li()
            item.append(task)
            item.append(
                render.A("/tasklist/"+(task).replace(" ", "-")+"/remove", "Delete"))
            item.append(
                render.A("/tasklist/"+(task).replace(" ", "-") + "/update", "Update"))
            item.append(render.Br())
            unorderedList.append(item)
        body.append(unorderedList)
        output.append(body)
        return render.render_page(output, "index.html")

    @staticmethod
    def newTask():
        taskList, output, body = renderFile().generate_base()
        body.append(render.H(1, "Add New Task"))
        body.append(render.Form("/tasklist/new"))
        body.append(render.Input("task"))
        body.append(render.Br())
        body.append(render.P("Add New Task"))
        body.append(render.Br())
        body.append(render.Submit("Add Task"))
        output.append(body)
        return render.render_page(output, "index.html")

    @staticmethod
    def removeTask(input):
        taskList, output, body = renderFile().generate_base()
        body.append(render.H(1, "Remove Task: " + input.replace("-", " ")))
        body.append(render.Form("/task/" + input + "/remove"))
        body.append(render.Submit("Remove", input))
        body.append(render.A("/tasklist", "Cancel"))
        output.append(body)
        return render.render_page(output, "index.html")

    @staticmethod
    def updateTask(input):
        taskList, output, body = renderFile().generate_base()
        body.append(render.H(1, "Update Task: " + input.replace("-", " ")))
        body.append(render.Form("/tasklist/" + input.replace(
            "%20", " ") + "/update"))
        body.append(render.Input("update", input))
        body.append(render.Submit("Update", input))
        body.append(render.A("/tasklist", "Cancel"))
        output.append(body)
        return render.render_page(output, "index.html")
