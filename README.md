# Web Metadata Retrieval API

Setup:

1. Clone the repository
    ```cmd
    git clone https://github.com/WebMetadataRetrieval/15-Web_Metadata_Retrieval.git
    ```
2. Create Virtual Environment
    ```cmd
    cd 15-Web_Metadata_Retrieval\Code
    virtualenv venv
    cd venv
    scripts\activate
    ```
3. Install Required Packages
    ```cmd
    pip install -r requirements.txt
    ```
4. Run Server
    ```cmd
    cd src
    python manage.py collectstatic
    python manage.py runserver
    ```
