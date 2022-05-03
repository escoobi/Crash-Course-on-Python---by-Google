def email_list(domains):
    emails = []
    for dominio in domains:
        for user in domains[dominio]:
            emails.append("{}@{}".format(dominio, user))
    return(", ".join(emails))

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))