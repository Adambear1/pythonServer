import html_render as render
from io import StringIO
import format_data as routes


class renderFile():
    @staticmethod
    def return_page():
        with open("test.html", "r", encoding='utf-8') as f:
            text = f.read()
            return text

    @staticmethod
    def homepage():
        taskList = routes.GatherData()._get()
        output = render.Html()
        header = render.Head()
        header.append(render.Meta(charset="UTF-8"))
        header.append(render.Title("Task List"))
        output.append(header)
        body = render.Body()
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
        render.render_page(output, "index.html")
