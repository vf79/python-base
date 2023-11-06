from textual.app import App


class Colors(App):

    async def on_load(self, event):
        await self.bind("r", "color('red')")
        await self.bind("g", "color('green')")
        await self.bind("b", "color('blue')")
        await self.bind("q", "quit")

    async def action_color(self, color: str):
        self.background = f"on {color}"


if __name__ == "__main__":
    app = Colors()
    app.run()
