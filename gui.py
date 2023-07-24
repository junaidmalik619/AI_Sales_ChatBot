import asyncio
import tkinter as tk
from rasa.core.agent import Agent
from rasa.utils.endpoints import EndpointConfig

class ChatApplication:
    def __init__(self, master=None):
        self.master = master
        self.text_widget = tk.Text(self.master)
        self.text_widget.pack()
        self.entry_widget = tk.Entry(self.master)
        self.entry_widget.pack()
        self.entry_widget.bind("<Return>", self.send_message)

    async def load_agent(self):
        model_path = '<path_to_your_model>'
        self.agent = await Agent.load(model_path, action_endpoint=EndpointConfig('http://localhost:5055/webhook'))

    async def send_message(self, event):
        message = self.entry_widget.get()
        self.text_widget.insert(tk.END, f'You: {message}\n')
        self.entry_widget.delete(0, tk.END)
        response = await self.agent.handle_text(message)
        self.text_widget.insert(tk.END, f'Bot: {response[0].get("text")}\n')

    async def run(self):
        await self.load_agent()

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApplication(master=root)
    asyncio.run(app.run())
    root.mainloop()
