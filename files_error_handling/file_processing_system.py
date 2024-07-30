import file_handler
from file_operations import write_file, read_file


def main():
    file_path = input("Enter the file path: ")
    file_mode = input("Enter the file mode: ")
    file = file_handler.file_handler(file_path, file_mode)
    file_name = file.args[0]

    if file_mode == "w":
        content = input("Enter the file content: ")
        write_file(file_name, content, file_mode)
    elif file_mode == "r":
        print(read_file(file_name, file_mode))
    else:
        raise ""


if __name__ == "__main__":
    main()