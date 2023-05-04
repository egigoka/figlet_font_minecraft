from commands import *


def replace_symbols(in_):
	out = in_

	out_end = ""
	if len(out) == 0:
		return ""
	if len(out) == 1:
		out += " "
	if out[1] not in "▄▀█ ":
		out_end = out[1]
		out = out[0] + " "
	
	out = out.replace("  ", " ") # 0
	
	out = out.replace("▀ ", "▘") # 1
	
	out = out.replace("▄ ", "▖") # 2
	
	out = out.replace("█ ", "▌") # 3
	
	out = out.replace(" ▀", "▝") # 4
	
	out = out.replace("▀▀", "▀") # 5
	
	out = out.replace("▄▀", "▞") # 6
	
	out = out.replace("█▀", "▛") # 7
	
	out = out.replace(" ▄", "▗") # 8
	
	out = out.replace("▀▄", "▚") # 9
	
	out = out.replace("▄▄", "▄") # 10
	
	out = out.replace("█▄", "▙") # 11
	
	out = out.replace(" █", "▐") # 12
	
	out = out.replace("▀█", "▜") # 13
	
	out = out.replace("▄█", "▟") # 14
	
	out = out.replace("██", "█") # 15

	out += out_end
	
	return out


file = "minecraft.flf"

out_file = "minecraft_condenced.flf"

content = File.read(file)

lines = Str.nl(content)

out = ""

for cnt, line in enumerate(lines):
	out_line = ""

	sublines = List.split_every(line, 2)

	print(cnt, sublines)
	for subline in sublines:
		out_line += replace_symbols(subline)

	print(cnt, '"' + out_line + '"')
	
	out += out_line + newline
	
	
File.write(out_file, out, mode="w")
