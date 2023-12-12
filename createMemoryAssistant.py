from openai import OpenAI
client = OpenAI(api_key="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")

assistant = client.beta.assistants.create(
    name="Reminder",
    instructions="You are personal assistant for people with bad memory. They can tell you their age for example and you will remember this informatin and tell them when they will ask you.",
    model="gpt-3.5-turbo"
)

thread = client.beta.threads.create()
print("Thread: ", thread, "Assistant: ", assistant)

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Hello my name is Jan and my age is 31"
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

