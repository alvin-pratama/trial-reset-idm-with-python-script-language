import sys, winreg, time
print("""
####### program trial reset IDM #######
=======================================
Output:""")

def uninstaller_cleanup():
    if sys.platform == 'win32':
        try:
            with winreg.OpenKey(winreg.HKEY_USERS, r'S-1-5-21-775043431-2979447631-1580498678-1001_Classes\WOW6432Node\CLSID', access=winreg.KEY_WRITE) as reg:
                winreg.DeleteKey(reg, '{07999AC3-058B-40BF-984F-69EB1E554CA7}')
                print("> deleted key successfully!")
        except FileNotFoundError:
            # pass
            print("> not found key!")
        except KeyboardInterrupt:
            print("> keyboard interrupt!")
        except Exception as e:
            print("> problems detected, please check the errors!")
    else:
        print("> problems detected, program runing on win32 only!")

uninstaller_cleanup()

time.sleep(3)
input("\npress anykey to close...")