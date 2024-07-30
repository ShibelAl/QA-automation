from file_processing_error import FileProcessingError


def read_file(file_path, mode):
    try:
        with open(file_path, mode) as file:
            content = file.read()
        return content
    except FileNotFoundError:
        raise FileProcessingError(f"File not found: {file_path}")
    except IOError as e:
        raise FileProcessingError(f"IO error occurred while reading the file: {e}")


def write_file(file_path, content, mode):
    try:
        with open(file_path, mode) as file:
            file.write(content)
    except PermissionError:
        raise FileProcessingError(f"Permission error occurred while accessing the file: {file_path}")
    except IOError as e:
        raise FileProcessingError(f"IO error occurred while writing to the file: {e}")
    else:
        print("File written successfully.")