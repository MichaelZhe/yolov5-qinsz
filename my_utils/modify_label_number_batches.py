import os


def replace_numbers(file_path, number):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        parts = line.split()
        if parts and parts[0].isdigit():
            parts[0] = f"{number}"
        modified_lines.append(' '.join(parts))

    with open(file_path, 'w') as file:
        content = "\n".join(modified_lines)
        file.write(content)


def replace_numbers_in_folder(folder_path, number):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            replace_numbers(file_path, number)


if __name__ == '__main__':
    folder_path = '/Users/qinshengzhe/Desktop/Git_Repositories/Python/assets/fire-third-80/labels/val'
    replace_numbers_in_folder(folder_path, 80)