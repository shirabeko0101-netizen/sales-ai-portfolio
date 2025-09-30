name = input("あなたの名前は？：")
messages = ["Hello, {}!", "Keep going, {}!", "Great job, {}!"]
for i, msg in enumerate(messages, 1):
    print(f"{i}回目:", msg.format(name))
