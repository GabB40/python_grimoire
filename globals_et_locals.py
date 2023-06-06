def foo():
    b = 5
    print(f" locals in foo() : {[l for l in locals() if not l.startswith('__')]}")
    print(f" globals in foo() : {[l for l in globals() if not l.startswith('__')]}")
    print(b)
    
a = 5
foo()

print()
print(f" locals in file() : {[l for l in locals() if not l.startswith('__')]}")
print(f" globals in file() : {[l for l in globals() if not l.startswith('__')]}")