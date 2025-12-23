import pandas as pd

# Δεδομένα Εισόδου
customers = [
    {
        "name": "Άννα",
        "surname": "Παπαδοπούλου",
        "email": "anna@example.com",
        "age": 28,
        "profession": "Ιατρός",
    },
    {
        "name": "Κώστας",
        "surname": "Νικολάου",
        "email": "kostas@example.com",
        "age": 35,
        "profession": "Μηχανικός Η/Υ",
    },
    {
        "name": "Ιωάννα",
        "surname": "Γεωργίου",
        "email": "ioanna@example.com",
        "age": 22,
        "profession": "Καθηγήτρια",
    },
]

# Λίστες για τη διατήρηση των διαχωρισμένων δεδομένων
pseudonymized_data = []
mapping_table = []

# Διαδικασία Ψευδωνυμοποίησης για κάθε πελάτη
for index, person in enumerate(customers, start=1):
    # Δημιουργία του ψευδωνύμου (π.χ., USER1, USER2)
    user_id = f"USER{index}"

    # 1. Δημιουργία της Ψευδωνυμοποιημένης Εγγραφής (Δεδομένα προς κοινοποίηση)
    # Αφαίρεση ονόματος, επωνύμου και email. Διατήρηση Ηλικίας και Επαγγέλματος.
    pseudo_record = {
        "User_ID": user_id,
        "Age": person["age"],
        "Profession": person["profession"],
    }
    pseudonymized_data.append(pseudo_record)

    # 2. Δημιουργία της Εγγραφής Αντιστοίχισης (Το κλειδί για επαναταυτοποίηση)
    # Σύνδεση του ψευδωνύμου με τα πραγματικά αναγνωριστικά.
    map_record = {
        "User_ID": user_id,
        "Name": person["name"],
        "Surname": person["surname"],
        "Email": person["email"],
    }
    mapping_table.append(map_record)

# 3.1 Εξαγωγή πίνακα προς κοινοποίηση
print("--- 1. Ψευδωνυμοποιημένα Δεδομένα (Ασφαλή για Κοινοποίηση) ---")
df_pseudo = pd.DataFrame(pseudonymized_data)
print(df_pseudo.to_string(index=False))

print("\n")

# 3.2 Εξαγωγή πίνακα αντιστοίχισης
print("--- 2. Πίνακας Αντιστοίχισης (Πρέπει να αποθηκεύεται με ασφάλεια και ξεχωριστά) ---")
df_map = pd.DataFrame(mapping_table)
print(df_map.to_string(index=False))

# 4. Γιατί η ψευδωνυμοποίηση βοηθά στην προστασία των προσωπικών δεδομένων, σύμφωνα με τον GDPR
"""
Η ψευδωνυμοποίηση αντικαθιστά τα άμεσα αναγνωριστικά (όπως ονόματα) με τεχνητούς κωδικούς.
Αυτό βοηθά στην προστασία των προσωπικών δεδομένων επειδή τα δεδομένα δεν μπορούν να αποδοθούν σε 
ένα συγκεκριμένο άτομο χωρίς τη χρήση πρόσθετων πληροφοριών (του πίνακα αντιστοίχισης).
Σύμφωνα με το GDPR, εφόσον ο πίνακας αντιστοίχισης διατηρείται ξεχωριστά και με ασφάλεια,
ο κίνδυνος για τα υποκείμενα των δεδομένων μειώνεται σημαντικά σε περίπτωση παραβίασης δεδομένων.
"""
