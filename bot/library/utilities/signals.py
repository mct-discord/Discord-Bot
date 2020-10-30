import signal
import asyncio

# TODO: WORK IN PROGRESS
# Class that handles SIGINT and SIGTERM Systemd Service commands


class Signals:
    kill_now = False

    def __init__(self, bot, api):
        self.b = bot
        self.a = api
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    async def exit_gracefully(self, signum, frame):
        self.kill_now = True
        self.b.logout()
        self.b.close()
        await self.a.shutdown()
        # Stop loop:
        self.b.loop.stop()

        # Find all running tasks:
        pending = asyncio.Task.all_tasks()

        # Run loop until tasks done:
        self.b.loop.run_until_complete(asyncio.gather(*pending))
