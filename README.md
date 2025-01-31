# PrivCheck

PrivCheck is a collection of Beacon Object Files (BOFs) designed to detect common privilege escalation paths in Windows OS.

It was originally forked from [mertdas/PrivKit](https://github.com/mertdas/PrivKit), which no longer appears to be updated. PrivCheck fixes multiple bugs from the original project and adds new modules for detecting privilege escalation paths.

PrivCheck currently includes the following modules:

| Module              | Description                                                                                                                                                                                                                                                    |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `alwayselevated`    | Checks if `Always Install Elevated` is enabled using the registry.                                                                                                                                                                                             |
| `autologon`         | Checks the registry for autologon information. The original module contained a bug that prevented it from returning any saved password.                                                                                                                        |
| `credman`           | Checks the current user's Windows Credential Manager for saved web passwords and returns them. <br>The original module contained a bug that caused it to only return the first character of the saved password.                                                |
| `hijackablepath`    | Checks the path environment variable for writable directories (`FILE_ADD_FILE`) that can be exploited to elevate privileges. <br>The original module did not work correctly and would simply return the first directory discovered, regardless of permissions. |
| `tokenpriv`         | Lists the current token privileges and highlights known vulnerable ones.                                                                                                                                                                                       |
| `unattendfiles`     | Checks for leftover unattend files that might contain sensitive information *(New module)*.                                                                                                                                                                    |
| `unquotedsvc`       | Checks for unquoted service paths. This module has been updated to display the vulnerable service name and path.                                                                                                                                               |
| `vulnerabledrivers` | Checks if any service on the system uses a known vulnerable driver (based on loldrivers.io). <br>The list of vulnerable drivers is downloaded from loldrivers.io during compilation, then baked into the BOF. Recompile periodically to update *(New module)*. |

All modules have been tested with Havoc and Windows 11 x64.

A Havoc module (`havoc_privcheck.py`) is included to provide easy integration with the Havoc framework. Use `help privcheck` within Havoc to view usage information.

### How to compile
1. `cd` into the project folder.
2. Run `make`. This uses `x86_64-w64-mingw32-gcc` for compilation and `python3` to retrieve the driver list from loldrivers.io.
3. All compiled modules are saved in the `output` folder.
