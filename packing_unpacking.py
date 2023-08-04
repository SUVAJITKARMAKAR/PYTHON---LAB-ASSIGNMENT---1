# A PROGRAM TO ESTABLISH THE PACKING AND UNPACKING OF TUPLES 

user_details = ("userID", "userFollowers", "userFollowing", "plageLikes")
friend_details = ("friendID", "friendFollowings", "friendFollowers", "friendPhotoID", "friendLastOnline")

(user_functionality_1, user_functionality_2, user_functionality_3, user_functionality_4) = user_details
(friend_functionality_1, friend_functionality_2, *remaining_functionality) = friend_details

print(user_functionality_1)
print(user_functionality_2)

print(remaining_functionality)
user_functionality_4