# Multi-Agent Chat System (MAS)

class Agent:
    def __init__(self, role):
        self.role = role

    def respond(self, message):
        pass


# -----------------------------
# Researcher Agent
# -----------------------------
class Researcher(Agent):
    def __init__(self):
        super().__init__("Researcher")

    def respond(self, topic):
        research_data = f"Research on '{topic}':\n- Key facts collected\n- Background information gathered\n- Important points identified"
        print(f"\n[{self.role}]: {research_data}")
        return research_data


# -----------------------------
# Writer Agent
# -----------------------------
class Writer(Agent):
    def __init__(self):
        super().__init__("Writer")

    def respond(self, research):
        article = f"Article Draft:\nBased on research, here is a structured content:\n{research}\n\nConclusion: This topic is important and informative."
        print(f"\n[{self.role}]: {article}")
        return article


# -----------------------------
# Reviewer Agent
# -----------------------------
class Reviewer(Agent):
    def __init__(self):
        super().__init__("Reviewer")

    def respond(self, article):
        review = f"Review Feedback:\n- Content is clear\n- Minor improvements needed\n- Grammar is good\n\nFinal Status: Approved ✅"
        print(f"\n[{self.role}]: {review}")
        return review


# -----------------------------
# Chat System Controller
# -----------------------------
class ChatMAS:
    def __init__(self):
        self.researcher = Researcher()
        self.writer = Writer()
        self.reviewer = Reviewer()

    def start(self):
        print("=== Multi-Agent Chat System ===")
        
        topic = input("\nEnter a topic: ")

        # Step 1: Researcher works
        research_output = self.researcher.respond(topic)

        # Step 2: Writer works
        article_output = self.writer.respond(research_output)

        # Step 3: Reviewer works
        review_output = self.reviewer.respond(article_output)

        print("\n=== Process Completed ===")


# -----------------------------
# Run Program
# -----------------------------
if __name__ == "__main__":
    system = ChatMAS()
    system.start()