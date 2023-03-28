from flask import Flask, render_template, request
from flask import current_app as app
import chardet

app = Flask(__name__)

# An API endpoint to read the contents from a given text file
@app.route('/files')
@app.route('/files/<filename>/', methods=["GET"])
def display_file(filename='file1.txt'):
    """
    Read the contents of a text file and return them as a list of lines.
    The filename can be specified in the URL path or as a query parameter.
    Optional query parameters 'start_line' and 'end_line' can be used to
    retrieve only a subset of the lines.
    """
    app.logger.info("Functionality : Read File Contents")

    # Get the start_line and end_line query parameters, if provided by the user and accept only if it is an integer value.
    # If the user provides string or float it would be considered as none and whole file will get read.
    start_line = request.args.get('start_line', type=int)
    end_line = request.args.get('end_line', type=int)

    try:
        # Detects the encoding of the file
        with open(f"files/{filename}", 'rb') as f:
            result = chardet.detect(f.read())
            encoding = result['encoding']

        # Opens the file and read its contents
        with open(f'files/{filename}', 'r', encoding=encoding) as f:
            content = f.readlines()

            # Filter the lines based on the start_line and end_line parameters
            if start_line is not None and end_line is not None:
                content = content[start_line :end_line + 1]
            elif start_line is not None:
                content = content[start_line :]
            elif end_line is not None:
                content = content[:end_line + 1]

    except FileNotFoundError:
        # Handles the case where the file is not found
        error = f"File '{filename}' not found"
        return render_template('error.html', lines=[], error = error)
    
    except Exception as e:
        # Handles any other exceptions that occur while reading the file
        error=f"An error occurred while processing file '{filename}': {str(e)}"
        return render_template('error.html', lines=[], error=error)

    # Render the file.html template with the file contents
    return render_template('file.html', lines=content)

if __name__ == '__main__':
    app.run()
