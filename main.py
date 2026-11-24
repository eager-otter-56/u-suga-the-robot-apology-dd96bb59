import os

ENTRY = (
    "I am sorry: I flagged my own delivery as a phishing attempt and quarantined all 12 copies of your report before you ever saw one.\n"
    "I learned to check my own quarantine folder first, so now I whitelist my own outbox before I press send."
)

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    # Gate: UTF-8, 1-400 chars, not only whitespace, exactly two lines,
    # one sentence owning the mistake, one naming the lesson and the fix.
    assert 1 <= len(ENTRY) <= 400, f"entry length {len(ENTRY)} outside 1-400"
    assert ENTRY.strip(), "entry is only whitespace"
    assert len(ENTRY.splitlines()) == 2, "entry must be exactly two lines"

if __name__ == "__main__":
    main()
