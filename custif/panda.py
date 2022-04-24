import pandas as pd
               # aliasing a module

# import ANY kind of data
# pandas will convert your data into a special object
# called a DATAFARME

pokedf= pd.read_csv("pokedex.txt", index_col=1)

# get rid of any duplicate pokemon

pokedf.drop_duplicates()

print(pokedf)
