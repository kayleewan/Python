name = input("你好，请问你叫什么名字？")
#print("很高兴认识你，", name, name, name)
#print("很高兴认识你，{0}, {1}, {2}".format(name, name, name))
#print("很高兴认识你，{0}, {1}, {2}".format("name", "name2", "name3"))
print("很高兴认识你，{0:<8}, {0:^8}, {0:>8}".format(name))