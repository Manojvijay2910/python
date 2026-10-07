from abc import ABC, abstractmethod

# Abstract Class
class TouchScreenLaptop(ABC):

    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass

#HP
class HP(TouchScreenLaptop):

    def scroll(self):
        print("Scrolling on HP laptop")

#DELL
class DELL(TouchScreenLaptop):

    def scroll(self):
        print("Scrolling on DELL laptop")

# HP Notebook
class HPNotebook(HP):

    def click(self):
        print("HP Notebook Clicking")

# Dell Notebook

class DellNotebook(DELL):

    def click(self):
        print("Dell Notebook Clicking")

# Create Objects

hp = HPNotebook()

dell = DellNotebook()

# Call Methods

hp.scroll()

hp.click()

dell.scroll()

dell.click()