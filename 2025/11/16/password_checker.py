# password_checker.py
# 2025-11-16 - パスワード強度チェッカー

print("=== パスワード強度チェッカー ===\n")

password = input ("パスワードを入力してね: ")

has_digit = any(c.isdigit() for c in password)
has_upper = any(c.isupper() for c in password)
has_symbol = any(c in "!@#$%^&*" for c in password)
length = len(password)

if length >= 12 and has_digit and has_upper and has_symbol:
  print("判定：最強！")
  print("素晴らしいパスワードだね！")
elif length >= 8 and has_digit and has_upper: 
  print("判定：強い")
  print("良いパスワードだよ！")
elif length >= 8 and has_digit:
  print("判定：普通")
  print("まあまあかな。")
else:
  print("判定：弱い")
  print("もうちょっと工夫しようね")
