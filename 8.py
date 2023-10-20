def print_truth_table(num_propositions):
    if num_propositions <= 0:  # پایه شرط توقف
        return

    truth_values = [False] * num_propositions  # حالت‌های درستی/غلطی را ذخیره کنید

    def generate_truth_table_helper(idx):
        if idx == num_propositions:  # شرط توقف
            print(truth_values)
        else:
            truth_values[idx] = False
            generate_truth_table_helper(idx + 1)
            truth_values[idx] = True
            generate_truth_table_helper(idx + 1)

    generate_truth_table_helper(0)

# در اینجا تعداد گزاره ها را به عنوان ورودی تابع پاس می دهیم
print_truth_table(3)  # مثال با سه گزاره