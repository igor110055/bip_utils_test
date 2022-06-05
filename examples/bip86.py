"""Example of key derivation using BIP86."""

from bip_utils import (
    Bip39WordsNum, Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44Changes, Bip86Coins, Bip86
)

# Generate random mnemonic
mnemonic = Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_24)
print(f"Mnemonic string: {mnemonic}")
# Generate seed from mnemonic
seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

# Construct from seed
bip86_mst_ctx = Bip86.FromSeed(seed_bytes, Bip86Coins.BITCOIN)
# Print master key
print(f"Master key (bytes): {bip86_mst_ctx.PrivateKey().Raw().ToHex()}")
print(f"Master key (extended): {bip86_mst_ctx.PrivateKey().ToExtended()}")
print(f"Master key (WIF): {bip86_mst_ctx.PrivateKey().ToWif()}")

# Generate BIP86 account keys: m/86'/0'/0'
bip86_acc_ctx = bip86_mst_ctx.Purpose().Coin().Account(0)
# Generate BIP86 chain keys: m/86'/0'/0'/0
bip86_chg_ctx = bip86_acc_ctx.Change(Bip44Changes.CHAIN_EXT)

# Generate the first 10 addresses: m/86'/0'/0'/0/i
for i in range(10):
    bip86_addr_ctx = bip86_chg_ctx.AddressIndex(i)
    print(f"{i}. Address public key (extended): {bip86_addr_ctx.PublicKey().ToExtended()}")
    print(f"{i}. Address private key (extended): {bip86_addr_ctx.PrivateKey().ToExtended()}")
    print(f"{i}. Address: {bip86_addr_ctx.PublicKey().ToAddress()}")
