from cx_Freeze import setup, Executable

setup(
	name="DemoPywin",
    version="0.0.1",
    description="Demo Application",
    executables=[Executable(
    	"main.py",
    	shortcut_name="Demo",
        shortcut_dir="DesktopFolder",
    )],
)
