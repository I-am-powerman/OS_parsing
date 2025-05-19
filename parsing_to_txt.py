import os

class parsing_to_txt():
    max_path = {}
    cickle_iter = 0

    def __init__(self, original_path: str):
        self.original_path :str = original_path

    def read_file(self, path: str):
        if os.path.isdir(path):
            list_directory = os.listdir(path)
            for i in range(len(list_directory)):
                print(self.cickle_iter)
                print(ord(path))
                self.read_file(path + "/" + list_directory[i])
                self.cickle_iter += 1
        else:
            self.max_path[path] = path
        
    
    def txt_max_path(self):
       self.read_file(self.original_path)
       max_keys = max(self.max_path.keys())
       print(self.max_path)
       return self.max_path[max_keys]
    
    def write_path(self):
        pass

"""нужно убрать повторения"""
