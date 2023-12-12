from openai import OpenAI
client = OpenAI(api_key="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")

# You will fetch assistant you created earlier
assistant = client.beta.assistants.retrieve(
    assistant_id="asst_UFWDoMMX67OQL8eI8989XkQj"
)
# You will fetch Thread you created earlier
thread = client.beta.threads.retrieve(
    thread_id="thread_h99Q1b2vk3os7wW9Pbm8Womr"
)
print("Thread: ", thread, "Assistant: ", assistant)

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Hello please remind me, what is my name and age?"
)

run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id
)

run = client.beta.threads.runs.retrieve(
    thread_id=thread.id,
    run_id=run.id
)

messages = client.beta.threads.messages.list(
    thread_id=thread.id
)

for message in reversed(messages.data):
    print(message.role + ": " + message.content[0].text.value)

