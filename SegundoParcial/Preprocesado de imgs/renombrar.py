import os

class BatchRename():
    def __init__(self, folder_path):
        self.path = folder_path

    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        i = 1

        for item in filelist:
            if item.endswith('.jpg'):
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), f'{i}.jpg')
                try:
                    os.rename(src, dst)
                    print(f'Renaming {src} to {dst} ...')
                    i += 1
                except:
                    continue

        print(f'Total {total_num} files renamed to {i-1} jpgs')

if __name__ == '__main__':
    folder_path = f'D:\Trabajos\IA 2 - 2023-2\segundoParcial\webroboflow'
    renamer = BatchRename(folder_path)
    renamer.rename()