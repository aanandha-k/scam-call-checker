import requests

def main():
    print("Phone input format Example: +1234567890")
    while True:
        phone = input("Enter a phone number ")
        if validate_phone(phone) is None:
            continue
        else:
            phone = validate_phone(phone)
            break
    print("------------------------MENU------------------------")
    print("1. Check Phone Number")
    print("2. Report Phone Number")
    value = input("Number:  ")
    if value == "1":
        check(phone)
    elif value == "2":
        add_entry(phone)
    else:
        print("❌ Invalid Input")

def validate_phone(phone):
    phone = phone.strip().replace("-" ,"").replace(" " , "").replace("(" , "").replace(")" , "").replace("." , "")
    if not phone.startswith("+"):
        print("❌ Phone number must include country code (e.g., +91...)")
        return None

    if not phone[1:].isdigit():
        print("❌ Phone number can only contain digits after +")
        return None

    if len(phone) < 8 or len(phone) > 16:
        print("❌ Invalid phone number length")
        return None
    return phone


def validate_category():
    while True:
        print("Scam categories:")
        print("1. Bank Fraud")
        print("2. IRS scam")
        print("3. Government scam")
        print("4. Tech support scam")
        value = input("Enter category (1-4): ")

        category_dict = {
            "1": "Bank fraud",
            "2": "IRS scam",
            "3": "Government scam",
            "4": "Tech support scam"
        }

        if value not in category_dict:
            print("❌ Invalid category")
            continue
        return category_dict[value]

def check(phone):
    try:
        response = requests.get("https://695927116c3282d9f1d6bf81.mockapi.io/numbers")
        response.raise_for_status()

        #Checking Number

        data = response.json()
        for entry in data:
            if entry["number"] == phone:
                if entry["reported"]:
                    category = entry["category"]
                    reports = entry["reports"]
                    print()
                    print(f"🔴 Scam detected! for {phone}")
                    if 1 <= reports <= 3:
                        risk = "Low"
                    elif 4 <= reports <= 7:
                        risk = "Moderate"
                    else:
                        risk = "High"
                    print(f"Risk Level: {risk}")
                    print(f"Category: {category}")
                    print(f"Reports: {reports}")
                    print()
                    print("Check Complete")
                    explain_risk(category , reports , risk)
                    break
                else:
                    print("✅ This number has no scam reports.")
                    print("Check Complete")
                    break
        else:
            print("🔵 No information available for this number.")
            print("Check Complete")

        #Handling All Error That Can Be Raised

    except(requests.exceptions.RequestException):
        print("🛜 The database failed. Please try again later.")
    except(requests.exceptions.JSONDecodeError):
        print("🖥️ Database could not be loaded. Please try again later.")
    except(TypeError, KeyError):
        print("📊 Data format error. Please try again later.")


def explain_risk(category, reports , risk):
    category_dict = {
        "Bank fraud" : "Callers may impersonate banks to obtain sensitive details.",
        "IRS scam" : "Callers may threaten legal action to pressure victims.",
        "Government scam" : "Callers may threaten legal action to pressure victims." ,
        "Tech support scam" : "Callers claim technical issues to gain remote access."}
    if risk == "Low":
        risk_expl = "Only a few reports exist, but caution is advised."
    elif risk == "Moderate":
        risk_expl = "Multiple independent reports suggest a pattern."
    else:
        risk_expl = "Numerous reports indicate a well-established scam."
    category_expl = category_dict.get(category)
    print()
    print("🌀 Why is it dangerous?")
    print()
    if category_expl is None:
        print(f"This number has been reported for suspicious behavior, but there is limited information about the specific scam type")
        print()

    else:
        print(f"This number is linked to {category}. {category_expl}")
        print(f"It has been reported by {reports} , suggesting a {risk} risk: {risk_expl}")
        print()
    print("🎬 What Should You Do?")
    print()
    print(give_advise(risk))
    print("🕵️ Do not share sensitive info")

def give_advise(risk):
    if risk == "Low":
        return "️🎯 Risk Level: Low – only a few reports exist, remain alert."
    elif risk == "Moderate":
        return "🛑 Risk Level: Moderate – multiple reports suggest a scam pattern don't engage with the caller."
    else:
        return "🔴 Risk Level: High – numerous reports indicate a serious scam Hang up immediately."


def add_entry(phone):
    try:
        category = validate_category()
        response = requests.get("https://695927116c3282d9f1d6bf81.mockapi.io/numbers")
        response.raise_for_status()
        data = response.json()

        number_exists = False
        for entry in data:
            if entry["number"] == phone:
                number_exists = True
                entry_id = entry["id"]
                current_reports = entry.get("reports", 0)

                updated_data = {
                    "number": phone,
                    "reported": True,
                    "reports": current_reports + 1,
                    "category": category
                }

                update_response = requests.put(
                    f"https://695927116c3282d9f1d6bf81.mockapi.io/numbers/{entry_id}",
                    json=updated_data
                )

                if update_response.status_code == 200:
                    print("✅ Report count updated!")
                else:
                    print("❌ Failed to update")
                break

        if not number_exists:
            new_entry = {
                "number": phone,
                "reported": True,
                "reports": 1,
                "category": category
            }

            post_response = requests.post(
                "https://695927116c3282d9f1d6bf81.mockapi.io/numbers",
                json=new_entry
            )

            if post_response.status_code == 201:
                print("✅ Scam reported successfully!")
            else:
                print("❌ Failed to report")

    except requests.exceptions.RequestException:
        print("🛜 The database failed. Please try again later.")
    except requests.exceptions.JSONDecodeError:
        print("🖥️ Database could not be loaded. Please try again later.")
    except (TypeError, KeyError):
        print("📊 Data format error. Please try again later.")


if __name__ == "__main__":
    main()
