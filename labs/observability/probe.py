"""One HTTP observation, not an availability monitoring system."""
import sys
import time
from urllib.request import urlopen
from urllib.error import URLError

url = sys.argv[1] if len(sys.argv) > 1 else 'http://127.0.0.1:8000/health'
start = time.monotonic()
try:
    with urlopen(url, timeout=3) as response:
        print(f'status={response.status} duration_ms={(time.monotonic()-start)*1000:.1f}')
except URLError as exc:
    print(f'probe_failed={exc} duration_ms={(time.monotonic()-start)*1000:.1f}', file=sys.stderr)
    sys.exit(1)
