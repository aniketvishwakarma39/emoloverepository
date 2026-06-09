import json
import webbrowser

class Surprise:

    def __init__(
        self,
        type,
        name,
        message,
        images
    ):

        self.type = type
        self.name = name
        self.message = message
        self.images = images

    def generate(self):

        data = {
            "type": self.type,
            "name": self.name,
            "message": self.message,
            "images": self.images
        }

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

        webbrowser.open("http://127.0.0.1:1214")

        print("Website generated successfully!")
