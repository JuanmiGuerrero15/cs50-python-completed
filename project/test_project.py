from project import clean_text, n_grama, counter

def test_clean_test():
    assert clean_text("Hi! How are you?") == "hi  how are you "
    assert clean_text("(okey...)") != "(okey...)"
    assert clean_text("¿Quieres comer?") == " quieres comer "


def test_n_grama():
    assert n_grama("hola") == ['hol', 'ola']
    assert n_grama("buenas que tal") == ['bue', 'uen', 'ena', 'nas', 'as ', 's q', ' qu', 'que', 'ue ', 'e t', ' ta', 'tal']
    assert n_grama("i love you") == ['i l', ' lo', 'lov', 'ove', 've ', 'e y', ' yo', 'you',]

def test_counter():
    assert counter(['hol', 'ola', 'la ', 'a a', ' am', 'ami', 'mig', 'igo']) == ({'hol': 1, 'ola': 1, 'la ': 1, 'a a': 1, ' am': 1, 'ami': 1, 'mig': 1, 'igo': 1})
    assert counter(['the', 'he ', 'e k', ' ki', 'kin', 'ing', 'ng ', 'g i', ' is', 'is ', 's t', ' th', 'thi', 'hin', 'ink', 'nki', 'kin', 'ing', 'ng ', 'g a', ' ab', 'abo', 'bou', 'out', 'ut ', 't t', ' th', 'the', 'he ', 'e t', ' th', 'thi', 'hin', 'ing', 'ng ']) == ({'ing': 3, 'ng ': 3, ' th': 3, 'the': 2, 'he ': 2, 'kin': 2, 'thi': 2, 'hin': 2, 'e k': 1, ' ki': 1, 'g i': 1, ' is': 1, 'is ': 1, 's t': 1, 'ink': 1, 'nki': 1, 'g a': 1, ' ab': 1, 'abo': 1, 'bou': 1, 'out': 1, 'ut ': 1, 't t': 1, 'e t': 1})

