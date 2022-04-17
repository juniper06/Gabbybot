from discord.ext import commands
from ttg import Truths


class Student(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    @commands.command(aliases=["ttg", "truthtable"])
    async def truth_table(self, ctx, pros: str, *, comps: str):
        """Truth table

                Args:
                    pros (str): variables
                    comps (str): compound propositions
                Logic operators:
                    Negation: ~, -, not
                    Conjunction: and, v
                    Disjunction: ^, or
                    Exclusive Or: xor, !=
                    implication: ->, =>
                    Biconditional: =
                Examples:
                    *ttg pq p^q pvq -pv-q
                    +-----+-----+-----------+----------+--------------+
                    |  p  |  q  |  p and q  |  p or q  |  - p or - q  |
                    |-----+-----+-----------+----------+--------------|
                    |  1  |  1  |     1     |    1     |      0       |
                    |  1  |  0  |     0     |    1     |      1       |
                    |  0  |  1  |     0     |    1     |      1       |
                    |  0  |  0  |     0     |    0     |      1       |
                    +-----+-----+-----------+----------+--------------+
        """

        def repl(x: str):
            x = " ".join(x)
            x = x.replace("^", "and")
            x = x.replace("v", "or")
            x = x.replace("->", "=>")
            return x

        pros = list(pros.strip(" "))
        comps = list(map(repl, list(comps.split(" "))))
        table = Truths(pros, comps, ints=True)
        print(table)
        await ctx.send(f"```py\n{table}\n```")


def setup(client):
    client.add_cog(Student(client))
