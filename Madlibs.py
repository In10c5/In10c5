# # string concatenation (aka how to put strings together)
# # suppose we want to create a string that says "subscribe to _______ "
# youtuber = "Ved Bhattathiripad" # some string variable 

# # a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}") # best way

adj = input("Adjecive: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person: ")

madlib = f"Computer Programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)