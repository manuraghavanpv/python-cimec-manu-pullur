# -*- coding: utf-8 -*-
"""Module-0 Homeworks.ipynb

#**MODULE-0**

##Lecture 0.0
"""

# 0.0.0
print("\n0.0.0 - Leap Year Checker")
year_0 = 1900
year_1 = 2000
year_2 = 2024
year_3 = 2025

for year in [year_0, year_1, year_2, year_3]:
    is_leap_year = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
    print(f"{year} is a leap year: {is_leap_year}")

# 0.0.1
print("\n0.0.1 - Temperature Converter")
temp_0 = 32.0
temp_1 = 212.0
temp_2 = 98.6
temp_3 = -40.0

for temp in [temp_0, temp_1, temp_2, temp_3]:
    temp_in_celsius = int((temp - 32) * 5/9)
    is_frozen = temp_in_celsius < 0
    is_boiling = temp_in_celsius >= 100
    is_liquid = 0 <= temp_in_celsius < 100
    print(f"\n{temp}°F = {temp_in_celsius}°C")
    print(f"Frozen: {is_frozen}")
    print(f"Boiling: {is_boiling}")
    print(f"Liquid: {is_liquid}")

"""##Lecture 0.1

"""

# 0.1.0
stupid_text = "Hello, world!"

uppercase_string = stupid_text.upper()
even_characters = stupid_text[::2]
odd_characters = stupid_text[1::2]
concatenated_string = even_characters + " " + odd_characters

print(f"Original: {stupid_text}")
print(f"Uppercase: {uppercase_string}")
print(f"Even chars: {even_characters}")
print(f"Odd chars: {odd_characters}")
print(f"Combined: {concatenated_string}")

# 0.1.1
# 1. List - good for ordered collection that needs modification
# 2. Dictionary - map student names to addresses
# 3. Tuple - immutable pair for coordinates
# 4. Set - ensures uniqueness of IPs

# 0.1.2
list_of_elements = [1, 2, 3, 4, 5]
dictionary_of_elements = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

last_element = list_of_elements.pop()
dictionary_of_elements["new_element"] = last_element
dictionary_of_elements["rest_of_the_list"] = list_of_elements
first_of_rest = dictionary_of_elements["rest_of_the_list"][0]

print(f"Modified dictionary: {dictionary_of_elements}")
print(f"First of rest: {first_of_rest}")

"""##Lecture 0.2"""

# 0.2.0
print("\n0.2.0 - Text Analysis")
text_sample1 = """
Python is a high-level, general-purpose programming language. Its design philosophy
emphasizes code readability with the use of significant indentation. Python is dynamically
typed and garbage-collected. It supports multiple programming paradigms, including structured,
object-oriented, and functional programming.
"""

text_sample2 = """
Python is widely used in artificial intelligence, data analysis, scientific computing,
and web development. Its syntax allows programmers to express concepts in fewer lines
of code than would be possible in languages such as C++ or Java. The language provides
constructs intended to enable clear programs on both small and large scales.
"""

# 1. Clean the texts
cleaned_text1 = text_sample1.lower().replace('.', '').replace(',', '')
cleaned_text2 = text_sample2.lower().replace('.', '').replace(',', '')

# 2. Create sets of unique words
unique_words1 = set(cleaned_text1.split())
unique_words2 = set(cleaned_text2.split())

# 3. Find common words
common_words = unique_words1 & unique_words2

# 4. Find unique words
only_in_text1 = unique_words1 - unique_words2
only_in_text2 = unique_words2 - unique_words1

# 5. Word frequency dictionary
all_words = cleaned_text1.split() + cleaned_text2.split()
word_frequency = {}
for word in all_words:
    word_frequency[word] = word_frequency.get(word, 0) + 1

# 6. Top five words
top_five_words = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)[:5]

print("\nCommon words:")
print(common_words)
print("\nUnique to text1:")
print(only_in_text1)
print("\nUnique to text2:")
print(only_in_text2)
print("\nTop 5 frequent words:")
print(top_five_words)

"""##Lecture 0.3"""

# 0.3.0
print("\n0.3.0 - Square List Function")
def square_list(numbers):
    return [x**2 for x in numbers]

print("Checking sums divisible by 3 (will print 'bingo' if found):")
for i in range(0, 100, 10):
    nums = list(range(i+1, i+11))
    squared = square_list(nums)
    if sum(squared) % 3 == 0:
        print(f"bingo for range {nums}")

# 0.3.1
print("\n0.3.1 - Netflix Session Generator")
import random

def simulate_session(prob_continue=0.9, prob_cliffhanger=0.3, max_episodes=10, cliffhanger_prob=None):
    episodes = 1
    while episodes < max_episodes:
        if random.random() > prob_continue:
            break
        if cliffhanger_prob is not None and random.random() < cliffhanger_prob:
            continue
        episodes += 1
    return episodes

print("Simulating 5 viewing sessions:")
for _ in range(5):
    print(f"Watched {simulate_session()} episodes")

"""##Lecture 0.4"""

# 0.4.0
print("\n0.4.0 - Counter Class Exercises")
class Counter:
    """A simple counter class that can increment and reset."""
    def __init__(self, start=0, max_value=None):
        self._value = start
        self._increment_count = 0
        self._max_value = max_value

    def increment(self, step=1):
        """Increases counter by step (default 1) and returns new value"""
        self._value += step
        self._increment_count += 1
        if self._max_value is not None and self._value > self._max_value:
            raise ValueError("Counter value exceeds maximum value")
        return self._value

    def reset(self):
        """Resets counter to 0 and returns new value"""
        self._value = 0
        return self._value

    def __str__(self):
        return f"Counter(value={self._value})"

# 1. Create instance and test
print("\nBasic counter:")
counter = Counter()
print(f"Initial: {counter}")
for _ in range(3):
    counter.increment()
    print(f"After increment: {counter}")

# 2. Increment by 2 until >20
print("\nCounting by 2s up to 20:")
counter = Counter()
while counter._value <= 20:
    counter.increment(2)
    print(counter)

# 3-5. Limited counter with resets
print("\nLimited counter with resets:")
limited_counter = Counter(start=5, max_value=10)
for i in range(20):
    try:
        limited_counter.increment()
    except ValueError:
        limited_counter.reset()
    if limited_counter._increment_count % 5 == 0:
        limited_counter.reset()
    print(f"Step {i+1}: {limited_counter}")

"""##Lecture-0.5"""

# 0.5.0
print("\n0.5.0 - RGBColor Class")
class RGBColor:
    def __init__(self, r, g, b):
        if not all(0 <= x <= 255 for x in (r, g, b)):
            raise ValueError("Values must be 0-255")
        self._r = r
        self._g = g
        self._b = b

    @property
    def r(self):
        return self._r

    @property
    def g(self):
        return self._g

    @property
    def b(self):
        return self._b

    @property
    def rgb_tuple(self):
        return (self._r, self._g, self._b)

    def mix_with(self, other_color):
        new_r = int((self._r + other_color.r) / 2)
        new_g = int((self._g + other_color.g) / 2)
        new_b = int((self._b + other_color.b) / 2)
        return RGBColor(new_r, new_g, new_b)

# Testing
print("Testing RGBColor class:")
color1 = RGBColor(100, 150, 200)
color2 = RGBColor(50, 100, 150)
print(f"Color 1: {color1.rgb_tuple}")
print(f"Color 2: {color2.rgb_tuple}")

mixed = color1.mix_with(color2)
print(f"Mixed color: {mixed.rgb_tuple}")
