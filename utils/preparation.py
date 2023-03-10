from pandas import Series


def get_max_floor(raw_floor: str) -> int | None:
    if not raw_floor or type(raw_floor) != str:
        return

    stripped_tokens = [int(t.strip()) for t in raw_floor.split('из')]

    if len(stripped_tokens) == 2:
        return stripped_tokens[-1]

    return


def get_current_floor(raw_floor: str) -> int | None:
    if not raw_floor or type(raw_floor) != str:
        return

    stripped_tokens = [int(t.strip()) for t in raw_floor.split('из')]

    return stripped_tokens[0]


def get_security_types(security: Series) -> list:
    security_types = []

    for row in security.unique():
        if type(row) != str:
            continue
        tokens = [r.strip() for r in row.split(',')]
        for token in tokens:
            if token not in security_types:
                security_types.append(token)

    return security_types


def has_token(security: str, token: str) -> str:
    if type(security) == str and token in security:
        return 'да'
    return 'нет'


def check_true(text: str) -> int:
    positive_tokens = ('да', 'возможен обмен')
    for token in positive_tokens:
        if token in text.lower():
            return 1
    return 0
