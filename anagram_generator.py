import random

anagrams = ["car", "tram", "bus", "boats", "cabs", "raft",
"rockets", "trucks", "campers", "glider", "mart", "arc", "frat", "sub",
"boast", "scab", "girdle", "restock", "struck", "scamper"]


def anagram_generator():
    rand_index = random.randint(0, len(anagrams) - 1)
    return anagrams[rand_index]


if __name__ == '__main__':
    print(anagram_generator())
