import asyncio

async def do_other_things(delay):
    print(f"doing other things {delay} start")    
    await asyncio.sleep(delay)
    print(f"doing other things {delay}")
    return delay
