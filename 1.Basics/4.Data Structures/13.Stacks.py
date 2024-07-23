browsing_sessions = []
browsing_sessions.append(1)
browsing_sessions.append(2)
browsing_sessions.append(3)

print(browsing_sessions) # [1, 2, 3]

last = browsing_sessions.pop()
print(last) # 3
print(browsing_sessions) # [1, 2]

print(f"redirect to: {browsing_sessions[-1]}") # redirect to: 2

browsing_sessions.clear()

if not browsing_sessions:
    print("disabled")
else:
    print(browsing_sessions[-1])
    
# disabled
