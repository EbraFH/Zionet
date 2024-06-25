
# param for the stripes row in the flag
STRIPE_ROW = 2

@staticmethod
def star_size(width, height):
    """
    Method calculates flag star size
    :return: return a star size
    """
    return min(width, height) // 4

def padding(width, height):
    """
    Method calculates flag padding space 
    :return: return a space size padding for the flag
    """
    stripe_height = max(1, height // 10)
    middle_section_height = height - 2 * stripe_height
    return (middle_section_height - star_size(width, height) ) // 4

def column_of_star(size):
    """
    Method calculates star column 
    :return: return star column
    """
    return base_of_star(size) * 3 - 2

def rows_of_star(size):
    """
    Method calculates star rows 
    :return: return star rows
    """
    return base_of_star(size) * 2 -1

def base_of_star(size):
    """
    Method calculates star base 
    :return: return star base
    """
    base = size//3
    if base % 2 == 0 :
        return base + 1
    return base