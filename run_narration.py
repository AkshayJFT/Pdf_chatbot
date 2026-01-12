import json
from narration_generator import (
    generate_slide_narration,
    generate_product_narration
)

INPUT_FILE = "presentation_output.json"
OUTPUT_FILE = "presentation_with_narration.json"


def main():
    with open(INPUT_FILE) as f:
        data = json.load(f)

    # Brand slides narration
    for slide in data["brand_features"]["slides"]:
        slide["narration"] = {
            "duration_sec": 45,
            "script": generate_slide_narration(slide, 45)
        }

    # Product narration
    for product in data["products"]["products"]:
        product["narration"] = {
            "duration_sec": 45,
            "script": generate_product_narration(product, 45)
        }

    with open(OUTPUT_FILE, "w") as f:
        json.dump(data, f, indent=2)

    print("Narration generation completed.")


if __name__ == "__main__":
    main()
