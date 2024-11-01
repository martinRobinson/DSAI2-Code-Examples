# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unverified_users = ['alice', 'brian', 'candace']
verified_users = []

# Display all verified users.
print("The following users need to be verified:")
for unverified_user in unverified_users:
    print(unverified_user.title())

print()
# Verify each user until there are no more unverified users.
# Move each verified user into the list of verified users.
while unverified_users:
    current_user = unverified_users.pop()
    print(f"Verifying user: {current_user.title()}")
    verified_users.append(current_user)
    
# Display all verified users.
print("\nThe following users have been verified:")
for verified_user in verified_users:
    print(verified_user.title())
