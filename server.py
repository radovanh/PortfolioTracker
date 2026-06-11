#!/usr/bin/env python3
"""Pay & Pray — local dev server. Run: python server.py"""
import http.server, os, webbrowser
from pathlib import Path

PORT = 8765
APP_DIR = Path(__file__).parent

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw): super().__init__(*a, directory=str(APP_DIR), **kw)
    def do_GET(self):
        if self.path == '/': self.path = '/index.html'
        super().do_GET()
    def log_message(self, fmt, *a): pass   # silent

if __name__ == '__main__':
    os.chdir(APP_DIR)
    print(f'  Pay & Pray  →  http://localhost:{PORT}')
    print('  Ctrl+C to stop')
    webbrowser.open(f'http://localhost:{PORT}')
    http.server.HTTPServer(('localhost', PORT), Handler).serve_forever()
