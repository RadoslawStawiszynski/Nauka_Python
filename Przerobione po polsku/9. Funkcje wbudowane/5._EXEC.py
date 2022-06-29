# EXEC jest podobny do EVAL, z tym że exec może uruchomić mini program

program = """
kroki = -3
if abs(kroki) > 0:
    print("Postać jest w ruchu")
else:
    print("Postać stoi w miejscu")
print()
"""
exec(program)
