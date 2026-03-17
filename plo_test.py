print("=== PLO VISION TEST - Klar for avansert analyse ===")

from pokerkit import parse_range, calculate_equities, Deck, StandardHighHand
import easyocr
import cv2

print("\n1. Test pokerkit (PLO-equity med 4 hullkort):")
hero = "AhKhQhJh"          # eksempel PLO-hånd
board = ["As", "Ks", "Qs", "2d", "3c"]
hero_range = parse_range(hero)
villain_range = parse_range("22+, A2s+, K9s+, QTs+, JTs, ATo+, KJo+")

equities = calculate_equities(
    ranges=(hero_range, villain_range),
    board=board,
    num_players=2,
    num_hole_dealings=4,
    deck=Deck.STANDARD,
    hand_types=(StandardHighHand,),
    sample_count=10000
)
print(f"   Din equity vs range: {equities[0]:.1%}")

print("\n2. Test EasyOCR (klar til å lese kort fra skjerm):")
reader = easyocr.Reader(['en'], gpu=False)
print("   EasyOCR initialisert – klar til live/offline analyse!")

print("\n✅ Alt fungerer! Vi er klare til å bygge full versjon (YAML, batch/live, advice, DB).")
