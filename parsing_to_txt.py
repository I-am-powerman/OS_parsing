import os

class parsing_to_txt():
    path_docx = {}

    def __init__(self, original_path: str):
        self.original_path :str = original_path
    
    def docx_max_path(self):
       self._read_file(self.original_path)
       max_keys = max(self.path_docx.keys())
       file_max_path = self.path_docx[max_keys]

       return file_max_path
    
    def docx_min_path(self):
       self._read_file(self.original_path)
       min_keys = min(self.path_docx.keys())
       file_min_path = self.path_docx[min_keys]

       return file_min_path
    
    def _read_file(self, path: str):
        if os.path.isdir(path):
            list_directory = os.listdir(path)
            for i in range(len(list_directory)):
                self._read_file(path + "/" + list_directory[i])
        else:
            iter = len(path.split("/"))
            docx = self._write_docx(path)
            self.path_docx[iter] = docx
    
    def _write_docx(self, docx: str) -> str:
        name_docx = docx.split("/")
        name_docx = name_docx[-1]

        return name_docx
