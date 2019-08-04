from paint import Paint


class Drawman:
    def draw(self, input_file="input.txt", output_file="output.txt"):
        inp = []
        with open(input_file, "r") as f:
            raw_input = [row.strip() for row in f]
        for raw in raw_input:
            inp.append(raw.split())

        if inp[0][0] != "C":
            raise ValueError("first parameter should be canvas, chech your inp.txt")
        else:
            picture = Paint(int(inp[0][1]), int(inp[0][2]))
            with open(output_file, "a") as f:
                f.write(f"{picture.draw_me()}\n")
            for inp_line in inp:
                token = inp_line[0]

                if token == "L":
                    x1 = int(inp_line[1])
                    y1 = int(inp_line[2])
                    x2 = int(inp_line[3])
                    y2 = int(inp_line[4])
                    picture.line(x1, y1, x2, y2)
                    with open(output_file, "a") as f:
                        f.write(f"{picture.draw_me()}\n")
                elif token == "R":
                    x1 = int(inp_line[1])
                    y1 = int(inp_line[2])
                    x2 = int(inp_line[3])
                    y2 = int(inp_line[4])
                    picture.rectangle(x1, y1, x2, y2)
                    with open(output_file, "a") as f:
                        f.write(f"{picture.draw_me()}\n")
                elif token == "B":
                    x = int(inp_line[1])
                    y = int(inp_line[2])
                    color = inp_line[3]
                    picture.bucket_fill(x, y, color)
                    with open(output_file, "a") as f:
                        f.write(f"{picture.draw_me()}\n")


dr = Drawman()
dr.draw()
