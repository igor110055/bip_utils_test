"""Example of key derivation using BIP49."""

from bip_utils import (
    Bip39WordsNum, Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44Changes, Bip49Coins, Bip49
)

# Generate random mnemonic
mnemonic = Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_24)
print(f"Mnemonic string: {mnemonic}")
# Generate seed from mnemonic
seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

# Construct from seed
bip49_mst_ctx = Bip49.FromSeed(seed_bytes, Bip49Coins.LITECOIN)
# Print master key
print(f"Master key (bytes): {bip49_mst_ctx.PrivateKey().Raw().ToHex()}")
print(f"Master key (extended): {bip49_mst_ctx.PrivateKey().ToExtended()}")
print(f"Master key (WIF): {bip49_mst_ctx.PrivateKey().ToWif()}")

# Generate BIP49 account keys: m/49'/0'/0'
bip49_acc_ctx = bip49_mst_ctx.Purpose().Coin().Account(0)
# Generate BIP49 chain keys: m/49'/0'/0'/0
bip49_chg_ctx = bip49_acc_ctx.Change(Bip44Changes.CHAIN_EXT)

# Generate the first 10 addresses: m/49'/0'/0'/0/i
for i in range(10):
    bip49_addr_ctx = bip49_chg_ctx.AddressIndex(i)
    print(f"{i}. Address public key (extended): {bip49_addr_ctx.PublicKey().ToExtended()}")
    print(f"{i}. Address private key (extended): {bip49_addr_ctx.PrivateKey().ToExtended()}")
    print(f"{i}. Address: {bip49_addr_ctx.PublicKey().ToAddress()}")
