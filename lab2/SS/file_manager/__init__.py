"""File manager init file for ex8."""
class FileManager:

    def read_file(source):
        """Read and print file whose source was given as argument."""
        with open(source, 'r', encoding='utf-8') as file:
            print(file.read())
            # for line in file:
            #     print(line.replace('\n', ''))
    
    def update_file(source, text_data):
        """Append text_data at the end of source data."""
        with open(source, 'a', encoding='utf-8') as file:
            file.write('\n')
            file.write(text_data)

