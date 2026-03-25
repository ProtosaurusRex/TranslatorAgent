from dotenv import load_dotenv
from agents import Agent, Runner
import asyncio


load_dotenv()

# 1. Define specialized agents first
spanish_agent = Agent(
    name="spanish_agent",
    instructions="You translate the user's message to Spanish."
)

german_agent = Agent(
    name="german_agent",
    instructions="You translate the user's message to German."
)

mandarin_chinese_agent = Agent(
    name="mandarin_chinese_agent",
    instructions="You translate the user's message to Mandarin Chinese. Use transliterated pinyin in parentheses after the Chinese characters to show pronunciation."
)

saudi_arabic_agent = Agent(
    name="saudi_arabic_agent",
    instructions="You translate the user's message to Saudi Arabic. Use transliterated Arabic in parentheses after the Arabic script to show pronunciation."
)

thai_agent = Agent(
    name="thai_agent",
    instructions="You translate the user's message to Thai. Use transliterated Thai in parentheses after the Thai script to show pronunciation."
)

triage_agent = Agent(
    name="Triage Agent",
    instructions="You determine which agent to use based on the user's phrase they want to translate",
    handoffs=[spanish_agent, german_agent, mandarin_chinese_agent, saudi_arabic_agent, thai_agent]
)

async def main():
    # Example 1: Spanish translation
    result = await Runner.run(triage_agent, "Translate 'Hello, how are you?' to Spanish.")
    print(result.final_output)

    # Example 2: German translation
    result = await Runner.run(triage_agent, "Translate 'Good morning, have a nice day!' to German.")
    print(result.final_output)

    # Example 3: Mandarin Chinese translation
    result = await Runner.run(triage_agent, "Translate 'Good morning, have a nice day!' to Mandarin Chinese.")
    print(result.final_output)

    # Example 4: Saudi Arabic translation
    result = await Runner.run(triage_agent, "Translate 'Good morning, have a nice day!' to Saudi Arabic.")
    print(result.final_output)

    # Example 5: Thai translation
    result = await Runner.run(triage_agent, "Translate 'Good morning, have a nice day!' to Thai.")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())