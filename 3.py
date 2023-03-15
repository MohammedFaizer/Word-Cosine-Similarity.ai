import openai
openai.api_key = "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"

# define a function to generate a response
def generate_response(prompt):
    response = openai.Completion.create(
        engine="s",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# main loop
while True:
    # get a message from the user
    message = input("You: ")
    # generate a response from ChatGPT
    response = generate_response(message)
    # print the response
    print("ChatGPT:", response)
