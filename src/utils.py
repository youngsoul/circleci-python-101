import arrow

def to_upper(p1:str):
    return p1.upper()


def utc_to_central():
    return arrow.utcnow().to("US/Central")