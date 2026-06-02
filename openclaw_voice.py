#!/usr/bin/env python3


import time
import subprocess
from pathlib import Path
from sunfounder_voice_assistant.stt import STT
from sunfounder_voice_assistant.tts import Piper
import random
import json

# Configuration
WAKE_WORDS = ["amy", "hello amy", "hi amy", "hey amy"]
LANGUAGE = 'en-us'
WORKSPACE = Path.home() / '.openclaw' / 'workspace'
MEMORY_FILE = WORKSPACE / 'memory' / 'voice_chat.md'
REPLAY_WAKES = ["I'm here", "Yes", "What can I do for you", "Please go ahead", "Hello", "How can I help"]

class VoiceChat:
    def __init__(self):
        print("🎙️  Initializing Voice Chat...")
        self.stt = STT(language=LANGUAGE)
        self.stt.set_wake_words(WAKE_WORDS)
        print(f"📢 Wake words: {WAKE_WORDS}")
        print(f"✅ STT Ready - Model: {self.stt.get_model_name(LANGUAGE)}")
        self.tts = Piper()
        self.tts.set_model('en_US-amy-medium')
        print(f"✅ TTS Ready - Using Piper, model: en_US-amy-medium")

    def get_llm_response(self, text):
        """Send text to OpenClaw and get LLM response"""
        try:
            cmd = [
                'openclaw',
                'agent',
                '--agent', 'main',
                '--channel', 'last',
                '--message', text,
                '--json',
                '--log-level', 'silent',
                '--timeout', '30'
            ]

            print(f"Running command: {' '.join(cmd)}")
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=35)
            if result.returncode == 0:
                # Filter out warning lines
                lines = result.stdout.splitlines()
                filtered_lines = [line for line in lines if "Config warnings" not in line]
                result.stdout = "\n".join(filtered_lines)
                # Parse JSON response
                response = json.loads(result.stdout)
                # Extract actual message content
                if isinstance(response, dict):
                    return response["result"]["payloads"][0]["text"]
                return str(response)
            else:
                print(f" ❌ Agent error: {result.stderr.strip()}")
                return f"Sorry, an error occurred: {result.stderr.strip()[:100]}"

        except Exception as e:
            return f"Sorry, connection failed: {e}"

    def log_interaction(self, user_text, bot_response):
        """Log voice interactions to memory file"""
        try:
            MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
            with open(MEMORY_FILE, 'a', encoding='utf-8') as f:
                f.write(f"\n## {timestamp}\n")
                f.write(f"**You said**: {user_text}\n")
                f.write(f"**I said**: {bot_response}\n")
        except Exception as e:
            print(f"⚠️  Could not log: {e}")

    def run(self):
        """Main voice chat loop"""
        print("=" * 50)
        print("🎙️  Voice Chat Started!")
        print("   Say a wake word to begin...")
        print("   Press Ctrl+C to stop")
        print("=" * 50)
        print()

        while True:
            # Start listening for wake words
            self.stt.start_listening_wake_words()

            # Wait for wake word
            print("⏳ Waiting for wake word...", end=' ', flush=True)
            while not self.stt.is_waked():
                time.sleep(0.5)

            if self.stt.is_waked():
                print("✅ Waked!")
                self.tts.say(random.choice(REPLAY_WAKES))

                # Listen for user's speech
                print("👂 Listening...", end=' ', flush=True)
                result = self.stt.listen(stream=False)

                if result:
                    user_text = result.strip()
                    print(f"\n🗣️  You said: {user_text}")

                    # Check for exit command
                    # if user_text.lower() in ['stop', 'exit', 'quit', 'goodbye', 'bye']:
                    #     print("👋 Goodbye!")
                    #     self.tts.say("Goodbye! Call me if you need me again")
                    #     break

                    # Get LLM response
                    print("🤔 Thinking...", end=' ', flush=True)
                    bot_response = self.get_llm_response(user_text)
                    print(f"\n💬 Response: {bot_response}")

                    # Speak the response
                    self.tts.say(bot_response)

                    # Log the interaction
                    self.log_interaction(user_text, bot_response)
                else:
                    print("❌ No speech detected")

                # Reset wake state
                time.sleep(0.5)


if __name__ == '__main__':
    chat = VoiceChat()
    chat.run()
