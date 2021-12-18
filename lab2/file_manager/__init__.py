class FileManager:

    def read_file(source):
        with open(source, 'r', encoding='utf-8') as file:
            print(file.read())
            file.close()
    
    def update_file(source, text_data):
        """Append text_data at the end of source data."""
        with open(source, 'a', encoding='utf-8') as file:
            file.write('\n')
            file.write(text_data)
            file.close()

