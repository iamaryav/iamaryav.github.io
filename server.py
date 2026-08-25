import http.server
import socketserver

# Used to locally run the index html
# url: localhost:8000
PORT = 8000


class Handler(http.server.SimpleHTTPRequestHandler):
    """Serves files with caching disabled so edits always show on reload."""

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        super().end_headers()


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    print("Press Ctrl+C to stop the server")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped")
