import glob
import os
from os.path import dirname, isfile


def __list_all_modules():
    work_dir = dirname(__file__)
    # Cross-platform glob for subpackages' python files
    mod_paths = glob.glob(os.path.join(work_dir, "*", "*.py"))

    all_modules = []
    for f in mod_paths:
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py"):
            # Get path relative to plugins dir (starts with path separator)
            rel = f[len(work_dir):]
            # Normalize both Windows and POSIX separators to dots
            rel = rel.replace("\\", ".").replace("/", ".")
            # Ensure leading dot, strip .py
            module = rel[:-3] if rel.startswith(".") else "." + rel[:-3]
            all_modules.append(module)

    return all_modules


ALL_MODULES = sorted(__list_all_modules())
__all__ = ALL_MODULES + ["ALL_MODULES"]
