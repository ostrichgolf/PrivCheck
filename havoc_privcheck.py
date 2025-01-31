from havoc import Demon, RegisterCommand, RegisterModule

def all(demonID, *param):
    TaskID: str = None
    demon: Demon = None

    demon = Demon(demonID)

    if demon.ProcessArch == "x86":
        demon.ConsoleWrite(demon.CONSOLE_ERROR, "x86 is not supported")
        return False

    TaskID = demon.ConsoleWrite(
        demon.CONSOLE_TASK,
        "Executing all checks"
    )

    demon.InlineExecute(TaskID, "go", "output/alwaysinstallelevated.x64.o", b'', False)
    demon.InlineExecute(TaskID, "go", "output/autologon.x64.o", b'', False)
    demon.InlineExecute(TaskID, "go", "output/credentialmanager.x64.o", b'', False)
    demon.InlineExecute(TaskID, "go", "output/hijackablepath.x64.o", b'', False)
    demon.InlineExecute(TaskID, "go", "output/tokenprivileges.x64.o", b'', False)
    demon.InlineExecute(TaskID, "go", "output/unattendfiles.x64.o", b'', False)
    demon.InlineExecute(TaskID, "go", "output/unquotedsvcpath.x64.o", b'', False)
    demon.InlineExecute(TaskID, "go", "output/vulnerabledrivers.x64.o", b'', False)

    return TaskID




def alwaysinstallelevated(demonID, *param):
    TaskID: str = None
    demon: Demon = None

    demon = Demon(demonID)

    if demon.ProcessArch == "x86":
        demon.ConsoleWrite(demon.CONSOLE_ERROR, "x86 is not supported")
        return False

    TaskID = demon.ConsoleWrite(
        demon.CONSOLE_TASK,
        "Tasked demon to check if always install elevated is enabled"
    )

    demon.InlineExecute(TaskID, "go", "output/alwaysinstallelevated.x64.o", b'', False)

    return TaskID

def autologon(demonID, *param):
    TaskID: str = None
    demon: Demon = None

    demon = Demon(demonID)

    if demon.ProcessArch == "x86":
        demon.ConsoleWrite(demon.CONSOLE_ERROR, "x86 is not supported")
        return False

    TaskID = demon.ConsoleWrite(
        demon.CONSOLE_TASK,
        "Tasked demon to look for autologon information"
    )

    demon.InlineExecute(TaskID, "go", "output/autologon.x64.o", b'', False)

    return TaskID

def credentialmanager(demonID, *param):
    TaskID: str = None
    demon: Demon = None

    demon = Demon(demonID)

    if demon.ProcessArch == "x86":
        demon.ConsoleWrite(demon.CONSOLE_ERROR, "x86 is not supported")
        return False

    TaskID = demon.ConsoleWrite(
        demon.CONSOLE_TASK,
        "Tasked demon to check the credential manager"
    )

    demon.InlineExecute(TaskID, "go", "output/credentialmanager.x64.o", b'', False)

    return TaskID

def hijackablepath(demonID, *param):
    TaskID: str = None
    demon: Demon = None

    demon = Demon(demonID)

    if demon.ProcessArch == "x86":
        demon.ConsoleWrite(demon.CONSOLE_ERROR, "x86 is not supported")
        return False

    TaskID = demon.ConsoleWrite(
        demon.CONSOLE_TASK,
        "Tasked demon to look for writable directories in the path variable"
    )

    demon.InlineExecute(TaskID, "go", "output/hijackablepath.x64.o", b'', False)

    return TaskID

def tokenprivileges(demonID, *param):
    TaskID: str = None
    demon: Demon = None

    demon = Demon(demonID)

    if demon.ProcessArch == "x86":
        demon.ConsoleWrite(demon.CONSOLE_ERROR, "x86 is not supported")
        return False

    TaskID = demon.ConsoleWrite(
        demon.CONSOLE_TASK,
        "Tasked demon to check the current token privileges"
    )

    demon.InlineExecute(TaskID, "go", "output/tokenprivileges.x64.o", b'', False)

    return TaskID

def unattendfiles(demonID, *param):
    TaskID: str = None
    demon: Demon = None

    demon = Demon(demonID)

    if demon.ProcessArch == "x86":
        demon.ConsoleWrite(demon.CONSOLE_ERROR, "x86 is not supported")
        return False

    TaskID = demon.ConsoleWrite(
        demon.CONSOLE_TASK,
        "Tasked demon to look for unattend installation files on the system"
    )

    demon.InlineExecute(TaskID, "go", "output/unattendfiles.x64.o", b'', False)

    return TaskID

def unquotedsvc(demonID, *param):
    TaskID: str = None
    demon: Demon = None

    demon = Demon(demonID)

    if demon.ProcessArch == "x86":
        demon.ConsoleWrite(demon.CONSOLE_ERROR, "x86 is not supported")
        return False

    TaskID = demon.ConsoleWrite(
        demon.CONSOLE_TASK,
        "Tasked demon to check for unquoted service paths"
    )

    demon.InlineExecute(TaskID, "go", "output/unquotedsvcpath.x64.o", b'', False)

    return TaskID

def vulnerabledrivers(demonID, *param):
    TaskID: str = None
    demon: Demon = None

    demon = Demon(demonID)

    if demon.ProcessArch == "x86":
        demon.ConsoleWrite(demon.CONSOLE_ERROR, "x86 is not supported")
        return False

    TaskID = demon.ConsoleWrite(
        demon.CONSOLE_TASK,
        "Tasked demon to enumerate drivers against known vulnerable ones"
    )

    demon.InlineExecute(TaskID, "go", "output/vulnerabledrivers.x64.o", b'', False)

    return TaskID

RegisterModule(
    "privcheck",
    "A module which assists you in finding common privesc methods",
    "",
    "[subcommand]",
    "",
    ""
)

RegisterCommand(all, "privcheck", "all", "execute all checks in module", 0, "", "")
RegisterCommand(alwaysinstallelevated, "privcheck", "alwayselevated", "check if always install elevated is enabled", 0, "", "")
RegisterCommand(autologon, "privcheck", "autologon", "check the registry for autologon information", 0, "", "")
RegisterCommand(credentialmanager, "privcheck", "credman", "check the credential manager for saved credentials", 0, "", "")
RegisterCommand(hijackablepath, "privcheck", "hijackablepath", "check for writable directories in the path environment variable", 0, "", "")
RegisterCommand(tokenprivileges, "privcheck", "tokenpriv", "check the current token privileges", 0, "", "")
RegisterCommand(unattendfiles, "privcheck", "unattendfiles", "check for leftover unattend files", 0, "", "")
RegisterCommand(unquotedsvc, "privcheck", "unquotedsvc", "check for unquoted service paths", 0, "", "")
RegisterCommand(vulnerabledrivers, "privcheck", "vulndrivers", "check the system for known vulnerable drivers", 0, "", "")
