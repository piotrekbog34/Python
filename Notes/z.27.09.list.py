a = [1, 2, 3]
b = [3, 2, 1]

a + b # łączy listy


nums = [1, 2, 3, 4]
for i in range (len(nums)):
    nums[i] = str(nums[i])
"".join(nums)

"1234"


phones = {
    "11-22-55": "Bob Marley",
}

print(phones["11-22-55"])



data = {
    42:1,
    43:"????",
    44: [1, 1, 3, 4],
    45: {
        "a": "b"
    }
}



phones = {
     "Bob Marley" : "11-22-55",
}
for key, value in phones.items():
    print(key, value)



phones = {
     "Bob Marley" : "11-22-55",
}

items = phones.items()
for key, value in list(items):
    phones[value] = key
print(phones)



if key not in phones.keys():
    print("Unknown key")
else:
    print(phones[key])



# UpSert = Update + Insert

phones_a ={

}
phones_b = {

}

phones_c = {}
phones_c.update(phones_a)
phones_c.update(phones_b)


list
tuple
dict
set

