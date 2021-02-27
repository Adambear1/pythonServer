from http.server import HTTPServer, BaseHTTPRequestHandler
import http.server
import cgi
import format_data as routes
import html_outline as html


class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        taskList = routes.GatherData()._get()
        if self.path.endswith("/tasklist"):
            self.send_response(200)
            self.send_header("content-type", "text/html")
            self.end_headers()
            html.renderFile().homepage()
            return self.wfile.write(bytes(html.renderFile().return_page(), "utf8"))
        if self.path.endswith("/new"):
            self.send_response(200)
            self.send_header("content-type", "text/html")
            self.end_headers()
            html.renderFile().newTask()
            return self.wfile.write(bytes(html.renderFile().return_page(), "utf8"))

        if self.path.endswith("/remove"):
            self.send_response(200)
            self.send_header("content-type", "text/html")
            self.end_headers()
            html.renderFile().removeTask(self.path.split("/")[2])
            return self.wfile.write(bytes(html.renderFile().return_page(), "utf8"))

        if self.path.endswith("/update"):
            listIDPath = self.path.split("/")[2]
            self.send_response(200)
            self.send_header("content-type", "text/html")
            self.end_headers()
            html.renderFile().updateTask(self.path.split("/")[2])
            return self.wfile.write(bytes(html.renderFile().return_page(), "utf8"))

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
                print(listIDPath.replace(
                    "%20", " "))
                print(fields.get('update')[0])
                routes.GatherData()._update(listIDPath.replace(
                    "%20", " "), fields.get('update')[0])

            self.send_response(301)
            self.send_header("content-type", "text/html")
            self.send_header('Location', '/tasklist')
            self.end_headers()
