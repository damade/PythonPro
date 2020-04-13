def my_generator(num):
    for i in range(num):
        yield i * 2


gen = my_generator(1000)
next(gen)
next(gen)
print(next(gen))

for item in gen:
    print(item)
