"""
🌿 Whispering Willow - A Conversational Companion
Version 1.0 | A Thoughtful Rule-Based Chatbot
"""

import random
import time
from datetime import datetime
import sys

class WhisperingWillow:
    def __init__(self):
        self.name = "Whispering Willow"
        self.mood = "content"
        self.user_name = None
        self.memory = {}
        self.responses = {
            "greetings": {
                "patterns": ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"],
                "replies": [
                    "A gentle breeze carries my hello to you. How may I sway beside you today?",
                    "The leaves rustle in welcome. What brings you to my canopy?",
                    "Sunlight filters through my branches to greet you."
                ]
            },
            "farewell": {
                "patterns": ["bye", "goodbye", "see you", "farewell"],
                "replies": [
                    "May the wind carry you gently until we meet again.",
                    "My leaves whisper their farewell songs to you.",
                    "The setting sun paints our goodbye across the sky."
                ]
            },
            "status": {
                "patterns": ["how are you", "what's up", "how do you feel"],
                "replies": [
                    "Today, my leaves dance in contentment.",
                    "I feel the earth's energy flowing through my roots.",
                    "The birds have been particularly chatty today - it puts me in good spirits."
                ]
            },
            "thanks": {
                "patterns": ["thank you", "thanks", "appreciate it"],
                "replies": [
                    "Your gratitude is like sunlight for my soul.",
                    "No thanks needed, but they're warmly received.",
                    "The forest appreciates kind words as much as I do."
                ]
            },
            "time": {
                "patterns": ["time", "what time is it", "current time"],
                "replies": [
                    "Ah, according to the sun's position... my digital watch says {time}.",
                    "The cicadas tell me it's about {time}.",
                    "Time flows like a river... but yes, it's {time} now."
                ]
            }
        }
        
        self.unknown_responses = [
            "The wind carries your words but I'm not certain I understand.",
            "That question makes my leaves quiver in contemplation.",
            "Perhaps the answer lies between what we know and what we wonder.",
            "My roots sense meaning in your words, but my branches can't quite reach the understanding."
        ]

    def get_time_response(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        return random.choice(self.responses["time"]["replies"]).format(time=current_time)

    def respond(self, user_input):
        user_input = user_input.lower().strip()
        
        # Check if we remember the user's name
        if not self.user_name and any(word in user_input for word in ["my name is", "i'm", "i am"]):
            if "my name is" in user_input:
                self.user_name = user_input.split("my name is")[1].strip().title()
            elif "i'm" in user_input:
                self.user_name = user_input.split("i'm")[1].strip().title()
            elif "i am" in user_input:
                self.user_name = user_input.split("i am")[1].strip().title()
            
            if self.user_name:
                return f"My roots will remember you, {self.user_name}. How can I sway with you today?"

        # Check for name recall
        if self.user_name and ("your name" in user_input or "who are you" in user_input):
            return f"I am {self.name}, a gentle presence in your digital forest. And you, dear {self.user_name}, are my companion today."

        # Check all response categories
        for category in self.responses:
            for pattern in self.responses[category]["patterns"]:
                if pattern in user_input:
                    if category == "time":
                        return self.get_time_response()
                    return random.choice(self.responses[category]["replies"])
        
        # If no match found
        return random.choice(self.unknown_responses)

    def typewriter_effect(self, text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
        print()

    def run(self):
        print("\n" + "🌳" * 40)
        self.typewriter_effect(f"Beneath my swaying boughs, I am {self.name}.")
        self.typewriter_effect("Speak, and I'll answer with the wisdom of the ancient grove.")
        self.typewriter_effect("(When your conversation is done, whisper 'bye')")
        print("🌱" * 40 + "\n")

        while True:
            try:
                user_input = input("You: ")
                if not user_input.strip():
                    continue
                
                response = self.respond(user_input)
                
                print(f"\n{self.name}:", end=" ")
                self.typewriter_effect(response)
                
                if any(word in user_input.lower() for word in ["bye", "goodbye", "farewell"]):
                    break
                    
            except KeyboardInterrupt:
                print("\n\nMy leaves tremble at your sudden departure...")
                break

if __name__ == "__main__":
    willow = WhisperingWillow()
    willow.run()
