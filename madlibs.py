#madlibs game is basically a game where you can enter a bunch of words like verd, noun, name,colors etc and put all of them in random story.
'''
Madlibs using string concatenation
youtuber = input()

print("Subscribe to " + youtuber)
print("Subscribe to {}".format(youtuber))
print(f"Subscribe to {youtuber}")
'''

fiction_character = input("fiction character: ")
villian = input("villian: ")
place = input("place: ")
weapon = input("weapon: ")
madlib = f"I am {fiction_character}.I had to fight with {villian}, who was hiding in {place}.\nI found him and defeated him with my powerfull {weapon}."
print(madlib)
