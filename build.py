from createindex import createindex
from createpoems import createpoem


createindex()

for i in range(152):
    createpoem(i)
