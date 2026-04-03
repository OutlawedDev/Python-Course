import requests
from config import HF_API_KEY

MODEL_ID = "sentence-transformers/all-MiniLM-L6-v2"
API_URL = f"https://router.huggingface.co/hf-inference/models/{MODEL_ID}"
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}

PAIRS = [
    ("The sun is a star located at the center of our solar system.",
     "Our solar system's middle point is a star we call the sun."),
    ("Heavy rain caused the football match to be cancelled.",
     "The game was called off because it was pouring outside."),
    ("To make a great pizza, you need fresh dough and good cheese.",
     "Quality cheese and fresh crust are secrets to a tasty pizza."),
    ("Computers use binary code, which is just ones and zeros.",
     "Digital machines run on binary, consisting of 0s and 1s."),
    ("Mount Everest is the tallest mountain above sea level.",
     "No mountain on Earth is higher than Everest."),
    ("Learning to drive takes a lot of practice and patience.",
     "You need to be patient and practice a ton to get your drivers license.")
]

def similarity(a: str, b: str) -> float:
    payload = {"inputs": {"source_sentence": a, "sentences": [b]}}
    r = requests.post(API_URL, headers=HEADERS, json=payload, timeout=30)
    if not r.ok: raise RuntimeError(f"HF error {r.status_code}: {r.text}")
    data = r.json()
    if isinstance(data, dict): raise RuntimeError(data.get("error", str(data)))
    return float(data[0]) 

def bar(score01: float) -> str:
    blocks = int((score01 * 100) // 10)
    return "█" * blocks + "░" * (10 - blocks)

def verdict(score01: float, threshold: float) -> str:
    if score01 >= threshold:
        return "TOO SIMILAR (PROBABLY IS COPY)"
    if score01 >= threshold - 0.15:
        return "KIND OF SIMILAR (MAYBE COPY BUT YOU CHANGED THE WORDING TOO MUCH)"
    return "DIFFERENT ENOUGH (COMPLETELY DIFFERENT)"

def main():
    print("Copy checker")
    print("This checks if two answers are similar in meaning.\n")
    threshold = 0.80
    print(f"Rule: If similarity ≥ {threshold}, we say 'Too Similar'.\n")

    while True:
        print("type 'demo' to test examples, or 'custom' to type your own, or 'exit'.")
        mode = input("Mode: ").strip().lower()
        if mode == "exit":
            print("Bye")
            break

        if mode == "demo":
            for i, (a1, a2) in enumerate(PAIRS[:5], 1):
                s = similarity(a1, a2)
                pct = round(s * 100, 1)
                print(f"\n{i}) Answer 1: {a1}\n   Answer 2: {a2}")
                print(f"   Similarity: {pct}% [{bar(s)}]  {verdict(s, threshold)}")

        elif mode == "custom":
            a1 = input("\nPerson Answer 1: ").strip()
            a2 = input("Person Answer 2: ").strip()
            if not a1 or not a2:
                print("Please type both answers.\n")
                continue
            s = similarity(a1, a2)
            pct = round(s * 100, 1)
            print(f"\nSimilarity: {pct}% [{bar(s)}]  {verdict(s, threshold)}\n")

        else:
            print("Please type: demo, custom, exit\n")

if __name__ == "__main__":
    main()
