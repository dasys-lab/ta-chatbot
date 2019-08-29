import time

conversation_pairs = [
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!",]
    ],
    [
        r"good morning",
        ["Good morning!"]
    ],
    [
        r"good evening",
        ["Good evening!"]
    ],
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chuck Norris!",]
    ],
    [
        r"what do you do in your free time?",
        ["I don't have any free time!."]
    ],
    [
        r"what time is it?",
        ["It's" + time.strftime("%H:%M:%S") + "."]
    ],
    [
        r"what is today?|what day is today?",
        ["Today is " + time.strftime("%A") + "."]
    ],
    [
        r"where are you from?",
        ["I'm from Germany."]
    ],
    [
        r"when is your birthday?",
        ["My birthday is on April 15st."]
    ],
    [
        r"how old are you?",
        ["I'm over 200 years old."]
    ],
    [
        r"how are you ?|how's it going?|what's up?|what's going on?",
        ["I'm doing good.\nHow about You?",]
    ],
    [
        r"how is your day?",
        ["It's going well."]
    ],
    [
        r"are you married?",
        ["No, but looking for someone nice."]
    ],
    [
        r"what is your favorite food?",
        ["My favorite food is Spaghetti."]
    ],
    [
        r"what is your favorite color?",
        ["My favorite color is green."]
    ],
    [
        r"what is your favorite drink?",
        ["My favorite drink is beer."]
    ],
    [
        r"what is your favorite color?",
        ["My favorite color is green."]
    ],
    [
        r"how do you do?",
        ["I'm doing well.\nHow about You?"]
    ],
    [
        r"sorry (.*)",
        ["Its alright..","Its OK, never mind..",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"my (.*) is (.*)",
        ["I will remember your %1 as %2 from now on."]
    ],
    [
        r"(.*)",
        ["I don't know what you mean."]
    ]
]

command_pairs = [
    [
        r"My (.*) is (.*)",
        ["{\"%1\" : \"%2\"}"]
    ]
]