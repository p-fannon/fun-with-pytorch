from fastapi import FastAPI
from nbconvert import HTMLExporter
from fastapi.responses import HTMLResponse
import nbformat

app = FastAPI()


def convert_notebook_to_html(notebook_path):
	with open(notebook_path) as f:
		nb = nbformat.read(f, as_version=4)
		html_exporter = HTMLExporter()
		# html_exporter.template_file = 'basic'
		(body, resources) = html_exporter.from_notebook_node(nb)
		return body

@app.get("/")
def serve_notebook():
	html_content = convert_notebook_to_html('linear model using autograd.ipynb')
	return HTMLResponse(content=html_content, status_code=200)