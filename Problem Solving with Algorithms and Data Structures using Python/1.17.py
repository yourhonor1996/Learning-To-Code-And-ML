''' Implement the simple methods get_num and get_den that will return the numerator and denominator of a fraction.'''
import fractions as fc
class Fraction:
    def __init__(self, fraction:str) -> None:
        self.fraction = fraction
        self.numerator = Fraction.get_num(self.fraction)
        self.denomenator = Fraction.get_den(self.fraction)
        self.gcd = fc.gcd(self.numerator, self.denomenator)
        self.reduced_fraction = self.numerator/
    
    
    @classmethod
    def get_num(fraction:str) -> int:
        """Gets the numerator of the given fraction in string

        Args:
            fraction (str): The given fraction in string

        Returns:
            int: The numerator of the fraction
        """
        numerator, denomenator = fraction.split("/")
        return int(numerator)
    
    @classmethod
    def get_den(fraction:str) -> int:
        """Returns the denomenator of the given fraction

        Args:
            fraction (str): The given fraction in string

        Returns:
            int: Returns the denomenator of the given fraction
        """
        numerator, denomenator = fraction.split("/")
        return int(denomenator)

        
    
    
    
    
    