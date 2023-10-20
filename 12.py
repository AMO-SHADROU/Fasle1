# برای جلوگیری از حالات تکراری از set  استفاده میکنیم
def a(current, target, output, s):
    if current == target:
        output.append(s)
    elif current < target:
        if (current*2, target) not in s:
            a(current*2, target, output, s | {(current*2, target)})
        if (current+3, target) not in s:
            a(current+3, target, output, s | {(current+3, target)})
