import os

def check_folder(folder):
    try:
        if not(os.path.isdir(folder)):
            os.makedirs(os.path.join(folder))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print(folder + ' 폴더를 생성하지 못 했습니다.')
            raise
        return False
    return True
