# This program counts skills

skills = ["Python", "Git", "HTML", "Communication", "Dancing"]

for index, skill in enumerate(skills, start=1):
    print(f"{index}. {skill}")

print(f"Total skills: {len(skills)}")