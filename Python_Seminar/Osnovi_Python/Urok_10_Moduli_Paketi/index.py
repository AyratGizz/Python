import moda
from folderb.modb import foo, bar  # так как в  подпапке, то указываем её (folderb)
# import modc
from modc import foo

# moda
print(moda.foo)
moda.bar()
# modb
print(foo)
bar()
