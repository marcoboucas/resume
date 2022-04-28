from jinja2 import Template


def main():
    """Generate the CV page for different languages."""

    with open('cv.html', "r", encoding="utf-8") as _:
        text = _.read()
    template = Template(text)

    for language in ['fr', "en"]:
        with open(f'cv_{language}.html', "w", encoding="utf-8") as _:
            _.write(
                template.render(
                    language=language,
                    fr=language == "fr",
                    en=language == "en"
                )
            )


if __name__ == "__main__":
    main()
