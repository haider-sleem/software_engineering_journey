# Chapter Exercises page 295


# # 1. DMOJ problem crci06p1, Bard
# n = int(input())
# e = int(input())

# songs = [set() for _ in range(n + 1)]
# song_id = 0

# for _ in range(e):
#     people = list(map(int, input().split()))
#     villagers = people[1:]

#     if 1 in villagers:
#         song_id += 1
#         for villager in villagers:
#             songs[villager].add(song_id)
#     else:
#         all_songs = set()
#         for villager in villagers:
#             all_songs.update(songs[villager])

#         for villager in villagers:
#             songs[villager] = all_songs.copy()

# total_songs = song_id

# for villager in range(1, n + 1):
#     if len(songs[villager]) == total_songs:
#         print(villager)


# # 2. DMOJ problem dmopc19c5p1, Conspicuous Cryptic Checklist
# import sys

# n, m = map(int, sys.stdin.readline().split())

# tools = set()
# done = 0

# for i in range(n):
#     tool = sys.stdin.readline().strip()
#     tools.add(tool)

# for j in range(m):
#     tools_nums = int(sys.stdin.readline())
#     tools_needed = set()

#     for k in range(tools_nums):
#         tool_needed = sys.stdin.readline().strip()
#         tools_needed.add(tool_needed)

#     if tools_needed.issubset(tools):
#         done += 1

# print(done)


# # 3. DMOJ problem coci15c2p1, Marko
# import sys
# input = sys.stdin.readline

# mapping = {
#     '2': 'abc', '3': 'def', '4': 'ghi',
#     '5': 'jkl', '6': 'mno', '7': 'pqrs',
#     '8': 'tuv', '9': 'wxyz'
# }

# char_to_key = {}
# for key, letters in mapping.items():
#     for ch in letters:
#         char_to_key[ch] = key

# def word_to_keys(word):
#     return ''.join(char_to_key[ch] for ch in word)

# n = int(input())
# words = [input().strip() for _ in range(n)]
# sequence = input().strip()

# count = 0
# for word in words:
#     if len(word) == len(sequence) and word_to_keys(word) == sequence:
#         count += 1

# print(count)


""" "
بدون قاموس # كلاود
import sys
input = sys.stdin.readline

KEYS = "22233344455566677778889999"

def word_to_keys(word):
    return ''.join(KEYS[ord(ch) - ord('a')] for ch in word)

n = int(input())
words = [input().strip() for _ in range(n)]
sequence = input().strip()

count = sum(1 for w in words if len(w) == len(sequence) and word_to_keys(w) == sequence)
print(count)
"""

# # 4. DMOJ problem ccc06s2, Attack of the CipherTexts
# decoded_message = input()
# secret_message = input()
# secret_message2 = input()

# symbol = {}

# used_plain = set()
# used_cipher = set()

# for plain_char, cipher_char in zip(decoded_message, secret_message):
#     symbol[cipher_char] = plain_char
#     used_plain.add(plain_char)
#     used_cipher.add(cipher_char)

# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

# remaining_plain = [ch for ch in alphabet if ch not in used_plain]
# remaining_cipher = [ch for ch in alphabet if ch not in used_cipher]

# if len(remaining_plain) == 1 and len(remaining_cipher) == 1:
#     symbol[remaining_cipher[0]] = remaining_plain[0]

# decoded = [symbol.get(char, ".") for char in secret_message2]

# print("".join(decoded))

# # 5. DMOJ problem dmopc19c3p1, Mode Finding
# n = int(input())
# numbers = list(map(int, input().split()))

# freq = {}

# for num in numbers:
#     if num not in freq:
#         freq[num] = 1
#     else:
#         freq[num] += 1

# max_frequency = max(freq.values())

# modes = []

# for num in freq:
#     if freq[num] == max_frequency:
#         modes.append(num)

# modes.sort()

# print(*modes)


# # 6. DMOJ problem coci14c2p2, Utrka (Try solving this one in three different ways: using a dictionary, using a set, and using lists!)
# n = int(input())

# players = {}
# for _ in range(n):
#     player_name = input()
#     if player_name not in players:
#         players[player_name] = 1
#     else:
#         players[player_name] += 1

# winners = {}
# for _ in range(n - 1):
#     winner_name = input()
#     if winner_name not in winners:
#         winners[winner_name] = 1
#     else:
#         winners[winner_name] += 1

# loser = ""

# for player in players:
#     if player not in winners:
#         loser = player
#         break
#     elif players[player] > winners[player]:
#         loser = player
#         break

# print(loser)

