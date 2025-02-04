import asyncio
from datetime import datetime
from utils import send_call

async def main():
    """Here is an example of how to simulate an outbound call:"""
    metadata_to_display = {
        'scheduledAt': datetime.now().isoformat(),
    }
    await send_call('1', metadata_to_display)

if __name__ == '__main__':
    asyncio.run(main()) 