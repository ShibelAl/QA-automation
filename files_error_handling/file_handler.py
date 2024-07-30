from contextlib import contextmanager
from file_processing_error import FileProcessingError


@contextmanager
def file_handler(file_path, mode):
    try:
        # Open the file and yield the file object
        file = open(file_path, mode)
        yield file  # Like return but with more options
    except FileNotFoundError:
        raise FileProcessingError(f"File not found: {file_path}")
    except PermissionError:
        raise FileProcessingError(f"Permission error occurred while accessing the file: {file_path}")
    except IOError as e:
        raise FileProcessingError(f"IO error occurred while accessing the file: {e}")
    finally:
        # Ensure the file is closed properly
        file.close()