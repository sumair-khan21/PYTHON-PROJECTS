import chainlit as cl

@cl.on_message
# cl.message is a decorator that is used to listen to the message event ye ek class hai jo chat ki life cycle ko manage karegi
async def main(message: cl.Message):
    # message is a class that is used to store the message data
    # .content is a property that is used to store the message content
    response = f"You Said: {message.content}"
    # ye .send ka function hai jo chat ki life cycle ko manage karegi
    await cl.Message(content=response).send()