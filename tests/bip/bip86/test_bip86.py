# Copyright (c) 2021 Emanuele Bellocchia
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


# Imports
import unittest
from bip_utils import Bip86, Bip44Coins, Bip49Coins, Bip84Coins, Bip86Coins
from tests.bip.bip44_base.test_bip44_base import Bip44BaseTestHelper
from tests.bip.bip44.test_bip44 import TEST_SEED

# Some tests from BIP-0086 page
# https://github.com/bitcoin/bips/blob/master/bip-0086.mediawiki
TEST_VECT = [
    # Bitcoin
    {
        "coin": Bip86Coins.BITCOIN,
        "names": ("Bitcoin", "BTC"),
        "is_testnet": False,
        "seed": b"5eb00bbddcf069084889a8ab9155568165f5c453ccb85e70811aaed6f6da5fc19a5ac40b389cd370d086206dec8aa6c43daea6690f20ad3d8d48b2d2ce9e38e4",
        "ex_master": "xprv9s21ZrQH143K3GJpoapnV8SFfukcVBSfeCficPSGfubmSFDxo1kuHnLisriDvSnRRuL2Qrg5ggqHKNVpxR86QEC8w35uxmGoggxtQTPvfUu",
        "wif_master": "Kx2nc8CerNfcsutaet3rPwVtxQvXuQTYxw1mSsfFHsWExJ9xVpLf",
        "account": {
            "ex_pub": "xpub6BgBgsespWvERF3LHQu6CnqdvfEvtMcQjYrcRzx53QJjSxarj2afYWcLteoGVky7D3UKDP9QyrLprQ3VCECoY49yfdDEHGCtMMj92pReUsQ",
            "ex_priv": "xprv9xgqHN7yz9MwCkxsBPN5qetuNdQSUttZNKw1dcYTV4mkaAFiBVGQziHs3NRSWMkCzvgjEe3n9xV8oYywvM8at9yRqyaZVz6TYYhX98VjsUk",
        },
        "chain_ext": {
            "ex_pub": "xpub6EmR4gT2Lt7tseJfws6sm6Mvkc1yEoF6WiZS7Ppxj39xqy8VbCbCenCsWmFnwupZoq1Mq1EnAQtq38bb8RnwAE5epc965k8cjqKpi8NNGZY",
            "ex_priv": "xprvA1n4fAv8WWZbfAECqqZsPxRCCaBUqLXF9VdqK1RMAhcyyAoM3fGx6ytPfVrTHMhqLqGLJP4pgLBsQKYb53tnM3vSDPS6U756uWfrF2TpcXS",
        },
        "addresses": [
            "bc1p5cyxnuxmeuwuvkwfem96lqzszd02n6xdcjrs20cac6yqjjwudpxqkedrcr",
            "bc1p4qhjn9zdvkux4e44uhx8tc55attvtyu358kutcqkudyccelu0was9fqzwh",
            "bc1p0d0rhyynq0awa9m8cqrcr8f5nxqx3aw29w4ru5u9my3h0sfygnzs9khxz8",
            "bc1py0vryk8aqusz65yzuudypggvswzkcpwtau8q0sjm0stctwup0xlqkkxler",
            "bc1pjpp8nwqvhkx6kdna6vpujdqglvz2304twfd308ve5ppyxpmcjufs7k6xyr",
        ],
    },
    # Bitcoin test net
    {
        "coin": Bip86Coins.BITCOIN_TESTNET,
        "names": ("Bitcoin TestNet", "BTC"),
        "is_testnet": True,
        "seed": b"5eb00bbddcf069084889a8ab9155568165f5c453ccb85e70811aaed6f6da5fc19a5ac40b389cd370d086206dec8aa6c43daea6690f20ad3d8d48b2d2ce9e38e4",
        "ex_master": "tprv8ZgxMBicQKsPe5YMU9gHen4Ez3ApihUfykaqUorj9t6FDqy3nP6eoXiAo2ssvpAjoLroQxHqr3R5nE3a5dU3DHTjTgJDd7zrbniJr6nrCzd",
        "wif_master": "cNPn53CWHSMt3MMr3HrymFzxaeDwZrZF2yAEZJ7knzAFD3GTTi2x",
        "account": {
            "ex_pub": "tpubDC3pD7UZXnsgh3EBjbtBQiB1FnLask7UHBSunZ1DPK4dCFFZoFRkgxHB8gt42FvLzx1DpxfHWxAsYaY6b643RVcGjDxXxns7wKKYnnfEcbB",
            "ex_priv": "tprv8fMn4hSKPRC1oaCPqxDb1JWtgkpeiQvZhsr8W2xuy3GEMkzoArcAWTfJxYb6Wj8XNNDWEjfYKK4wGQXh3ZUXhDF2NcnsALpWTeSwarJt7Vc",
        },
        "chain_ext": {
            "ex_pub": "tpubDF93avGi4A5M9SVXQ45xy1hJ5j7dEBkA4M9jTwt74wurbFoCfRSHoDshkoLaUQmobjYGSakehWisjK6CXHeB3fXwtCtPmGnrKnvEU6u8NwV",
            "ex_priv": "tprv8iT1SWETunPgFyTjWQRNZc3BWhbh4rZFV3YxBRqoeg7TkmYS32chcjFqag27Hj69iGo7JUgaqgmfsB6LCGEjA7C2k2eQ8To9pcRGge7hhCz",
        },
        "addresses": [
            "tb1p5cyxnuxmeuwuvkwfem96lqzszd02n6xdcjrs20cac6yqjjwudpxqp3mvzv",
            "tb1p4qhjn9zdvkux4e44uhx8tc55attvtyu358kutcqkudyccelu0wasjpkd5c",
            "tb1p0d0rhyynq0awa9m8cqrcr8f5nxqx3aw29w4ru5u9my3h0sfygnzsj7pfcg",
            "tb1py0vryk8aqusz65yzuudypggvswzkcpwtau8q0sjm0stctwup0xlqp7ssrv",
            "tb1pjpp8nwqvhkx6kdna6vpujdqglvz2304twfd308ve5ppyxpmcjufsf7vf7v",
        ],
    },
]

