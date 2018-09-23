import os

data_save_folder = os.path.join('G:/', 'Estate Agents')


class Grab:
    @staticmethod
    def get_destination_folders():
        return [folder for folder in os.listdir(data_save_folder) if
                folder.startswith('1000') or folder.startswith('HSS')]
