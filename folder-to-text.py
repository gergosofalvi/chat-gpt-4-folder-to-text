import os
import sys
from tqdm import tqdm

def write_directory_structure_to_file(directory_path, output_file_name, failed_files, exclude=[]):
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
        with tqdm(total=len(file_list), desc="Progress", unit=" file") as pbar:
            for file_path in file_list:
                pbar.update(1)
                total_files += 1

                output_file.write(f"{file_path}\n")
                try:
                    with open(file_path, 'r', encoding='utf-8') as input_file:
                        output_file.write(input_file.read())
                    copied_files += 1
                except UnicodeDecodeError:
                    failed_files.append(file_path)
                    output_file.write("Failed to decode the file, as it is not saved with UTF-8 encoding.\n")
                output_file.write("---\n")

    return total_files, copied_files

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 folder-to-text.py <directory path> <output file name>")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_file_name = sys.argv[2] + ".txt"

    exclude = ["node_modules/", ".git/", "build", "test", ".gitignore", ".DS_Store", ".jpg", ".png", ".svg"]

    failed_files = []

    total_files, copied_files = write_directory_structure_to_file(input_directory, output_file_name, failed_files, exclude)

    print(f"There are a total of {total_files} files in the {input_directory} directory.")
    print(f"A total of {copied_files} files have been copied to {output_file_name}.")

    if failed_files:
        print(f"The following files could not be decoded ({len(failed_files)} files):")
        for file_path in failed_files:
            print(file_path)
