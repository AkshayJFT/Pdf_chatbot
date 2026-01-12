import json
from controller import PresentationController
from voice_service import speech_to_text

def main():
    with open("presentation_with_narration.json") as f:
        data = json.load(f)

    slides = data["brand_features"]["slides"]
    products = data["products"]["products"]

    controller = PresentationController(slides, products)

    controller.play()

    input("\n🎤 Press ENTER after asking a question (simulate mic capture)...")

    # Assume mic audio already recorded as question.wav
    question_text = speech_to_text("question.wav")
    controller.ask_question(question_text)

    controller.end_qa()
    controller.skip()

if __name__ == "__main__":
    main()