# Tests for default path derivation
TEST_VECT_DEFAULT_PATH = [
    # Bitcoin
    {
        "coin": Bip86Coins.BITCOIN,
        "seed": b"5eb00bbddcf069084889a8ab9155568165f5c453ccb85e70811aaed6f6da5fc19a5ac40b389cd370d086206dec8aa6c43daea6690f20ad3d8d48b2d2ce9e38e4",
        "default_address": "bc1p5cyxnuxmeuwuvkwfem96lqzszd02n6xdcjrs20cac6yqjjwudpxqkedrcr",
    },
    # Bitcoin test net
    {
        "coin": Bip86Coins.BITCOIN_TESTNET,
        "seed": b"5eb00bbddcf069084889a8ab9155568165f5c453ccb85e70811aaed6f6da5fc19a5ac40b389cd370d086206dec8aa6c43daea6690f20ad3d8d48b2d2ce9e38e4",
        "default_address": "tb1p5cyxnuxmeuwuvkwfem96lqzszd02n6xdcjrs20cac6yqjjwudpxqp3mvzv",
    },
]

# Tests for different key formats
TEST_VECT_KEY_FORMATS = {
    "coin": Bip86Coins.BITCOIN,
    "seed": "5eb00bbddcf069084889a8ab9155568165f5c453ccb85e70811aaed6f6da5fc19a5ac40b389cd370d086206dec8aa6c43daea6690f20ad3d8d48b2d2ce9e38e4",
    "ex_priv": "xprv9s21ZrQH143K3GJpoapnV8SFfukcVBSfeCficPSGfubmSFDxo1kuHnLisriDvSnRRuL2Qrg5ggqHKNVpxR86QEC8w35uxmGoggxtQTPvfUu",
    "raw_priv": "1837c1be8e2995ec11cda2b066151be2cfb48adf9e47b151d46adab3a21cdf67",
    "ex_pub": "xpub661MyMwAqRbcFkPHucMnrGNzDwb6teAX1RbKQmqtEF8kK3Z7LZ59qafCjB9eCRLiTVG3uxBxgKvRgbubRhqSKXnGGb1aoaqLrpMBDrVxga8",
    "raw_compr_pub": "03d902f35f560e0470c63313c7369168d9d7df2d49bf295fd9fb7cb109ccee0494",
    "raw_uncompr_pub": "04d902f35f560e0470c63313c7369168d9d7df2d49bf295fd9fb7cb109ccee04947d000a1345d3845dd83b4c5814f876c918305b598f066c958fad972bf59f2ec7",
}

