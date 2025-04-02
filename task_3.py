import sys
from pathlib import Path
from colorama import Fore, Style

def dir_tree(path: Path, level=0):
  
  
  for el in path.iterdir():
    if el.is_dir():
      print(f'{' ' * level}{Fore.BLUE + el.name}')
      dir_tree(el, level +1)
    else:  
      print(f'{' ' * level}{Fore.GREEN + el.name}')


def main():
  if len(sys.argv) >= 2:
    path_dir = sys.argv[1]
    dir_tree(Path(path_dir))
    print (Style.RESET_ALL)    
  else:
    print('Enter valid dir path')

if __name__ == '__main__':
  main()