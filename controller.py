from voice_service import text_to_speech
from audio_player import play_audio

class PresentationController:
    def __init__(self, slides, products):
        self.slides = slides
        self.products = products
        self.current_index = 0
        self.state = "IDLE"
        self.context_stack = []

    def current_slide(self):
        return self.slides[self.current_index]

    def play(self):
        self.state = "PRESENTING"
        slide = self.current_slide()

        print(f"\n▶️ Playing slide {slide['slide_id']}: {slide['title']}")

        narration_text = slide["narration"]["script"]
        audio_file = text_to_speech(narration_text)

        play_audio(audio_file)


    def pause(self):
        if self.state == "PRESENTING":
            self.state = "PAUSED"
            print("\n⏸️ Presentation paused")

    def resume(self):
        if self.state == "PAUSED":
            self.state = "PRESENTING"
            slide = self.current_slide()
            print(f"\n▶️ Resuming slide {slide['slide_id']}")

    def skip(self):
        if self.current_index < len(self.slides) - 1:
            self.current_index += 1
            print("\n⏭️ Skipping to next slide")
            self.play()
        else:
            print("\n✅ Presentation completed")

    def ask_question(self, question):
        print(f"\n💬 User asked: {question}")
        self.context_stack.append(self.current_index)
        self.state = "QA"
        print("🤖 Answering question (stubbed response)")

    def end_qa(self):
        if self.state == "QA":
            self.current_index = self.context_stack.pop()
            self.state = "PRESENTING"
            print("\n▶️ Resuming presentation after Q&A")
            self.play()
