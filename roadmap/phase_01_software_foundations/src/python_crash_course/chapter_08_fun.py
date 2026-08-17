# TRY IT YOURSELF  page 169

# # 8-1. Message:
# def display_message():
#     '''  telling everyone what I'm learning about in this chapter.'''
#     print("I'm  learning function in this chapter.")

# display_message()


# # 8-2. Favorite Book:
# def favorite_book(title):
#     ''' Display my favorite books '''
#     print(f"One of my favorite books is {title.title()}.")

# favorite_book("alice in wonderland")
# help(favorite_book)


# -----------------------------------------------------------

# TRY IT YOURSELF  page 174


# # 8-3. T-Shirt:
# def  make_shirt(size, text="Hello world"):
#     ''' Display  a size and the text of a message that should be printed on the shirt '''
#     print(f"The size of the shirt is {size} and the message printed on it is '{text.title()}'.")
# make_shirt("XL")
# make_shirt(size="L", text="Python is Great")


# # 8-4. Large Shirts:
# def make_shirt(size, message="I love Python"):
#     ''' Display  a size and the text of a message that should be printed on the shirt '''
#     print(f"The size of the shirt is {size} and the message printed on it is '{message.title()}'.")

# make_shirt(size="L")
# make_shirt(size="M")
# make_shirt(size="XL", message="Python is Great")


# # 8-5. Cities:
# def describe_city(city, country="egypt"):
#     ''' Displat the name & the country of thr city'''
#     print(f"{city.title()} is in {country.title()}.")

# describe_city("cairo")
# describe_city("alex")
# describe_city("makka", "KSA")

# --------------------------------------------------------------------

# TRY IT YOURSELF  page 179

# # 8-6. City Names:
# def city_country(city, country):
#     # ''' Displat the name of the city and the country '''
#     return f"{city.title()}, {country.title()}"

# city1 = city_country("santiago", "chile")
# print(city1)

# city2 = city_country("tokyo", "japan")
# print(city2)

# city3 = city_country("paris", "france")
# print(city3)


# # 8-7. Album:
# def make_album(artist_name, album_title, number_of_songs=None ):
#     '''  builds a dictionary describing a music album.'''
#     album_dict = {
#         "artist": artist_name.title(),
#         "title": album_title.title(),
#     }
#     if number_of_songs:
#         album_dict["number of songs"] = number_of_songs
#     return album_dict
# album1 = make_album("amr diab", "nour el ein")
# album2 = make_album("adele", "21")
# album3 = make_album("pink floyd", "the dark side of the moon")
# album4 = make_album("amr diab", "nour el ein", 14)


# print(album1)
# print(album2)
# print(album3)
# print(album4)


# # 8-8. User Albums:
# def make_album(artist_name, album_title, number_of_songs=None ):
#     '''  builds a dictionary describing a music album.'''
#     album_dict = {
#         "artist": artist_name.title(),
#         "title": album_title.title(),
#     }
#     if number_of_songs:
#         album_dict["number of songs"] = number_of_songs
#     return album_dict

# print("(enter 'q' at any time to quit)")
# # Create an empty list to store multiple album dictionaries
# albums_list = []
# while True:
#     artist_name = input("Enter artist name : ")
#     if artist_name == "q":
#         break
#     album_title = input("Enter the Album title : ")
#     if album_title == "q":
#         break
#     album = make_album(artist_name, album_title)
#     print(album)
#     albums_list.append(album)
# print(albums_list)


# -------------------------------------------------------------

# TRY IT YOURSELF  page 184

# # 8-9. Messages:
# def show_messages(messages):
#     """Print each text message in the list."""
#     for message in messages:
#         print(message)

# # Define a list of short text messages
# text_messages = [
#     "Hello, how are you?",
#     "Don't forget the meeting at 5 PM.",
#     "Python is fun to learn!",
#     "Are we still going to the gym?"
# ]

# # Pass the list to the function
# show_messages(text_messages)


# # 8-10. Sending Messages:
# def send_messages(messages_to_send, sent_messages):
#     """
#     Print each message and move it from the first list
#     to the sent_messages list.
#     """
#     while messages_to_send:
#         current_message = messages_to_send.pop()
#         print(f"Sending message: {current_message}")
#         sent_messages.append(current_message)

# messages = ["Hello world", "Python is great", "Hi"]
# sent_messages_list = []

# send_messages(messages, sent_messages_list)

# print(f"Original list: {messages}")
# print(f"Sent messages list: {sent_messages_list}")


# # 8-11. Archived Messages:
# def send_messages(messages_to_send, sent_messages):
#     """Print each message and send a copy it to sent_messages."""
#     while messages_to_send:
#         current_message = messages_to_send.pop(0) # pop(0) علشان نحافظ على نفس الترتيب بعد النقل
#         print(f"Sending message: {current_message}")
#         sent_messages.append(current_message)

# messages_queue = ["Hello world", "Python is great", "Hi"]
# sent_messages_list = []

# # تمرير نسخة من القائمة وليس القائمة
# send_messages(messages_queue[:], sent_messages_list)

# # القائمة الأصلية ستبقى كما هي لأننا مررنا نسخة منها فقط
# print(f"Original list (retained): {messages_queue}")
# print(f"Sent messages list: {sent_messages_list}")


# -------------------------------------------------------------------------

# TRY IT YOURSELF  page 187

# # 8-12. Sandwiches:
# def make_sandwich(*items):
#     ''' Sandwich items displayed '''
#     print("\nSandwich items :")
#     for item in items:
#         print(f"- {item.title()}")

# make_sandwich("cheese")
# make_sandwich("turkey", "lettuce", "tomato")
# make_sandwich("roast beef", "mustard", "onions", "pickles")


# # 8-13. User Profile:
# def user_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user."""
#     user_info["First_name"] = first.title()
#     user_info["Last_name"] = last.title()
#     return user_info

# haider_profile = user_profile("haider", "sleem", Age=41, Location="egypt", Job="programmer")
# print(haider_profile)


# # 8-14. Cars:
# def make_car(manufacturer, model, **car_info):
#     """Store information about a car in a dictionary."""
#     car_info['manufacturer'] = manufacturer.title()
#     car_info['model'] = model.title()
#     return car_info

# car = make_car('subaru', 'outback', color='blue', tow_package=True)

# print(car)

# -------------------------------------------------------------------------

# TRY IT YOURSELF  page 192  I will apply in my project.



