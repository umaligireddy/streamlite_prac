def mock_chatgpt(prompts):
    return ("this is a fake prompt answer")
prompts = ["what is your name", "what are you trying to get",
     "what is you goel","what is the next step",
     "my final step"]
with open("chat_log1.txt","x",encoding="utf-8") as log_file:
    for i , prompt in enumerate(prompts):
        print(f"prompt {i+1}: {prompt}")
        response = mock_chatgpt(prompts)
        print("respomse", response)

        log_file.write(f"prompt {i+1}:{prompt}")
        log_file.write(f"\nresponse: {response}\n")
