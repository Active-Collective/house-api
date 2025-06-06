"""Compatibility helpers loaded automatically by Python."""

import sys
import types
import http.client

try:
    from urllib3.packages import six
except Exception:
    # Older ``urllib3`` releases may not bundle ``six`` when built for newer
    # Python versions. Fall back to the standalone ``six`` package if present.
    try:  # pragma: no cover - optional dependency
        import six  # type: ignore
    except Exception:  # pragma: no cover - ``six`` not installed
        six = None  # type: ignore

if six is not None:  # pragma: no cover - executed when ``six`` is available
    # Ensure ``urllib3.packages.six.moves`` and the ``http_client`` module exist
    sys.modules.setdefault(
        "urllib3.packages.six", types.ModuleType("urllib3.packages.six")
    )
    moves = types.ModuleType("urllib3.packages.six.moves")
    # Populate moves with attributes from ``six.moves``
    for attr in dir(six.moves):
        setattr(moves, attr, getattr(six.moves, attr))
    sys.modules.setdefault("urllib3.packages.six.moves", moves)
    # Provide the specific submodule required by ``urllib3``
    sys.modules.setdefault("urllib3.packages.six.moves.http_client", http.client)
