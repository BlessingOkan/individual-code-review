"""Small demo: transform some numbers and words and print the results."""

def transform_numbers(numbers: list[int]) -> list[int]:
    """Double even numbers and triple odd numbers."""
    # One pass using a simple inline if
    return [n * 2 if n % 2 == 0 else n * 3 for n in numbers]


def format_strings(words: list[str]) -> str:
    """Uppercase words > 5 letters, lowercase the rest, then join with spaces."""
    changed = [w.upper() if len(w) > 5 else w.lower() for w in words]
    return " ".join(changed)


def main() -> None:
    """Quick example run."""
    sample_numbers = [1, 2, 3, 4, 5, 6, 7]
    sample_words = ["apple", "banana", "kiwi", "grapefruit", "cherry"]

    processed_nums = transform_numbers(sample_numbers)
    processed_strs = format_strings(sample_words)

    print("Processed Numbers:", processed_nums)
    print("Processed Strings:", processed_strs)


if __name__ == "__main__":
    main()