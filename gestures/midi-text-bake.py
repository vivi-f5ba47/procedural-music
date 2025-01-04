import os
import sys

if __name__ == "__main__":
    folder = os.path.realpath("./midi")

    files = [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

    for fi in files: 
        print(fi)

        with open(fi, "rb") as midi:
            while byte := midi.read(1):
                try: 
                    msg = int.from_bytes(byte, byteorder="big")
                    print(msg)
                except UnicodeDecodeError: 
                    print(" ")
        
        break