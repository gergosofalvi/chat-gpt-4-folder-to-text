Folder to Text Converter
========================

This Python script is designed to convert the contents of a directory into a single text file that can be uploaded to GPT-4 for processing. It provides a convenient way to share and collaborate on complete projects as a single file with the GPT model.

Usage
-----

1.  Install the required packages:
```bash
pip install tqdm
```
3.  Run the script with the following command:
```bash
python3 folder-to-text.py <directory path> <output file name>
```
*   `<directory path>`: The path to the directory you want to convert (e.g., /Users/username/Documents/project/).
*   `<output file name>`: The desired name of the output text file (without the .txt extension, e.g., project).

6.  The script will generate a text file containing the directory structure and the contents of text-based files. Non-text files will be excluded from processing.
7.  Optionally, you can specify excluded files and folders by modifying the `exclude` variable in the script. Use a comma to separate multiple excluded file and folder names.
8.  A progress bar will indicate the processing status, and the script will display the total number of files found and the ones that could not be processed.

Example
-------

To convert a directory located at '/Users/username/Documents/project/' into a text file named 'project.txt', run the following command:
```bash
python3 folder-to-text.py /Users/username/Documents/project/ project
```
Excluded Files and Folders
--------------------------

By default, the script excludes the following files and folders:

*   `node_modules/`
*   `.git/`
*   `build`
*   `test`
*   `.gitignore`
*   `.DS_Store`

You can customize the list of excluded files and folders by modifying the `exclude` variable in the script.

Limitations
-----------

This script only processes text-based files and may not work with binary or non-standard file formats.
