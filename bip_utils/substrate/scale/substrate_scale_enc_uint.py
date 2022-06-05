# Copyright (c) 2022 Emanuele Bellocchia
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

"""Module for Substrate SCALE encoding for unsigned integers."""

# Imports
from typing import Any
from bip_utils.substrate.scale.substrate_scale_enc_base import SubstrateScaleEncoderBase
from bip_utils.utils.misc import IntegerUtils


class SubstrateScaleUIntEncoder(SubstrateScaleEncoderBase):
    """Substrate SCALE encoder class for generic unsigned integers."""

    m_bytes_num: int

    def __init__(self,
                 bytes_num: int) -> None:
        """
        Construct class.

        Args:
            bytes_num (int): Number of bytes of the integer
        """
        self.m_bytes_num = bytes_num
        self.m_max_val = (2 << (self.m_bytes_num * 8)) - 1

    def Encode(self,
               value: Any) -> bytes:
        """
        Encode the specified value to bytes.

        Args:
            value (Any): Value to be encoded

        Returns:
            bytes: Encoded value

        Raises:
            ValueError: If the value is not valid
        """
        if value < 0 or value > self.m_max_val:
            raise ValueError(f"Invalid integer value ({value})")
        return IntegerUtils.ToBytes(value, self.m_bytes_num, endianness="little")


class SubstrateScaleU8Encoder(SubstrateScaleUIntEncoder):
    """Substrate SCALE encoder class for 8-bit unsigned integers."""

    def __init__(self) -> None:
        """Construct class."""
        super().__init__(1)


class SubstrateScaleU16Encoder(SubstrateScaleUIntEncoder):
    """Substrate SCALE encoder class for 16-bit unsigned integers."""

    def __init__(self) -> None:
        """Construct class."""
        super().__init__(2)


class SubstrateScaleU32Encoder(SubstrateScaleUIntEncoder):
    """Substrate SCALE encoder class for 32-bit unsigned integers."""

    def __init__(self) -> None:
        """Construct class."""
        super().__init__(4)


class SubstrateScaleU64Encoder(SubstrateScaleUIntEncoder):
    """Substrate SCALE encoder class for 64-bit unsigned integers."""

    def __init__(self) -> None:
        """Construct class."""
        super().__init__(8)


class SubstrateScaleU128Encoder(SubstrateScaleUIntEncoder):
    """Substrate SCALE encoder class for 128-bit unsigned integers."""

    def __init__(self) -> None:
        """Construct class."""
        super().__init__(16)


class SubstrateScaleU256Encoder(SubstrateScaleUIntEncoder):
    """Substrate SCALE encoder class for 256-bit unsigned integers."""

    def __init__(self) -> None:
        """Construct class."""
        super().__init__(32)
