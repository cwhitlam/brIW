import src.core.db as database
from http.server import BaseHTTPRequestHandler, HTTPServer
from src.core.round import Round, Order
import json
from src.core.accessor import Accessor
from src.api.encoder import MyEncoder


class PersonPageHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def _get_person_html(self):
        try:
            f = open("/home/chris/repos/miniproject/src/dynamic_website/person_page.html", "r")
            return f.read()
        except:
            print("Failed to open html file")
            return ""

    def _get_main_css(self):
        try:
            f = open("/home/chris/repos/miniproject/src/dynamic_website/main.css", "r")
            return f.read()
        except:
            print("Failed to open css file")
            return ""

    def _create_html_table_contents(self, table_contents, object_attributes):
        html_text = ""
        for row in table_contents.values():
            row_text = "<tr>"
            for index in range(0, len(object_attributes)):
                cell_text = str(getattr(row, object_attributes[index]))
                html_cell = f"<td>{cell_text}</td>"
                row_text += html_cell
            row_text += "</td>"
            html_text += row_text
        return html_text
    
    def _render_page(self, html):
        self.wfile.write(html.encode("utf-8"))

    def _encode_css(self, css):
        output_css = "<script>"
        output_css += f"{css} </script>"
        return output_css

    def do_GET(self):
        self._set_headers()
        acc = Accessor()
        people = acc.get_people()
        html = self._get_person_html()
        css = self._get_main_css()
        object_attributes = ["id", "first_name", "surname", "prefered_drink"]
        table_contents = self._create_html_table_contents(people, object_attributes)
        
        html_document = html.format(
            css = self._encode_css(css),
            table_contents = table_contents
        )

        self._render_page(html_document)

if __name__ == "__main__":
    server_address = ("0.0.0.0", 8080)
    httpd = HTTPServer(server_address, PersonPageHandler)
    print("Starting web page server...")
    httpd.serve_forever()
