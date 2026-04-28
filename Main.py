# Main.py

from Utils.Agents import GroqAgent


def main():
    agent = GroqAgent()
    reply = agent.ask("Explain RAG in simple terms")
    print("\n✅ AI Response:\n")
    print(reply)


if __name__ == "__main__":
    main()


    