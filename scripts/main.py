from logger import get_loader_by_name
import os

pipeline_logging = get_loader_by_name(loader_name="pipeline", file_name="pipeline.logs")

class DataLoader:
    def __init__(self, file_path:str):
        self.file_path = os.path.join(file_path)
        pipeline_logging.info(f"Starting with the file path: {self.file_path}")

    def fetch(self,file_name):
        full_file_name = os.path.join(self.file_path,file_name)
        if not os.path.exists(full_file_name):
            pipeline_logging.error(f"File Not Found path: {full_file_name}")
            return None
        try:
            with open(full_file_name,'r') as file:
                data = file.read()
                pipeline_logging.info(f"Data is loaded successfully with {len(data)} lines.")

        except Exception as e:
            pipeline_logging.error(
                f"System error in opening the file {full_file_name}: {e}.\
                \nMay be file doesn't exist or opening mode is not correct.")





if __name__ == "__main__":
    data_loader = DataLoader("data_files")
    data_loader.fetch("students.csv")

