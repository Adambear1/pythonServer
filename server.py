from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi
import html_render
import api_routes

taskList = ['Task 1', 'Task 2', 'Task 3']


def main():
    PORT = 8000
    server = HTTPServer(("", PORT), api_routes.requestHandler)
    print('Server running on port %s' % PORT)
    server.serve_forever()


if __name__ == '__main__':
    main()
