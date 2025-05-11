import os
from jinja2 import Environment, FileSystemLoader

def render_saft_xml(context):
    template_path = os.path.join(os.path.dirname(__file__), "templates")
    env = Environment(loader=FileSystemLoader(template_path))
    template = env.get_template("saft_template.xml.jinja")
    return template.render(context)
