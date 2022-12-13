"""Logic Expression."""

AND = 'AND'
OR = 'OR'

class LogicExpression():
    """Logic Expression."""

    def __init__(self):
        """Constructor."""
        self.cache = None
        self.or_stack = []

    def logic(self, exp, symbol):
        """Logic concat.

            Args:
                exp (Expression): Pyarrow Dataset Expression
                symbol (str): logic symbol
        """
        if len(self.or_stack) == 0 and symbol is None:
            self.cache = exp
            return
        if OR == symbol:
            self.or_stack.append(self.cache)
            self.cache = exp
            return
        if AND ==symbol:
            self.cache = self.cache & exp

    def final_expr(self):
        """Final Expression.

            Return:
                Expression
        """
        if self.cache is not None:
            self.or_stack.append(self.cache)
        res_expr = self.or_stack[0]
        for i in range(1, len((self.or_stack))):
            sub_expr = self.or_stack[i]
            res_expr = res_expr | sub_expr
        return res_expr
