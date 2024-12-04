import json


class CommonUtils:
    def __init__(self, project_id=None):
        self.project_id = project_id

    @staticmethod
    def load_json_from_file(file_path):
        with open(file_path) as f:
            return json.loads(f.read())

