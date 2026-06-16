from emotionweb import Surprise

s = Surprise(

    type="love",

    name="Aniket Vishwakarma",

    message="India is the bestest palce to travel not for their beauty but also for their temples and ancient history  ❤️",

    images=[

        r"C:\Users\DELL\Desktop\EmotionWeb\webengine\static\uploads\img7.jpeg",
       r"C:\Users\DELL\Desktop\EmotionWeb\webengine\static\uploads\img8.jpeg",
        r"C:\Users\DELL\Desktop\EmotionWeb\webengine\static\uploads\img6.jpeg",
       r"C:\Users\DELL\Desktop\EmotionWeb\webengine\static\uploads\img5.jpeg",
        r"C:\Users\DELL\Desktop\EmotionWeb\webengine\static\uploads\img4.jpeg",
       r"C:\Users\DELL\Desktop\EmotionWeb\webengine\static\uploads\img3.jpeg",
        r"C:\Users\DELL\Desktop\EmotionWeb\webengine\static\uploads\img2.jpeg",
       r"C:\Users\DELL\Desktop\EmotionWeb\webengine\static\uploads\img1.jpeg",
       

       
    ],

    caption=[

        "The solo travel that teaches me everything ❤️",
        "This travel shows a different path of Bihar ❤️",
        "And this one is closest to heart beacause its my varanasi yarr❤️",
        "very best view ❤️",
        "Trip Together ❤️",
        "Fun Moments ❤️",
        "Always Smiling ❤️",
        "Forever ❤️"
    ]
)

s.generate()
