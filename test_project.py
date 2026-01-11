import project as p

def test_validate_phone():
    assert p.validate_phone("+1 - 4155550100") == "+14155550100"
    assert p.validate_phone("hi how are you") == None
    assert p.validate_phone("938434839") == None
    assert p.validate_phone("+ -1(4155550100.)") == "+14155550100"
    assert p.validate_phone("873987645678134970") == None
    assert p.validate_phone("1122000") == None



def test_category_phone(monkeypatch):
    monkeypatch.setattr('builtins.input' , lambda _: "1")
    assert p.validate_category() == "Bank fraud"
    monkeypatch.setattr('builtins.input' , lambda _: "2")
    assert p.validate_category() == "IRS scam"
    monkeypatch.setattr('builtins.input' , lambda _: "3")
    assert p.validate_category() == "Government scam"
    monkeypatch.setattr('builtins.input' , lambda _: "4")
    assert p.validate_category() == "Tech support scam"



def test_give_advise():
    assert p.give_advise("Low") == "️🎯 Risk Level: Low – only a few reports exist, remain alert."
    assert p.give_advise("Moderate") == "🛑 Risk Level: Moderate – multiple reports suggest a scam pattern."
    assert p.give_advise("High") == "🔴 Risk Level: High – numerous reports indicate a serious scam."
