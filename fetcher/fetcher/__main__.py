import asyncio
import sys

import fetcher.run

if __name__ == "__main__":
    asyncio.run(fetcher.run.main())
    sys.exit()
