from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
import logging
logging.basicConfig(level=logging.WARNING)
font_config = FontConfiguration()
import os

def main():
    for language in ["en", "fr"]:
        with open(f'./cv_{language}.html', "r") as file:
            html = HTML(string=file.read(),  base_url=os.path.dirname(os.path.abspath(__file__)))
        html.write_pdf(
            f'resume_{language}.pdf', stylesheets=[],
            font_config=font_config, zoom=2, presentational_hints=True
        )

if __name__ == "__main__":
    main()