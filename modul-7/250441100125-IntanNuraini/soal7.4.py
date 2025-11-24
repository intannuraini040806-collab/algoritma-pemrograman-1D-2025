# ekstrakulikuler = {}
renang = {"rara","rudi","mitha","sandi"}
basket = {"rara","dila","dandi","sandi"}
ekstrakulikuler1 = renang.intersection(basket)
ekstrakulikuler2 = basket.intersection(renang)
ekstrakulikuler3 = renang.difference(basket)
ekstrakulikuler4 = basket.difference(renang)
ekstrakulikuler5 = renang.union(basket)
print("siswa yang mengikuti ektra renang dan basket",ekstrakulikuler5)
print("siswa yang hanya mengikuti ekstrakulikuler renang hanya:",ekstrakulikuler3,ekstrakulikuler4)
print("siswa yang mengikuti dua ekstra : ",ekstrakulikuler1)
print("siswa unik yg mengikuti kedua klub yaitu",len(ekstrakulikuler2))