from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
import logging
logging.basicConfig(level=logging.WARNING)
font_config = FontConfiguration()
import os
from pathlib import Path
from jinja2 import Template
import shutil


OUTPUT_DIR = Path('./output').resolve()

def generate_html(language: str) -> None:
    # Load the HTML template
    with open(os.path.join(os.path.dirname(__file__), 'cv.html'), "r", encoding="utf-8") as _:
        text = _.read()
    template = Template(text)

    with open(os.path.join(OUTPUT_DIR, f'cv_{language}.html'), "w", encoding="utf-8") as _:
        _.write(
            template.render(
                language=language,
                **{
                   language: True
                }
            )
        )

def generate_pdf(language: str) -> None:
    html_path = Path(OUTPUT_DIR, f'cv_{language}.html')
    if not html_path.exists():
        raise FileNotFoundError(f"{html_path} does not exist. Please run generate_html_documents.py first.")

    with open(html_path, "r") as file:
        html = HTML(
            string=file.read(),
            base_url=os.getcwd()
        )
    pdf_path = OUTPUT_DIR / f'resume_{language}.pdf'
    html.write_pdf(
        pdf_path.resolve(),
        stylesheets=[],
        font_config=font_config, zoom=2, presentational_hints=True
    )


def main(language: str) -> None:
    generate_html(language)
    generate_pdf(language)


if __name__ == "__main__":

    # Change working directory to the output folder
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    os.chdir(OUTPUT_DIR)
    for lang in ['fr', 'en']:
        main(lang)