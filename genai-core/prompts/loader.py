from pathlib import Path
from .exceptions import PromptNotFoundError

class PromptLoader:
    
    def __init__(
        self,
        template_dir="templates"
    ):
        
        self.template_dir = Path(template_dir)

    def load(
        self,
        template_path: str
    ) -> str:
        
        path = (self.template_dir / template_path)

        if not path.exists():

            raise PromptNotFoundError(f"Prompt not found: {path}")
        
        return path.read_text(encoding="utf-8")