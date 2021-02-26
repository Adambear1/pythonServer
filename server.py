from http.server import HTTPServer, BaseHTTPRequestHandler
import html_render
import api_routes


def main():
    PORT = 8000
    server = HTTPServer(("", PORT), api_routes.requestHandler)
    print('Server running on port %s' % PORT)
    server.serve_forever()


if __name__ == '__main__':
    main()
