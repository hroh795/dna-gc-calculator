sequence = "ATGCGCGTA"

g_count = sequence.count("G")
c_count = sequence.count("C")

gc_content = (g_count + c_count) / len(sequence) *100

print(gc_content)