import json
import webbrowser
import shutil
import os

class Surprise:

    def __init__(
        self,
        type,
        name,
        message,
        images,
        caption,
    ):

        self.type = type
        self.name = name
        self.message = message
        self.images = images
        self.caption= caption

    def generate(self):

        upload_folder = (
            "webengine/static/uploads"
        )

        os.makedirs(
            upload_folder,
            exist_ok=True
        )

        copied = []

        for i,image in enumerate(self.images):

            ext = image.split(".")[-1]

            new_name = f"img{i+1}.{ext}"

            shutil.copy(
                image,
                f"{upload_folder}/{new_name}"
            )

            copied.append(
                new_name
            )

        data = {
            "type": self.type,
            "name":self.name,

            "message":self.message,

            "images":copied,
            "caption":self.caption,
        }

        with open(
            "data.json",
            "w"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

        webbrowser.open(
            "http://127.0.0.1:1214"
        )

        print(
            "Website generated successfully!"
        )