# Tests for extended keys with valid and invalid depths
TEST_VECT_EX_KEY_DEPTHS = {
    # Private key with depth 5 is fine
    "ex_priv_5": "xprvA47LQAPDXEkr9wwtUHNta4qWqiobTGKppzVy5JZVCszLdGTTQbuRxRMCJGqSdBg91M13Z2RTP2BKU5yDD41WFwZ7yavhhbCEs7cTnyvkxJV",
    # Private key with depth 6 shall raise an exception
    "ex_priv_6": "xprvA69uJSR3uVgvYFM5AFabGnMuAvtdLrbm84CwEieMBbk5Kjk9ZGeYPF4AWuJ9EPBzC8pLn117Y6TFqgNKZ6EVKmoDxT4EjT1BaG3RhWL6wdF",
    # Public key with depth 2 shall raise an exception
    "ex_pub_2": "xpub6AmukNpN4yyLgyzSysjU6JqqoYA1mVUvtinHYdBGPDppatJXHxT8CcDsmBo9n3yLBgrcw9z62ygt1siT9xai4UaJ2w4FPmY6kPCF96YN2cF",
    # Public key with depth 3 shall raise an exception
    "ex_pub_3": "xpub6BosfCnifzxcFwrSzQiqu2DBVTshkCXacvNsWGYJVVhhawA7d4R5WSWGFNbi8Aw6ZRc1brxMyWMzG3DSSSSoekkudhUd9yLb6qx39T9nMdj",
    # Public key with depth 5 is fine
    "ex_pub_5": "xpub6Fbrwk4KhC8qnFVXTcR3wRsqiTGkedcSSZKyTqKaxXjFN6rZv3UJYZ4mQtjNYY3gCa181iCHSBWyWst2PFiXBKgLpFVSdcyLbHyAahin8pd",
    # Public key with depth 6 shall raise an exception
    "ex_pub_6": "xpub6JtuhUVosPSgpBQFZS9oy6oorydcmXS66Kr2TmURvm8uu5wWBXRmRziMT85N4epgkVtwgxpt5FnduVJFi1ARiUcSELWhnZwp9Ge1icYFvhj",
}


#
# Tests
#
class Bip86Tests(unittest.TestCase):
    # Test specification name
    def test_spec_name(self):
        self.assertEqual(Bip86.SpecName(), "BIP-0086")

    # Run all tests in test vector using FromSeed for construction
    def test_from_seed(self):
        Bip44BaseTestHelper.test_from_seed(self, Bip86, TEST_VECT)

    # Run all tests in test vector using FromExtendedKey for construction
    def test_from_ex_key(self):
        Bip44BaseTestHelper.test_from_ex_key(self, Bip86, TEST_VECT)

    # Run all tests in test vector using FromPrivateKey for construction
    def test_from_priv_key(self):
        Bip44BaseTestHelper.test_from_priv_key(self, Bip86, TEST_VECT)

    # Test default path derivation
    def test_default_path_derivation(self):
        Bip44BaseTestHelper.test_default_path_derivation(self, Bip86, TEST_VECT_DEFAULT_PATH)

    # Test for IsLevel method
    def test_is_level(self):
        Bip44BaseTestHelper.test_is_level(self, Bip86, Bip86Coins, TEST_SEED)

    # Test different key formats
    def test_key_formats(self):
        Bip44BaseTestHelper.test_key_formats(self, Bip86, TEST_VECT_KEY_FORMATS)

    # Test construction from extended keys with valid and invalid depths
    def test_from_ex_key_depth(self):
        Bip44BaseTestHelper.test_from_ex_key_depth(self, Bip86, Bip86Coins, TEST_VECT_EX_KEY_DEPTHS)

    # Test type error during construction
    def test_type_error(self):
        Bip44BaseTestHelper.test_type_error(self, Bip86, [Bip44Coins, Bip49Coins, Bip84Coins])

    # Test invalid path derivations
    def test_invalid_derivations(self):
        Bip44BaseTestHelper.test_invalid_derivations(self, Bip86, Bip86Coins, TEST_SEED)
