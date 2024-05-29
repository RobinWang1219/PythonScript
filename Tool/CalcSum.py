import getopt,sys,os
from pathlib import Path

def convert_path(path):
    return path.replace(r'\/'.replace(os.sep, ''), os.sep)
    
# buffersize = 0x2000000
def main(arg):
    crcvalue = 0
    file_path = ' '
    
    file_path = convert_path(arg)
    FILE_PATH =Path(file_path)
    FILE_SIZE =os.path.getsize(file_path)
    if FILE_PATH.exists():
        with open(FILE_PATH, 'rb') as afile:
            buffr = afile.read(FILE_SIZE)
            crcvalue = sum(buffr)

    print('0x'+(format(crcvalue & 0xFFFFFFFF, '08x')).upper()) # a509ae4b

if __name__ == "__main__":
    main(sys.argv[1])
