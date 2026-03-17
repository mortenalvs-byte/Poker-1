print("=== PLO VISION TEST v2 - Fikset pokerkit ===")

from pokerkit import parse_range, calculate_equities, Deck, StandardHighHand

print("\n1. Test pokerkit PLO equity:")

hero_hand = "AhKhQhJh"
board = ["As", "Ks", "Qs", "2d", "3c"]

hero_range = parse_range(hero_hand)
villain_range = parse_range("22+, A2s+, K9s+, QTs+, JTs, ATo+, KJo+")

try:
    equities = calculate_equities(
        (hero_range, villain_range),   # ranges som tuple (viktig!)
        board,
        num_players=2,
        num_hole_dealings=4,
        deck=Deck.STANDARD,
        hand_types=(StandardHighHand,),
        sample_count=8000
    )
    print(f"   Din equity vs range: {equities[0]:.1%}")
    print("✅ pokerkit PLO Monte Carlo fungerer!")
except Exception as e:
    print("❌ pokerkit feilet:", e)

print("\n2. EasyOCR og pytesseract er allerede testet OK fra før.")

print("\nVi er nå klare til å bygge videre med YAML-config, OCR-engine og Rich CLI!")