"""
# ChatGpt
n = int(input())

players = {}

# تسجيل جميع المتسابقين
for _ in range(n):
    name = input()
    players[name] = players.get(name, 0) + 1

# طرح كل من أنهى السباق
for _ in range(n - 1):
    name = input()
    players[name] -= 1

# البحث عن المتسابق الذي لم ينهِ السباق
for name, count in players.items():
    if count > 0:
        print(name)
        break
"""

"""
# claude
from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
registered = [input().strip() for _ in range(n)]
finished   = [input().strip() for _ in range(n - 1)]

reg = Counter(registered)
for name in finished:
    reg[name] -= 1

for name, count in reg.items():
    if count > 0:
        print(name)
        break
"""

# 7. DMOJ problem coci17c2p2, ZigZag (Hint: maintain two dictionaries. The first maps each starting letter to its list of words; the second maps each starting letter to the index of its next word that will be output. That way, we can cycle through the words for each letter without having to explicitly update numbers of occurrences or modify lists.)
# n, m = map(int, input().split())

# words = {}
# used = {}

# for _ in range(n):
#     word = input().strip()
#     first = word[0]

#     if first not in words:
#         words[first] = []

#     words[first].append(word)
#     used[word] = 0

# for letter in words:
#     words[letter].sort()

# for _ in range(m):
#     letter = input().strip()

#     best = words[letter][0]

#     for word in words[letter]:
#         if used[word] < used[best]:
#             best = word
#         elif used[word] == used[best] and word < best:
#             best = word

#     print(best)
#     used[best] += 1

"""
# ChatGpt
import heapq

n, m = map(int, input().split())

words = {}

for _ in range(n):
    word = input().strip()
    letter = word[0]

    if letter not in words:
        words[letter] = []

    heapq.heappush(words[letter], (0, word))

for _ in range(m):
    letter = input().strip()

    used, word = heapq.heappop(words[letter])

    print(word)

    heapq.heappush(words[letter], (used + 1, word))
"""

"""
# claude
import sys
from collections import defaultdict
input = sys.stdin.readline

n, q = map(int, input().split())
words = [input().strip() for _ in range(n)]
letters = [input().strip() for _ in range(q)]

# نجمع الكلمات حسب أول حرف، مرتبة أبجدياً مسبقاً
by_letter = defaultdict(list)
for w in sorted(words):
    by_letter[w[0]].append(w)

count = defaultdict(int)

for letter in letters:
    candidates = by_letter[letter]
    min_count = min(count[w] for w in candidates)
    chosen = next(w for w in candidates if count[w] == min_count)
    count[chosen] += 1
    print(chosen)


"""


# CCO '99 P2 - Common Words
def invert_dictionary(d):
    """
    d is a dictionary mapping strings to numbers.
    Return the inverted dictionary of d.
    """
    inverted = {}

    for key in d:
        num = d[key]

        if num not in inverted:
            inverted[num] = [key]
        else:
            inverted[num].append(key)

    return inverted


def with_suffix(num):
    """
    num is an integer >= 1.
    Return a string of num with its suffix added; e.g. '5th'.
    """
    s = str(num)

    if s[-1] == "1" and s[-2:] != "11":
        return s + "st"
    elif s[-1] == "2" and s[-2:] != "12":
        return s + "nd"
    elif s[-1] == "3" and s[-2:] != "13":
        return s + "rd"
    else:
        return s + "th"


def most_common_words(num_to_words, k):
    """
    num_to_words is a dictionary mapping number of occurrences
    to lists of words.

    k is an integer >= 1.

    Return a list of the kth most common words.
    """
    nums = list(num_to_words.keys())
    nums.sort(reverse=True)

    total = 0
    i = 0
    done = False

    while i < len(nums) and not done:
        num = nums[i]

        if total + len(num_to_words[num]) >= k:
            done = True
        else:
            total = total + len(num_to_words[num])
            i = i + 1

    if total == k - 1 and i < len(nums):
        return num_to_words[nums[i]]
    else:
        return []


n = int(input())

for dataset in range(n):
    lst = input().split()
    m = int(lst[0])
    k = int(lst[1])

    word_to_num = {}

    for i in range(m):
        word = input()

        if word not in word_to_num:
            word_to_num[word] = 1
        else:
            word_to_num[word] = word_to_num[word] + 1

    num_to_words = invert_dictionary(word_to_num)

    ordinal = with_suffix(k)
    words = most_common_words(num_to_words, k)

    print(f"{ordinal} most common word(s):")

    for word in words:
        print(word)

    print()
