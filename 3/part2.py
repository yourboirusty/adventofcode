f = open('3/input')
lines = f.readlines()
lines = [line[:-1] for line in lines]
lgt = len(lines[0])
lines_oxygen = lines.copy()
lines_co2 = lines.copy()
for i in range(lgt):
    if len(lines_oxygen) > 1:
        num_lines = len(lines_oxygen)
        count_ones = [li[i] for li in lines_oxygen].count("1")
        most_common = "1" \
            if count_ones >= num_lines / 2 \
            else "0"
        lines_oxygen = [li for li in lines_oxygen
                        if li[i] == most_common]
    if len(lines_co2) > 1:
        num_lines = len(lines_co2)
        count_zeros = [li[i] for li in lines_co2].count("0")
        least_common = "0" \
            if count_zeros <= num_lines / 2 \
            else "1"
        lines_co2 = [li for li in lines_co2
                    if li[i] == least_common]

print(f"{int(lines_oxygen[0],2) * int(lines_co2[0],2)}")