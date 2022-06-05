"""Example of key derivation using BIP32 (ed25519 curve based on SLIP-0010)."""

from bip_utils import (
    Bip39WordsNum, Bip39MnemonicGenerator, Bip39SeedGenerator, Bip32Ed25519Slip, SolAddrEncoder
)

# Generate random mnemonic
mnemonic = Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_24)
print(f"Mnemonic string: {mnemonic}")
# Generate seed from mnemonic
seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

# Construct from seed, using ed25519 curve for key derivation
bip32_mst_ctx = Bip32Ed25519Slip.FromSeed(seed_bytes)
# Print master key
print(f"Master key (bytes): {bip32_mst_ctx.PrivateKey().Raw().ToHex()}")
print(f"Master key (extended): {bip32_mst_ctx.PrivateKey().ToExtended()}")

# Derive a path
bip32_der_ctx = bip32_mst_ctx.DerivePath("m/44'/501'/0'")
# Print key
print(f"Derived private key (bytes): {bip32_der_ctx.PrivateKey().Raw().ToHex()}")
print(f"Derived private key (extended): {bip32_der_ctx.PrivateKey().ToExtended()}")
print(f"Derived public key (bytes): {bip32_der_ctx.PublicKey().RawCompressed().ToHex()}")
print(f"Derived public key (extended): {bip32_der_ctx.PublicKey().ToExtended()}")

# Print address in Solana encoding
# The BIP32 elliptic curve shall be the same one expected by Solana (ed25519 in this case)
sol_addr = SolAddrEncoder.EncodeKey(bip32_der_ctx.PublicKey().KeyObject())
print(f"Address (SOL): {sol_addr}")
