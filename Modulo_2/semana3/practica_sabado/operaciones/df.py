class DF_Modelo:

    def __init__(self, valor_x, xi, fi, Fi, fr, Fr) -> None:
        self.valor_x = valor_x
        self.xi = xi
        self.fi = fi
        self.Fi = Fi
        self.fr = fr
        self.Fr = Fr

    def __iter__(self):
        return iter([self.valor_x, self.xi, self.fi, self.Fi, self.fr, self.Fr])