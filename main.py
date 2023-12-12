from openai import OpenAI
client = OpenAI(api_key="")

assistant = client.beta.assistants.create(
    name="Math teacher",
    instructions="You are personal math tutor. Write and run code to answer math questions",
    model="gpt-3.5-turbo"
)

thread = client.beta.threads.create()
print(thread)

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Solve this problem: 3x + 11 = 14"
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

