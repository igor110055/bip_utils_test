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

"""Module for BIP84 coins configuration."""

# Imports
from bip_utils.addr import P2WPKHAddrEncoder
from bip_utils.bip.bip32 import Bip32KeyNetVersions, Bip32Secp256k1
from bip_utils.bip.conf.common import BipCoinConf, NOT_HARDENED_DEF_PATH
from bip_utils.coin_conf import CoinsConf


# Bitcoin key net version (zpub / zprv)
_BIP84_BTC_KEY_NET_VER: Bip32KeyNetVersions = Bip32KeyNetVersions(b"\x04\xb2\x47\x46",
                                                                  b"\x04\xb2\x43\x0c")


class Bip84Conf:
    """Class container for Bip84 configuration."""

    # Configuration for Bitcoin main net
    BitcoinMainNet: BipCoinConf = BipCoinConf(
        coin_names=CoinsConf.BitcoinMainNet.CoinNames(),
        coin_idx=0,
        is_testnet=False,
        def_path=NOT_HARDENED_DEF_PATH,
        key_net_ver=_BIP84_BTC_KEY_NET_VER,
        wif_net_ver=CoinsConf.BitcoinMainNet.Params("wif_net_ver"),
        bip32_cls=Bip32Secp256k1,
        addr_cls=P2WPKHAddrEncoder,
        addr_params={
            "hrp": CoinsConf.BitcoinMainNet.Params("p2wpkh_hrp"),
        },
    )
    # Configuration for Bitcoin test net
    BitcoinTestNet: BipCoinConf = BipCoinConf(
        coin_names=CoinsConf.BitcoinTestNet.CoinNames(),
        coin_idx=1,
        is_testnet=True,
        def_path=NOT_HARDENED_DEF_PATH,
        key_net_ver=Bip32KeyNetVersions(b"\x04\x5f\x1c\xf6",
                                        b"\x04\x5f\x18\xbc"),   # vpub / vprv
        wif_net_ver=CoinsConf.BitcoinTestNet.Params("wif_net_ver"),
        bip32_cls=Bip32Secp256k1,
        addr_cls=P2WPKHAddrEncoder,
        addr_params={
            "hrp": CoinsConf.BitcoinTestNet.Params("p2wpkh_hrp"),
        },
    )

    # Configuration for Litecoin main net
    LitecoinMainNet: BipCoinConf = BipCoinConf(
        coin_names=CoinsConf.LitecoinMainNet.CoinNames(),
        coin_idx=2,
        is_testnet=False,
        def_path=NOT_HARDENED_DEF_PATH,
        key_net_ver=_BIP84_BTC_KEY_NET_VER,
        wif_net_ver=CoinsConf.LitecoinMainNet.Params("wif_net_ver"),
        bip32_cls=Bip32Secp256k1,
        addr_cls=P2WPKHAddrEncoder,
        addr_params={
            "hrp": CoinsConf.LitecoinMainNet.Params("p2wpkh_hrp"),
        },
    )
    # Configuration for Litecoin test net
    LitecoinTestNet: BipCoinConf = BipCoinConf(
        coin_names=CoinsConf.LitecoinTestNet.CoinNames(),
        coin_idx=1,
        is_testnet=True,
        def_path=NOT_HARDENED_DEF_PATH,
        key_net_ver=Bip32KeyNetVersions(b"\x04\x36\xf6\xe1",
                                        b"\x04\x36\xef\x7d"),   # ttub / ttpv
        wif_net_ver=CoinsConf.LitecoinTestNet.Params("wif_net_ver"),
        bip32_cls=Bip32Secp256k1,
        addr_cls=P2WPKHAddrEncoder,
        addr_params={
            "hrp": CoinsConf.LitecoinTestNet.Params("p2wpkh_hrp"),
        },
    )