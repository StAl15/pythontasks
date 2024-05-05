import pickle
import zlib

from kvstorage.service.Storage import Storage
from kvstorage.utils.file_handler.FileHandler import FileHandler
from utils.arguments_parser.ArgumentParser import ArgumentParser

arg_parser = ArgumentParser()
print("""
     __      __       .__                                       __                    _____  .____     _______________  ___       ____  __.____   ____
/  \    /  \ ____ |  |   ____  ____   _____   ____        _/  |_  ____           /  _  \ |    |    \_   _____/\   \/  /      |    |/ _|\   \ /   /
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \       \   __\/  _ \         /  /_\  \|    |     |    __)_  \     /       |      <   \   Y   / 
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/        |  | (  <_> )       /    |    \    |___  |        \ /     \       |    |  \   \     /  
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >       |__|  \____/        \____|__  /_______ \/_______  //___/\  \      |____|__ \   \___/   
       \/       \/          \/            \/     \/                                    \/        \/        \/       \_/              \/           
""")

while True:
    args = arg_parser.parser.parse_args(input().strip().split()).__dict__
    func = args['func']
    del args['func']
    func(**args)

# fh = FileHandler()
# store = Storage()
# # store.set_value_to_store("test", "fourth", "adis abebra")
# store.get_value_from_store("test", "fourth")


