import json
from controller import PresentationController
from voice_service import speech_to_text
from mic_recorder import record_audio

def main():
    with open("presentation_with_narration.json") as f:
        data = json.load(f)

    slides = data["brand_features"]["slides"]
    products = data["products"]["products"]

    controller = PresentationController(slides, products)

    # Play narration
    controller.play()

    # Record user question
    input("\nPress ENTER to ask a question using your voice...")
    record_audio("question.wav", duration=5)

    # Transcribe
    question_text = speech_to_text("question.wav")
    print(f"\n📝 Transcribed Question: {question_text}")

    # Ask question
    controller.ask_question(question_text)

    # Resume presentation
    controller.end_qa()
    controller.skip()

if __name__ == "__main__":
    main()
