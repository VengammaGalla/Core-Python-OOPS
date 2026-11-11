class Applicant:
    def __init__(self, name, skills):
        self.name = name
        self.__skills = set(skills)

    def __add__(self, skill):
        new_skills = self.__skills.copy()
        new_skills.add(skill)
        return Applicant(self.name, new_skills)

    def __sub__(self, skill):
        new_skills = self.__skills.copy()
        new_skills.discard(skill)
        return Applicant(self.name, new_skills)

    def __eq__(self, other):
        return self.__skills == other.__skills

    def show_skills(self):
        print(sorted(self.__skills))


class ExperiencedApplicant(Applicant):
    def __init__(self, name, skills, experience, company):
        super().__init__(name, skills)
        self.experience = experience
        self.company = company


a1 = Applicant("Ravi", ["Python", "SQL"])
a2 = a1 + "Java"
a2.show_skills()

a3 = a2 - "SQL"
a3.show_skills()

a4 = Applicant("Sita", ["Python", "Java"])
print(a3 == a4)

experienced = ExperiencedApplicant(
    "Rani", ["Python", "SQL"], 3, "ABC Company"
)
print(experienced.experience)