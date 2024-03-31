from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from langchain.llms import CTransformers
from langchain.prompts import PromptTemplate
import os
import logging

load_dotenv()
API_TOKEN=os.getenv("TOKEN")
logging.basicConfig(level=logging.INFO)

def getLLamaresponse(text):

    ### LLama2 model
    llm=CTransformers(model=r"C:\Users\Siddhant\Documents\\Running-Llama2-on-CPU-Machine\\model\\llama-2-7b-chat.ggmlv3.q4_1.bin",    # give your model path here
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})
    template="You are a helpful agent. Reply to the following message to the best of your knowledge. {question}"
    prompt=PromptTemplate(input_variables=["question"],template=template)
    response=llm(prompt.format(question=text))
    return response

bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)
@dp.message_handler(commands=['start','help'])
async def command_start_handler(message: types.Message):
    await message.reply("HI I am an AI bot built by Sid")

@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(getLLamaresponse(message.text))

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)