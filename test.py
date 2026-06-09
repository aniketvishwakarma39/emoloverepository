from emotionweb import Surprise

s = Surprise(
    type="love",
    name="Aniket",
    message="You are my world ❤️",
    images=[
        "1.jpg",
        "2.jpg",
        "3.jpg",
        "4.jpg",
        "5.jpg",
        "6.jpg",
        "7.jpg",
        "8.jpg"
    ]
)

s.generate()
