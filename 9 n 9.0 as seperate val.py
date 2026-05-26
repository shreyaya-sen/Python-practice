values ={
    9,9.0
}
print(values)
#invalid as  both number will not be printed seperately 
# python always assumes them to be a single same value
new ={
    "9",9.0
}
print(new)

new2 ={
    ("float","9.0"),
    ("int","9")
}
print(new2)