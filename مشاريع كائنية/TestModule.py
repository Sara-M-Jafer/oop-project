from main import Student, StudentManager

def main():
    manager = StudentManager()

    while True:
        print("\n========== إدارة الطلاب ==========")
        print("1 - إضافة طالب")
        print("2 - عرض كل الطلاب")
        print("3 - تحديث بيانات طالب")
        print("4 - حذف طالب")
        print("5 - خروج")
        print("===================================")

        choice = input("اختر الخيار: ")

        # ------------------ إضافة طالب ------------------
        if choice == "1":
            try:
                student_id = int(input("ID ادخل: "))
                name = input("ادخل اسم الطالب: ")
                age = int(input("ادخل العمر: "))
                department = input("ادخل القسم: ")
                gpa = float(input("ادخل المعدل (0 - 4): "))

                student = Student(student_id, name, age, department, gpa)
                manager.add_student(student)

            except ValueError:
                print(" خطأ: يرجى إدخال قيم صحيحة (أرقام للمعدل والعمر).")

        # ------------------ عرض الطلاب ------------------
        elif choice == "2":
            manager.show_all()

        # ------------------ تحديث طالب ------------------
        elif choice == "3":
            try:
                student_id = int(input("ادخل ID الطالب المراد تحديثه: "))

                print("اترك الحقل فارغ إذا ما تريد تعدله")

                new_name = input("اسم جديد: ")
                new_age_input = input("عمر جديد: ")
                new_department = input("قسم جديد: ")
                new_gpa_input = input("معدل جديد: ")

                new_age = int(new_age_input) if new_age_input else None
                new_gpa = float(new_gpa_input) if new_gpa_input else None

                manager.update_student(student_id, new_name or None, new_age, new_department or None, new_gpa)

            except ValueError:
                print(" خطأ: إدخال غير صالح.")

        # ------------------ حذف طالب ------------------
        elif choice == "4":
            try:
                student_id = int(input("ادخل ID الطالب المراد حذفه: "))
                manager.delete_student(student_id)
            except ValueError:
                print(" يرجى إدخال رقم صحيح.")

        # ------------------ خروج ------------------
        elif choice == "5":
            print("تم الخروج من البرنامج.")
            break

        else:
            print(" خيار غير صحيح، حاول مرة أخرى.")

if __name__ == "__main__":
    main()


