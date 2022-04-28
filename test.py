from weasyprint import HTML, CSS, default_url_fetcher
from weasyprint.text.fonts import FontConfiguration
import reques
font_config = FontConfiguration()
with open('./cv_en.html', "r") as file:
    html = HTML(string=file.read())

"""
css = CSS(string='''
    @font-face {
        font-family: Gentium;
        src: url(http://example.com/fonts/Gentium.otf);
    }
    h1 { font-family: Gentium }''', font_config=font_config)
"""

def my_fetcher(url):
    if url.startswith('graph:'):
        graph_data = map(float, url[6:].split(','))
        return dict(string=generate_graph(graph_data),
                    mime_type='image/png')
    return default_url_fetcher(url)
html.write_pdf(
    'example.pdf', stylesheets=[],
    font_config=font_config,
    base_url=request.build_absolute_uri('/'))