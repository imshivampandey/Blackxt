# Copyright (C) 2021 KeinShin@Github.


from pathlib import Path
a=Path('exconfig.py').is_file()


if a:
    from exconfig import variable as Variable
else:
    from system.Config.utils import Variable


Variable  = Variable



