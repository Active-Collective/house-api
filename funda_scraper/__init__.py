"""Expose the public scraper API and apply compatibility fixes."""

import sys

try:  # pragma: no cover - safeguard for urllib3 import issues
    from urllib3.packages import six

    sys.modules.setdefault("urllib3.packages.six.moves", six.moves)
except Exception:  # pragma: no cover - ignore if urllib3 internals change
    pass

from funda_scraper.scrape import FundaScraper
from funda_scraper.extract import DataExtractor

__all__ = ["FundaScraper", "DataExtractor"]
