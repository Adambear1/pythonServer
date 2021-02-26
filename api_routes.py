from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi
import format_data as routes


class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        taskList = routes.GatherData()._get()
        if self.path.endswith("/tasklist"):
            self.send_response(200)
            self.send_header("content-type", "text/html")
            self.end_headers()
            output = ''
            output += '<html><body>'
            output += '<h1>Task List</h1>'
            output += '<h3><a href="/tasklist/new">Add New Task</a></h3>'
            for task in taskList:
                output += task
                output += '<a href="/tasklist/%s/remove">Delete</a>' % task
                output += '<a href="/tasklist/%s/update">Update</a>' % task
                output += "</br>"
            output += "</body></html>"
            self.wfile.write(output.encode())
        if self.path.endswith("/new"):
            self.send_response(200)
            self.send_header("content-type", "text/html")
            self.end_headers()
            output = ''
            output += '<html><body>'
            output += '<h1>Add New Task</h1>'
            output += '<form method="POST" enctype="multipart/form-data" action="/tasklist/new">'
            output += '<input name="task" type="text" placeholder="Add New Task">'
            output += '<input type="submit" value="Add">'
            output += '</form>'
            output += '</body></html>'
            self.wfile.write(output.encode())

        if self.path.endswith("/remove"):
            listIDPath = self.path.split("/")[2]
            self.send_response(200)
            self.send_header("content-type", "text/html")
            self.end_headers()
            output = ""
            output += "<html><body>"
            output += "<h1>Remove Task: %s</h1>" % listIDPath.replace(
                "%20", " ")
            output += "<form method='POST' enctype='multipart/form-data' action='/tasklist/%s/remove'>" % listIDPath
            output += "<input type='submit' value='Remove'>"
            output += "</form>"
            output += '<a href="/tasklist">Cancel</a>'
            output += "</body></html>"
            self.wfile.write(output.encode())

        if self.path.endswith("/update"):
            listIDPath = self.path.split("/")[2]
            self.send_response(200)
            self.send_header("content-type", "text/html")
            self.end_headers()
            output = ""
            output += "<html><body>"
            output += "<h1>Update Task: %s</h1>" % listIDPath.replace(
                "%20", " ")
            output += "<form method='POST' enctype='multipart/form-data' action='/tasklist/%s/update'>" % listIDPath
            output += '<input name="update" type="text" value="%s">' % listIDPath.replace(
                "%20", " ")
            output += "<input type='submit' value='Update'>"
            output += "</form>"
            output += '<a href="/tasklist">Cancel</a>'
            output += "</body></html>"
            self.wfile.write(output.encode())

    def do_POST(self):
        if self.path.endswith("/new"):
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            content_len = int(self.headers.get('Content-length'))
            pdict['CONTENT-LENGTH'] = content_len
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                new_task = fields.get('task')
                routes.GatherData()._add(new_task[0])

        self.send_response(301)
        self.send_header("content-type", "text/html")
        self.send_header('Location', '/tasklist')
        self.end_headers()

        if self.path.endswith("/remove"):
            listIDPath = self.path.split("/")[2]
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            if ctype == "multipart/form-data":
                list_item = listIDPath.replace("%20", " ")
                routes.GatherData()._remove(list_item)

            self.send_response(301)
            self.send_header("content-type", "text/html")
            self.send_header('Location', '/tasklist')
            self.end_headers()

        if self.path.endswith("/update"):
            listIDPath = self.path.split("/")[2]
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            content_len = int(self.headers.get('Content-length'))
            pdict['CONTENT-LENGTH'] = content_len
            if ctype == "multipart/form-data":
                fields = cgi.parse_multipart(self.rfile, pdict)
                routes.GatherData()._update(listIDPath.replace(
                    "%20", " "), fields.get('update')[0])

            self.send_response(301)
            self.send_header("content-type", "text/html")
            self.send_header('Location', '/tasklist')
            self.end_headers()
