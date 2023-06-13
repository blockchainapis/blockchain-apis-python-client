from BlockchainAPIsTester import BlockchainAPIsTester

class TestTokenDecimalForm(BlockchainAPIsTester):
    async def test_to_decimal(self):
        decimal_form = self.api.get_token_decimal_form(2500000000000000000, 18)
        self.assertEqual(decimal_form, "2.5")

    async def test_to_decimal_short(self):
        decimal_form = self.api.get_token_decimal_form(2504000000000000000, 18)
        self.assertEqual(decimal_form, "2.504")

    async def test_to_decimal_long(self):
        decimal_form = self.api.get_token_decimal_form(2500000000000000001, 18)
        self.assertEqual(decimal_form, "2.500000000000000001")

    async def test_to_decimal_no_decimal(self):
        decimal_form = self.api.get_token_decimal_form(2000000000000000000, 18)
        self.assertEqual(decimal_form, "2")
