Task: Create Flask application.

Application details:

1. Application should have single GET route.

2. On call to this route application need to read content of given file (see file1.txt.. file4.txt)
and render properly it in HTML page. Any markup should be preserved.files are in English file 4 contains some Chinese

3. Endpoint should accept target file name as optional variable part of URL and default to
file1.txt.

4. Endpoint should accept optional URL query parameters to specify start line number and
end line number. If those parameters present – return only part of file between specified line
numbers. If parameters absent – return all lines.

5. All most likely exceptions in application logic should be handled gracefully. When
exception happens error page should be displayed with exception details.



## Steps to Run the Application :

1. Firstly, Clone the project: 
    - Copy the Github project's URL and clone it to your local machine using Git. You can use the following command in your terminal:
        - git clone <project URL>

2. Now create a virtual environment using the command : python3 -m venv <name of virtualenv>. After that, activate the venv by entering the command venv\Scripts\activate on Windows, or source venv/bin/activate on macOS/Linux.

3. Afterwards , Install dependencies: 
    - Navigate to the project directory and install the required dependencies using pip.
        - cd <project directory>
        - pip install -r requirements.txt

4. Lastly, Run the Flask App :
    - flask run

5. You can either run the API in postman by creating a GET Request and setting the url path or you can also directly open the url in web browser.

