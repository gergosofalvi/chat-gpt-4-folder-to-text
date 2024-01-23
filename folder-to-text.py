import os
import sys
from tqdm import tqdm
from multiprocessing import Pool

def process_file(file_path):
    failed_files = []
    try:
        with open(file_path, 'r', encoding='utf-8') as input_file:
            content = input_file.read()
        return file_path, content, None
    except UnicodeDecodeError:
        failed_files.append(file_path)
        return file_path, None, "Failed to decode the file, as it is not saved with UTF-8 encoding."

def write_directory_structure_to_file(directory_path, output_file_name, exclude=[]):
    total_files = 0
    copied_files = 0

    file_list = []
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)

            exclude_file = False
            for ex in exclude:
                if ex in file_path:
                    exclude_file = True
                    break

            if not exclude_file:
                file_list.append(file_path)

    with open(output_file_name, 'w', encoding='utf-8') as output_file:
        with Pool() as pool:
            results = list(tqdm(pool.imap(process_file, file_list), total=len(file_list), desc="Progress", unit=" file"))

        for result in results:
            total_files += 1
            if result[1] is not None:
                file_name_line = f"--- START FILE: {result[0]} ---\n"
                output_file.write(file_name_line)
                output_file.write(result[1] + "\n")
                end_line = f"--- END FILE: {result[0]} ---\n"
                output_file.write(end_line)
                copied_files += 1
            if result[2] is not None:
                output_file.write(f"{result[0]}\n{result[2]}\n")

    return total_files, copied_files

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 folder-to-text.py <directory path> <output file name>")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_file_name = sys.argv[2] + ".txt"

    exclude = ["node_modules/", ".git/", "build", "test", ".gitignore", ".DS_Store", ".jpg", ".png", ".svg"]

    total_files, copied_files = write_directory_structure_to_file(input_directory, output_file_name, exclude)

    print(f"There are a total of {total_files} files in the {input_directory} directory.")
    print(f"A total of {copied_files} files have been copied to {output_file_name}.")
