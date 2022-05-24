# Purpose: Record progress and problems..

# Levels:        NotSet, Debug, Info, Warning, Error, Critical
# Numeric Value:    0,    10,    20,    30,      40,     50
import logging

# Create and configure logger 
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"  # Log message format manually set.

logging.basicConfig(filename = "C:\\Users\\Owner\Documents\\Python made easy\\13.1_Test_Logging.Log",    # File pathway (change if needed).
                    level = logging.DEBUG,  # level set to DEBUG and above to see all levels of errors.
                    format = LOG_FORMAT,    # formats the error messages using the standard made above in "LOG_FORMAT" variable.
                    filemode = 'w')         # By default, the filemode is 'a', this manually sets it to overwrite all messages in debug file.

logger = logging.getLogger()

# Test messages 
logger.debug("Debug test message")
logger.info("Info test message")
logger.warning("Warning test message")
logger.error("Error test message")
logger.critical("Critical test message")

#================================================================
import math # To use sqrt function

# Quadratic Formula 
# Solutions to ax^2 + bx+c = 0 are x = -b+- sqrt(b^2 -4ac) / 2a

def quadratic_formula(a, b, c):
    """Return the solutions to the equation ax^2 + bx + c = 0."""
    logger.info("quadratic_formula({0}, {1}, {2})".format(a, b, c))

    # Compute the discriminant
    logger.debug("# Compute the discriminant")
    disc = b**2 - 4*a*c

    # Compute the two roots
    logger.debug("# Compute the two roots")
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)

    # Return the roots
    logger.debug("# Return the roots")
    return (root1, root2)

# Testing the program with a proper input
roots1 = quadratic_formula(1, 0, -4)
print(roots1)

# Causing an error to occur and using the logger to find where the problem is located.
roots2 = quadratic_formula(1, 0, 1)
print(roots2)
