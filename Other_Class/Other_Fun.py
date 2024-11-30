class Other_fun:
    def __init__(self):
        # Use a raw string for the file path to avoid issues with escape characters
        with open(r"C:\Users\hacia\Desktop\Ri_Project\StopList.txt", "r") as fo:
            self.StopList = [line.strip() for line in fo.readlines() if line.strip() != ""]

    def check_Stop_List(self, stopwords):
        # Check if any word in stopwords exists in self.StopList
        for word in stopwords:
            if word in self.StopList:
                return False
        return True

 

 

