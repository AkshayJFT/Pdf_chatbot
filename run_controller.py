import json
from controller import PresentationController

def main():
    with open("presentation_with_narration.json") as f:
        data = json.load(f)

    slides = data["brand_features"]["slides"]
    products = data["products"]["products"]

    controller = PresentationController(slides, products)

    controller.play()
    controller.pause()
    controller.resume()
    controller.ask_question("Is this energy efficient?")
    controller.end_qa()
    controller.skip()
    controller.skip()

if __name__ == "__main__":
    main()
