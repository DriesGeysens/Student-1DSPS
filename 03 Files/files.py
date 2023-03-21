from pathlib import Path
print(__name__)
if __name__ == "__main__":
   filepath = Path(__file__)
   print(filepath.name)
   print(filepath.suffix)
   print(filepath.stem)