# figuring out rprint
from rich import print as rprint

sample = [[['blue', 'apple'], ['green', 'leaves'], ['purple', 'shirt']],
          [['yellow', 'orange'], ['red', 'blood'], ['black', 'charcoal']]]

for info in sample:
    rprint(' ['+ info[0][0] +'] '+ info[0][1] + 
           ' ['+ info[1][0] +'] '+ info[1][1] + 
           ' ['+ info[2][0] +'] '+ info[2][1])