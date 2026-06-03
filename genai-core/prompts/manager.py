from jinja2 import Template
from .loader import PromptLoader

class PromptManager:

    def __init__(
        self,
        template_dir="templates"
    ):
        
        self.loader = PromptLoader(
            template_dir
        )

    def render(
        self,
        template_path: str,
        **kwargs
    ) -> str:
        
        template_content = self.loader.load(template_path)

        template = Template(template_content)

        return template.render(**kwargs)