from collections import defaultdict
from romeo_and_juliet_data import lines as rj


def word_length_histogram(text_list):
    """Takes the a list of multiword lines and returns
    a dictionary where the keys are word lengths and the
    values are how many words there are of that length.
    Assume there is no punctuation to worry about.
    For example, the input:
        [ "Summer school", "is nearly over"]
    should return the dictionary
        { 6 : 3, 2 : 1, 4 : 1 }
    """
    out = defaultdict(int)
    for word in [word.replace("'", "") for line in text_list for word in line.split()]:
        out[len(word)] += 1
    return dict(out)


def main():
    data = word_length_histogram(rj)
    total = sum(data.values())
    for key in sorted(data.keys()):
        print(
            f"Proportion of {key}-letter words: {data[key] / total * 100:.2f}% ({data[key]} words)"
        )


if __name__ == "__main__":
    main()
