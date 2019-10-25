import signal

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
        self.b.close()
        await self.a.shutdown()
