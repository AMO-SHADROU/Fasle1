def is_duplicate(s):
    if not s:  # رشته به طول صفر Duplicate است
        return True
    if len(s) % 2 != 0:  # رشته به طول فرد نمی‌تواند Duplicate باشد
        return False
    s1 = s[:len(s)//2]  # زیر رشته اول
    s2 = s[len(s)//2:]  # زیر رشته دوم
    if s1 == s2:  # s به فرم s1s1 است
        return is_duplicate(s1)  # بررسی s1
    s2 = s2[1:]  # حذف اولین کاراکتر از زیر رشته دوم
    if is_duplicate(s2):  # بررسی باقی مانده از s
        return is_duplicate(s2)  # بررسی s2
    return False