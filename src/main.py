import asyncio
from datetime import datetime
from utils import send_call

async def main():
    """Main function to demonstrate send_call functionality."""
    # Call send_call three times with different jobId
    await send_call('1', {'scheduledAt': datetime.now().isoformat()})
    await send_call('2', {'scheduledAt': datetime.now().isoformat()})
    await send_call('3', {'scheduledAt': datetime.now().isoformat()})

if __name__ == '__main__':
    asyncio.run(main()) 