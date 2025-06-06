import sys

try:
    from urllib3.packages import six

    sys.modules.setdefault("urllib3.packages.six.moves", six.moves)
except Exception:
    pass
