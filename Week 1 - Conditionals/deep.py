def main():
    secret = input("What is the secret of life? ").strip().lower()
    valid_answers = {"42","forty two","forty-two"}
    if secret in valid_answers:
        print("Yes")
    else:
        print("No")

main()