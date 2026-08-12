import sys
import os
import site


"""
VIRTUAL ENVIRONMENT NOTES:

sys:
- Python interpreter/system information.
- sys.executable = path of the Python interpreter currently running.
- sys.prefix = path of the current Python environment.
- sys.base_prefix = path of the original/base Python installation.

os:
- Provides OS-related functions.
- os.path provides path-manipulation functions.
- os.path.basename(path) = gets the last part of a path.
  Example: "/project/matrix_env" -> "matrix_env"

site:
- Provides information about Python package installation.
- site.getsitepackages() = returns site-packages directories(spd).
- The site-packages directory is the default target location where
    Python installs third-party libraries and modules that are not
    part of the standard, core Python distribution.
"""


def display_venv_out() -> None:
    print("\nMATRIX STATUS: You're still plugged in.\n")
    print("Current Python:", sys.executable)
    print("Virtual Environment: None detected\n")
    print("Warning: You're in global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Window")
    print("\nThen run this program again.")


def display_venv_in() -> None:
    print("\nMATRIX STATUS: Welcome to the construct\n")
    print("Current Python:", sys.executable)
    print("Virtual Environment:", os.path.basename(sys.prefix))
    print("Environment Path:", sys.prefix)
    print("\nSUCCESS: You're in an isolated environemnt!")
    print("Safe to install packages without affecting the global system.\n")
    print("Package installation path:", site.getsitepackages())


# hasattr(object, attribute):
# - Checks whether an object has a specific attribute.
# - Returns True or False.
# - hasattr return True if sys has real_prefix or base_prefix
#     attribute.

# VIRTUAL ENVIRONMENT DETECTION:
# - sys.real_prefix: real_prefix is virtual-environment indicator,
#     associated with the older virtualenv mechanism.
# - sys.prefix = path of the current Python environment.
# - sys.base_prefix = path of the original/base Python installation.
# - when outside venv, sys.base_prefix == sys.prefix,
#     when inside venv, sys.base_prefix != sys.prefix.
def main() -> None:
    if (
        hasattr(sys, 'real_prefix')
        or (
            hasattr(sys, 'base_prefix')
            and sys.base_prefix != sys.prefix
        )
    ):
        display_venv_in()
    else:
        display_venv_out()


if __name__ == "__main__":
    main()
