import sys, winreg, time, os
print("""
####### program delay update IDM to disable popup serial key #######
========================================""")

# data = input("masukkan bulan/tanggal/tahun seperti format berikut (30/12/99): ")
data = input("enter the year like the following format (2099 -> 99): ")

print("""location idm installed:
:[1] Program Files
:[2] Program Files (x86)""")
installation_location_IDM = input("enter number location IDM installed (1 or 2): ")

def uninstaller_cleanup(data, location):
    if sys.platform == 'win32' or sys.platform == 'windows':
        try:
            print('\noutput: ')
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\DownloadManager', 0, winreg.KEY_SET_VALUE) as reg:
                winreg.SetValueEx(reg, 'LstCheck', 0, winreg.REG_SZ, f'09/01/{data}')
                winreg.SetValueEx(reg, 'CheckUpdtVM', 0, winreg.REG_SZ, '0')
                print("> updated key successfully!")

            idm_grep_helper = 'IDMGrHlp.exe'
            idm_broker = 'idmBroker.exe'
            if location == 1:
                loc_path_idm = 'Program Files'
                path = f'C:\\{loc_path_idm}\\Internet Download Manager'
                # print(path)
                if os.path.isdir(f'{path}'):
                    if os.path.isfile(f'{path}\\{idm_grep_helper}'):
                        os.rename(f'{path}\\{idm_grep_helper}', f'{path}\\{idm_grep_helper}.bak')
                    else:
                        pass
                    if os.path.isfile(f'{path}\\{idm_broker}'):
                        os.rename(f'{path}\\{idm_broker}', f'{path}\\{idm_broker}.bak')
                    else:
                        pass
                    print("> file update completed!")
                else:
                    print("> errors directory IDM not found!")
            elif location == 2:
                loc_path_idm = 'Program Files (x86)'
                path = f'C:\\{loc_path_idm}\\Internet Download Manager'
                if os.path.isdir(f'{path}'):
                    if os.path.isfile(f'{path}\\{idm_grep_helper}'):
                        os.rename(f'{path}\\{idm_grep_helper}', f'{path}\\{idm_grep_helper}.bak')
                    else:
                        pass
                    if os.path.isfile(f'{path}\\{idm_broker}'):
                        os.rename(f'{path}\\{idm_broker}', f'{path}\\{idm_broker}.bak')
                    else:
                        pass
                    print("> file update completed!")
                else:
                    print("> errors directory IDM not found!")
        except FileNotFoundError:
            print("> not found key!")
        except KeyboardInterrupt:
            print("> keyboard interrupt!")
        except Exception as e:
            print("> problems detected, please check the errors!")
    else:
        print("> problems detected, program runing on win32 only!")

uninstaller_cleanup(data, int(installation_location_IDM))

time.sleep(3)
input("\npress anykey to close...")