import os
from glob import glob
import getpass

[os.remove(f) for f in glob.glob(f"C:/Users/{getpass.getuser()}/Documents*.rdp")]
os.system('Reg delete HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Default')
os.system('HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Servers')
