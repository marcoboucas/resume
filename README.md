# Marco Boucas' Resume

This repository contains the source code for my personal resume. It is automatically generated using Python, Jinja2, and WeasyPrint.

## Features

*   **Multilingual:** The resume is available in English and French.
*   **Automated Generation:** The HTML and PDF files are generated automatically from a single HTML template and a set of CSS files.
*   **CI/CD:** A GitHub Actions workflow automatically generates and uploads the PDF files as artifacts whenever new changes are pushed to the repository.

## Project Structure

The project is structured as follows:

```
.
├── assets
│   ├── flags
│   ├── lato
│   └── raleway
├── output
├── .github
│   └── workflows
│       └── generate_pdf.yml
├── cv.html
├── font.css
├── generate_html_documents.py
├── generate_pdfs.py
├── Makefile
├── README.md
├── requirements.txt
└── style.css
```

*   **`assets/`**: Contains all the assets used in the resume, such as fonts, images, and flags.
*   **`output/`**: Contains the generated HTML and PDF files.
*   **`.github/`**: Contains the GitHub Actions workflow.
*   **`cv.html`**: The Jinja2 template for the resume.
*   **`font.css`**: The CSS file for the fonts.
*   **`generate_html_documents.py`**: A Python script that generates the HTML files for each language.
*   **`generate_pdfs.py`**: A Python script that generates the PDF files from the HTML files.
*   **`Makefile`**: A Makefile that contains commands to generate the resume.
*   **`README.md`**: This file.
*   **`requirements.txt`**: The Python dependencies.
*   **`style.css`**: The main CSS file for the resume.

## Usage

To generate the resume, you need to have Python 3 and pip installed.

1.  Clone the repository:

    ```bash
    git clone https://github.com/marcoboucas/resume.git
    ```

2.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    Note: If you have an error related to weasyprint on macos, please install it using brew `brew install weasyprint`

3.  Generate the resume:

    ```bash
    make
    ```

    This will generate the HTML and PDF files in the `output` directory.

## CI/CD

The project uses GitHub Actions to automatically generate the resume whenever new changes are pushed to the repository. The workflow is defined in the `.github/workflows/generate_pdf.yml` file.

The workflow does the following:

1.  Checks out the code from the repository.
2.  Sets up Python.
3.  Installs the dependencies.
4.  Generates the HTML and PDF files.
5.  Uploads the generated PDF files as artifacts.