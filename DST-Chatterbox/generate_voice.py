"""
Chatterbox TTS - Teemo Voice Generator (Advanced)
Each line uses a matched reference WAV with tuned parameters.
"""

import torchaudio as ta
from chatterbox.tts import ChatterboxTTS
import os
import sys
import time

# ============================================
# REFERENCE WAV FILES (put these in the "wav" folder)
# ============================================

REF_XXX     = os.path.join("wav", "XXX.wav")
# --- サンプル（コメントを外して編集してください。修正箇所はREFとLINESの2か所です） ---
# REF_HA_HA     = os.path.join("wav", "Ha_ha_ha!.wav")
# REF_YESSIR    = os.path.join("wav", "Yes_sir!.wav")

# ============================================
# LINES TO GENERATE
# ============================================

LINES = {
    "xxx": {
        "text": "Put your text here",
        "ref": REF_XXX,
        "exaggeration": 0.5,
        "cfg": 0.5,
    },
}
# --- サンプル（コメントを外して編集してください。修正箇所はREFとLINESの2か所です） ---
# LINES = {
#     "ha_ha_ha": {
#         "text": "Ha ha ha!",
#         "ref": REF_HA_HA,
#         "exaggeration": 0.6,
#         "cfg": 0.5,
#     },
#     "yes_sir": {
#         "text": "Yes sir!",
#         "ref": REF_YESSIR,
#         "exaggeration": 0.5,
#         "cfg": 0.5,
#     },
# }


OUTPUT_DIR = "output"

# ============================================
# MAIN
# ============================================

def main():
    print("=" * 50)
    print("  Chatterbox TTS - Teemo Voice Generator")
    print("=" * 50)
    print()

    all_refs = set(line["ref"] for line in LINES.values())
    for ref in all_refs:
        if not os.path.exists(ref):
            print(f"[ERROR] Reference audio not found: {ref}")
            print(f"Put it in the 'wav' folder.")
            sys.exit(1)

    print(f"Lines to generate: {len(LINES)}")
    for name, cfg in LINES.items():
        print(f"  {name}: \"{cfg['text']}\"")
        print(f"    ref={cfg['ref']}, exag={cfg['exaggeration']}, cfg={cfg['cfg']}")
    print()

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("[1] Loading model... (first run downloads several GB)")
    start = time.time()
    model = ChatterboxTTS.from_pretrained(device="cpu")
    print(f"    Done ({time.time() - start:.1f}s)")
    print()

    for i, (name, cfg) in enumerate(LINES.items(), 1):
        text = cfg["text"]
        ref = cfg["ref"]
        exag = cfg["exaggeration"]
        cfg_w = cfg["cfg"]

        print(f"[{i+1}] Generating: \"{text}\"")
        print(f"     ref={ref}, exag={exag}, cfg={cfg_w}")
        start = time.time()

        wav = model.generate(
            text,
            audio_prompt_path=ref,
            exaggeration=exag,
            cfg_weight=cfg_w,
        )

        output_path = os.path.join(OUTPUT_DIR, f"{name}.wav")
        ta.save(output_path, wav, model.sr)

        elapsed = time.time() - start
        print(f"     -> {output_path} ({elapsed:.1f}s)")
        print()

    print("=" * 50)
    print(f"  Done! Check the '{OUTPUT_DIR}' folder.")
    print("=" * 50)
    print()

if __name__ == "__main__":
    main()
