def masukin_pw():
    password_benar = "AnjaiMabar"

    print("Masukin password dulu le...")

    percobaan = 1

    while percobaan <= 3:

        password_input = input("Masukin password: ")

        if password_input == password_benar:

            print("Gokil bre, ayo mabar sekarang!")
            break

        else:

            print("Waduh, passwordnya salah nih!")
            percobaan += 1

    else:
        print("Game Over! Sorry bre kita gabisa mabar!")

masukin_pw()