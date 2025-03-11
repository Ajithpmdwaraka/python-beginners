lang = ["python", "swift", "javasript", "typescript"]

lang.append("c")
count = lang.count('python')
index = lang.index('swift')

print(lang)
print(count)
print(index)

framework = ["django", "c++", "angular", "nest"]

# combined_list = lang + framework

lang.extend(framework)

print(lang)


