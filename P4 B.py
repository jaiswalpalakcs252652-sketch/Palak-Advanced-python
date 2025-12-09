class CET:
    def __init__(self):
        self.level = "State Level"
    def cet_info(self):
        return "Common Entrance Test"

class JEE:
    def __init__(self):
        self.level = "National Level"
    def jee_info(self):
        return "Engineering Entrance"

class NEET:
    def __init__(self):
        self.level = "National Level"
    def neet_info(self):
        return "Medical Entrance"

class BCA:
    def __init__(self):
        self.level = "University Level"
    def bca_info(self):
        return "Computer Application"

class GovernmentExams(CET, JEE, NEET, BCA):
    def __init__(self, name):
        CET.__init__(self)
        JEE.__init__(self)
        NEET.__init__(self)
        BCA.__init__(self)
        self.name = name
    def info(self):
       return f"""
        {self.name}:
        1. {self.cet_info()} (State Level)
        2. {self.jee_info()} (National Level)
        3. {self.neet_info()} (National Level)
        4. {self.bca_info()} (University Level)
        """  
    
exam1 = GovernmentExams("MAH-CET")
print(exam1.info())
print("From CET:", exam1.cet_info())
print("From JEE:", exam1.jee_info())
print("From NEET:", exam1.neet_info())
print("From BCA:", exam1.bca_info())
print(f"\nself.level value: {exam1.level}")
