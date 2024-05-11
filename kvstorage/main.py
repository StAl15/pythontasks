import asyncio

from utils.arguments_parser.ArgumentParser import ArgumentParser
from kvstorage.service.Storage import Storage

# arg_parser = ArgumentParser()
print("""
     __      __       .__                                       __                    _____  .____     _______________  ___       ____  __.____   ____
/  \    /  \ ____ |  |   ____  ____   _____   ____        _/  |_  ____           /  _  \ |    |    \_   _____/\   \/  /      |    |/ _|\   \ /   /
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \       \   __\/  _ \         /  /_\  \|    |     |    __)_  \     /       |      <   \   Y   / 
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/        |  | (  <_> )       /    |    \    |___  |        \ /     \       |    |  \   \     /  
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >       |__|  \____/        \____|__  /_______ \/_______  //___/\  \      |____|__ \   \___/   
       \/       \/          \/            \/     \/                                    \/        \/        \/       \_/              \/           
""")

# while True:
#     args = arg_parser.parser.parse_args(input().strip().split()).__dict__
#     func = args['func']
#     del args['func']
#     func(**args)

# fh = FileHandler()
# store = Storage()
# # store.set_value_to_store("test.txt", "fourth", "adis abebra")
# store.get_value_from_store("test.txt", "fourth")

store = Storage(table_name="test")
create_task = asyncio.run(store.set("some", "abebra"))
create_task1 = asyncio.run(store.set("some1", "adis"))
create_task2 = asyncio.run(store.set("some2", "benis"))
create_task3 = asyncio.run(store.set("some3", "denis"))

get_task = asyncio.run(store.get("some"))
get_task1 = asyncio.run(store.get("some1"))
get_task2 = asyncio.run(store.get("some2"))
get_task3 = asyncio.run(store.get("some3"))

print(get_task, get_task1, get_task2, get_task3)
